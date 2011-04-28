#!/usr/bin/python
######################################################################
##
## Vacuum tube plate characteristics graph ploter 
## for the Falstad.com Java circuit simulator.
##
## Author: Evan Salazar esalazar1981@gmail.com  
## Copyright Creative Commons CC BY-SA 2011
######################################################################
from pylab import *
import pylab as pl
from matplotlib.widgets import Slider, Button, RadioButtons

######################################
#Inital settings and graph charistics 
#for EL84 / 6BQ5 In Triod Mode
######################################
grid = np.arange(0.0,-16.5,-2.5)
mu0 = 18.44
kg10 = 286.89 
max_voltage = 300
max_current = 200

######################################
#Inital settings and graph charistics 
#for 12ax7
######################################
#grid = np.arange(0.0,-5,-.5)
#mu0 = 77.86
#kg10 = 627.25 
#max_voltage = 450.
#max_current = 4.0


print grid
mu= mu0
kg1 = kg10
l = range(12)
i=0;
for Vgk in grid:
    x = np.arange(0.0,max_voltage,10)
    Vpk = x;
    ip =((Vgk+Vpk/mu) **1.5)/kg1
    y = ip * 1000.0;
    pl.grid(color='b', linestyle='-', linewidth=.5)
    l[i], = plot(x,y,"k-",linewidth=1.5,label="%f" % (Vgk))
    i=i+1;

axis([0,max_voltage,0,max_current])
ax = subplot(111)
subplots_adjust(bottom=.25)

axcolor = 'lightgoldenrodyellow'
axmu = axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
axkg1  = axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

skg1 = Slider(axkg1, 'kg1', 1., 1500, valinit=kg10)
smu = Slider(axmu, 'mu', .1, 200.0, valinit=mu0)

def update(val):
    i=0
    for Vgk in grid:
	mu = smu.val
	kg1 = skg1.val
	x = np.arange(0.0,max_voltage,10)
	Vpk = x;
	ip =((Vgk+Vpk/mu) **1.5)/kg1
	y = ip * 1000.0;
	l[i].set_ydata(y);
	i=i+1
    draw()

smu.on_changed(update)
skg1.on_changed(update)

resetax = axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event):
    smu.reset()
    skg1.reset()
button.on_clicked(reset)
show()
