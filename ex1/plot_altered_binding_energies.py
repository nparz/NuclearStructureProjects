def liquid_drop_BE(N,Z,x):
    a1=15.49
    a2=17.23
    a3=0.697
    a4=22.6
    
    if x==1:
        a2=0.0
        a3=0.0
        a4=0.0
    elif x==2:
        a3=0.0
        a4=0.0
    elif x==3:
        a3=0.0
    
    
    res = a1* (N+Z) - a2*(N+Z)**(2./3.)
    res -= a3*Z*Z/(N+Z)**(1./3.) 
    res -= a4*(N-Z)*(N-Z)/(N+Z)
    return res

from numpy import *
from pylab import *
from matplotlib import rc, rcParams
import matplotlib.units as units
import matplotlib.ticker as ticker
import sys
import os

### ERASE THE FIRST TWO LINES OF THE FILE BEFORE YOU RUN THIS

# set tickers etc
#rc('text',usetex=True)
#rc('font',**{'family':'serif','serif':['Binding energies']})
#title(r'{\bf Neutron Seperation energies}', fontsize=20)
title(r'Binding Energy per Nucleon',fontsize=20)     
# read in data from file
BEdata = loadtxt("mass/aud11.dat")
l = len(BEdata[:,0])

z=[]
a=[]
BE=[]

for i in range(220):
    mx=0.0
    mxj = 0 
    for j in range(l):
        if int(BEdata[j,1]) == i:
            if BEdata[j,2] > mx:
                mx = BEdata[j,2] 
                mxj=j 
              
    z.append(BEdata[mxj,0])
    a.append(BEdata[mxj,1])
    BE.append(BEdata[mxj,2])


bpn=[]
alist=[]
bpnliq=[]
bpn1=[]
bpn2=[]
bpn3=[]

for i in range(1,len(z)):
    if z[i] > 82:
        break
    bpn.append(BE[i]/a[i])
    alist.append(a[i])
    bpnliq.append(liquid_drop_BE(a[i]-z[i],z[i],0)/a[i])
    bpn1.append(liquid_drop_BE(a[i]-z[i],z[i],1)/a[i])
    bpn2.append(liquid_drop_BE(a[i]-z[i],z[i],2)/a[i])
    bpn3.append(liquid_drop_BE(a[i]-z[i],z[i],3)/a[i])


axis([0,220,0,20])
xlabel(r'Atomic Number',fontsize=20)
ylabel(r'Energy (MeV)',fontsize=20)



scatter(alist, bpn , color='k', s=5)
scatter(alist, bpnliq, color='r', s=5)
scatter(alist, bpn1, color='b', s=5)
scatter(alist, bpn2, color='c', s=5)
scatter(alist, bpn3, color='m', s=5)

p1 = Rectangle((0, 0), 1, 1, fc="k")
p2 = Rectangle((0, 0), 1, 1, fc="r")
p3 = Rectangle((0, 0), 1, 1, fc="b")
p4 = Rectangle((0, 0), 1, 1, fc="c")
p5 = Rectangle((0, 0), 1, 1, fc="m")

legend((p1, p2, p3, p4, p5), ('experiment','liquid drop','volume only',\
'volume+surface','volume+surface+coulomb'), loc=4)

# Save the figure in a separate file
savefig('liquid_drop_variations.pdf', format='pdf')

# Draw the plot to screen
show()
