program Lipkin_HF
!HF solver for 4 particle Lipkin Model
  implicit none 
  
  real(8) :: crit,eps,V,W,e1,e2,EHF
  real,dimension(2,2) :: FOCK,C
  real,dimension(2) :: evals,eold
  integer :: i,j,kd,p,q,s,n
  
  print*, 'epsilon? '
  read*, eps
  print*, 'V? '
  read*, V
  print*, 'W? '
  read*, W
  
  !initial conditions ( C = 1  is a stationary point ) 
  C  = sqrt( .1 ) 
  C(1,1) = sqrt(.9)
  C(2,2) = sqrt(.9)

  eold = (/100.,200./)
  crit =10.
  j=0
  
do while (crit > 1e-6) 
  !fock matrix is easy to construct
  Fock(1,1) = -1.*eps/2.d0 -  W * C(2,1)*C(2,1)
  Fock(2,2) =  eps/2.d0 -  W * C(1,1)*C(1,1) 
  Fock(1,2) = (3 * V  +  4 *W )* C(2,1) * C(1,1) 
  Fock(2,1) = Fock(1,2) 
 
  !eigenvalues calculated
  e1 = (Fock(1,1) + Fock(2,2))/2.d0 + 0.5*sqrt((Fock(1,1)-Fock(2,2))**2 + &
       4. * Fock(1,2)**2 ) 
  e2 = (Fock(1,1) + Fock(2,2))/2.d0 - 0.5*sqrt((Fock(1,1)-Fock(2,2))**2 + &
       4. * Fock(1,2)**2 ) 
  
  evals(1) = min(e1,e2) 
  evals(2) = max(e1,e2) 
  
  ! calculate eigenvectors
  if (Fock(1,2) == 0.d0) then 
     C = 0.d0
     C(1,1) = 1.
     C(2,2) = 1.
  else  
     C(1,1) = 1.
     C(2,1) = -1*(Fock(1,1) - evals(1))/Fock(1,2) 
     C(1,2) = 1.
     C(2,2) = -1*(Fock(1,1) - evals(2))/Fock(1,2)
  end if 
 
  !normalize eigenvectors
  C(:,1) = C(:,1) / sqrt(Sum(C(:,1)**2))  
  C(:,2) = C(:,2) / sqrt(Sum(C(:,2)**2))
 
  !convergence check
  crit = sum(abs(evals - eold))/2.d0
  eold = evals
  j=j+1

end do 

print*
print*
print*,'================================'
write(*,'(A,I3)') ' number of iterations for convergence:',j
write(*,'(A,2(f10.5))') ' HF Orbital Energies:', evals
EHF = 4*evals(1) -12*(V+W)*( C(1,1) * C(2,1) ) ** 2 
write(*,'(A,f10.5)') ' HF Energy:', EHF

print*
print*, 'eigenvectors in columns: ' 
do i=1,2
   write(*,'(2(f10.5))') C(i,:)
end do 
print*,'================================' 

end program  
