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
title(r'Neutron Seperation Energies',fontsize=20)     
# read in data from file
BEdata = loadtxt("mass/aud11.dat")
l = len(BEdata[:,0])

z = BEdata[:,0]
n = BEdata[:,1]-BEdata[:,0]
BE = BEdata[:,2]

zlist=[]
nlist=[]
snlist=[]

out=0
for i in range(1,len(z)):
    if z[i] > 82:
        break
    if int(z[i-1]) != int(z[i]):
        pass
    elif int(n[i-1]) != int(n[i]-1):
        pass
    elif z[i] == out:
        pass
    elif (BE[i] - BE[i-1]) < 0.0:
        out=z[i]        
    else:
        zlist.append(z[i])
        nlist.append(n[i])
        snlist.append(BE[i]-BE[i-1])

axis([0,130,0,83])
xlabel(r'Neutron Number',fontsize=20)
ylabel(r'Proton Number',fontsize=20)

scatter(nlist, zlist , c=snlist, s=20, vmin=0.0, vmax=24)
tks=[]
for i in range(10):
    tks.append(float(i)*2.5)
cbar=colorbar(ticks=tks)
lbls=[]
for i in range(10):
    lbls.append(str(tks[i]) + ' MeV')
lbls[9] = '> '+lbls[9]
cbar.set_ticklabels(lbls)

# Save the figure in a separate file
savefig('NeutronSeperation.pdf', format='pdf')

# Draw the plot to screen
show()
