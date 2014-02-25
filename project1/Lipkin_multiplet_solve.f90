program Lipkin_multiplet_solve
  ! Solves the J=2 Lipkin model
  implicit none 

  
  integer :: i,j,d,info
  real(8) :: eps, V, W
  real(8),dimension(5,5) :: H0,H1,H2,H
  real(8),dimension(5) :: Jz,eig,etest
  real(8),dimension(50) :: dwork

  print*, 'Enter epsilon: '
  read*, eps
  print*, 'Enter V: '
  read*, V
  print*, 'Enter W: ' 
  read*, W
  
  Jz = (/ -2. , -1. , 0. , 1. , 2. /)
  H0=0.
  H2=0.
  H1=0.
  
  do i=1,5
     H0(i,i) = Jz(i)
     H2(i,i) = ( 4 - Jz(i)**2 ) 
  end do 
 
  do j = 3,5
     H1(j-2,j) = sqrt( ( 6- Jz(j) * (Jz(j)-1) ) *&
          (6 - (Jz(j)-2) * (Jz(j)-1) ) ) 
  end do 
  
  do j=1,3
     H1(j+2,j) = sqrt( ( 6- Jz(j) * (Jz(j)+1) ) *&
          (6 - (Jz(j)+2) * (Jz(j)+1) ) ) 
   end do 
   
   H0=H0*eps
   H1=H1*V/2.d0
   H2=H2*W
     
   H = H0 + H1 + H2 
   d = 5
  
   ! LAPACK routine eig holds eigenvalues
   ! H receives eigenvectors in columns
   
   
   call dsyev('V','U',d,H,d,eig,dwork,10*d,info) 
  
   print*
   print*, '==================================='
   print*, 'eigenvalue, eigenvector pairs' 
   print*
   do i=1,d
      write(*,'(f10.5)') eig(i)
      write(*,'(5(f10.5))') H(:,i) 
      print*
   end do

   print*, '==================================='
end program
      
      


