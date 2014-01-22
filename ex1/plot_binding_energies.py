def liquid_drop_BE(N,Z):
    a1=15.49
    a2=17.23
    a3=0.697
    a4=22.6
    
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

z = BEdata[:,0]
a = BEdata[:,1]
BE = BEdata[:,2]

bpn=[]
alist=[]
bpnliq=[]
for i in range(1,len(z)):
    if z[i] > 82:
        break
    bpn.append(BE[i]/a[i])
    alist.append(a[i])
    bpnliq.append(liquid_drop_BE(a[i]-z[i],z[i])/a[i])

axis([0,220,0,10])
xlabel(r'Atomic Number',fontsize=20)
ylabel(r'Energy (MeV)',fontsize=20)

scatter(alist, bpnliq, color='r', s=1)
scatter(alist, bpn , color='k', s=1)

p1 = Rectangle((0, 0), 1, 1, fc="k")
p2 = Rectangle((0, 0), 1, 1, fc="r")
legend((p1, p2), ('experiment','liquid drop'))

# Save the figure in a separate file
savefig('bindingenergy.pdf', format='pdf')

# Draw the plot to screen
show()
