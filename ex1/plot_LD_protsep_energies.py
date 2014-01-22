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
title(r'Proton Seperation Energies in the Liquid Drop Model',fontsize=15)     
# read in data from file
BEdata = loadtxt("mass/aud11.dat")
l = len(BEdata[:,0])

zx = BEdata[:,0]
nx = BEdata[:,1]-BEdata[:,0]
BEx = BEdata[:,2]

#### LIQUID DROP MODEL BE DATA  
for i in range(len(zx)):
    BEx[i] = liquid_drop_BE(nx[i],zx[i]) 

z=[]
n=[]
BE=[]
for i in range(1,130):
    for j in range(len(nx)):
        if int(nx[j]) == i:
            z.append(zx[j])
            n.append(nx[j])
            BE.append(BEx[j])

zlist=[]
nlist=[]
splist=[]

out=0
for i in range(1,len(z)):
    if z[i] > 82:
        pass
    elif int(n[i-1]) != int(n[i]):
        pass
    elif int(z[i-1]) != int(z[i]-1.): 
        pass
    elif n[i] == out:
        pass
    elif (BE[i] - BE[i-1]) < 0.0:
        out=n[i]        
    else:
        zlist.append(z[i])
        nlist.append(n[i])
        splist.append(BE[i]-BE[i-1])

axis([0,130,0,83])
xlabel(r'Neutron Number',fontsize=20)
ylabel(r'Proton Number',fontsize=20)

scatter(nlist, zlist , c=splist, s=20,vmin=0,vmax=26)

tks=[]
for i in range(9):
    tks.append(float(i)*3)
cbar=colorbar(ticks=tks)
lbls=[]
for i in range(9):
    lbls.append(str(tks[i]) + ' MeV')
lbls[8] = '> '+lbls[8]
cbar.set_ticklabels(lbls)

# Save the figure in a separate file
savefig('ProtonSeperation_liquiddrop.pdf', format='pdf')

# Draw the plot to screen
show()
