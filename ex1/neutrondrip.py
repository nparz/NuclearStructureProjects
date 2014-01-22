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


# set tickers etc
#rc('text',usetex=True)
#rc('font',**{'family':'serif','serif':['Binding energies']})
#title(r'{\bf Neutron Seperation energies}', fontsize=20)
title(r'Neutron Dripline',fontsize=20)     
# read in data from file
BEdata = loadtxt("mass/aud11.dat")
l = len(BEdata[:,0])

#z = BEdata[:,0]
#n = BEdata[:,1]-BEdata[:,0]
#BE = BEdata[:,2]

z=[]
n=[]
for i in range(1,125):
    for j in range(1,200):
        z.append(float(i)) 
        n.append(float(j))


BE=[]
#### LIQUID DROP MODEL BE DATA  
for i in range(len(z)):
    BE.append(liquid_drop_BE(n[i],z[i])) 

zlist=[]
nlist=[]

out=0
for i in range(1,len(z)):
    if z[i] > 120:
        break
    if int(z[i-1]) != int(z[i]):
        pass
    elif int(n[i-1]) != int(n[i]-1):
        pass
    elif z[i] == out:
        pass
    elif (BE[i] - BE[i-1]) < 0.0:
        out=z[i]        
        zlist.append(z[i])
        nlist.append(n[i])
 
z = BEdata[:,0]
n = BEdata[:,1]-BEdata[:,0]
BE = BEdata[:,2]   

zexp=[]
nexp=[]

out=0
for i in range(1,len(z)):
    if z[i] > 120:
        break
    if int(z[i-1]) != int(z[i]):
        pass
    elif int(n[i-1]) != int(n[i]-1):
        pass
    elif z[i] == out:
        pass
    elif (BE[i] - BE[i-1]) < 0.0:
        out=z[i]        
        zexp.append(z[i])
        nexp.append(n[i])
 
axis([0,120,0,60])
xlabel(r'Neutron Number',fontsize=20)
ylabel(r'Proton Number',fontsize=20)

plot(nlist, zlist , markersize=7)
scatter(nexp,zexp,color='k',s=5)

# Save the figure in a separate file
savefig('Neutrondripline.pdf', format='pdf')

# Draw the plot to screen
show()
