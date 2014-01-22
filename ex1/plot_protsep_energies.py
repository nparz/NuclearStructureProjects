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
title(r'Proton Seperation Energies',fontsize=20)     
# read in data from file
BEdata = loadtxt("mass/aud11.dat")
l = len(BEdata[:,0])

zx = BEdata[:,0]
nx = BEdata[:,1]-BEdata[:,0]
BEx = BEdata[:,2]

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

scatter(nlist, zlist , c=splist, s=20,vmin=0.0,vmax=26)
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
savefig('ProtonSeperation.pdf', format='pdf')

# Draw the plot to screen
show()
