'''asteroidbelt.py'''

from visual import*
from visual.graph import*
from random import *
from math import *

G = 6.67e-11
AU = 1.5e11
year = 365.25*24.*60.*60.
r0 = 5.2*AU*pow(2./3.,2./3.)
asteroidpos = []
asteroidvel = []

sun = sphere(pos=(0,0,0), radius = 100*7e8, mass = 2.e30, color = color.yellow)
jupiter = sphere(pos=(5.2*AU,0,0), radius=8000.*6.4e6, mass = 9.0e25, color=color.red)
jupiter.vel = vector(0,sqrt(G*sun.mass/(5.2*AU)),0)

asteroid_list = []
for i in range(0,100):
    angle = i*2*pi/100
    asteroid = ellipsoid(pos=(r0*cos(angle), r0*sin(angle),0), length= 300*6.4E7, width = 200.*6.4e7, height = 200*6.4e7, color = (1,1,0))
    asteroid.vel = vector(-sqrt(G*sun.mass/r0)*sin(angle),sqrt(G*sun.mass/r0)*cos(angle),0.1*sqrt(G*sun.mass/r0))
    asteroid_list.append(asteroid)

plot = gdisplay(x=0, y = 400, height = 400, width = 600, title = "r vs. t", xtitle = 't', ytitle = 'r')
data = gdots(color=color.white)

dt = 1.e6
t = 0.0

while True:
    for asteroid in asteroid_list:
        asteroid.vel = asteroid.vel + (-G*sun.mass*(asteroid.pos - sun.pos)/mag(asteroid.pos - sun.pos)**3 - G*jupiter.mass*(asteroid.pos-jupiter.pos)/mag(asteroid.pos-jupiter.pos)**3)*dt
        asteroid.pos = asteroid.pos + asteroid.vel*dt
    data.plot(pos=(t/year, mag(asteroid.pos/r0)-1))

    jupiter.vel = jupiter.vel + -G*sun.mass*(jupiter.pos-sun.pos)/mag(jupiter.pos-sun.pos)**3*dt
    jupiter.pos = jupiter.pos + jupiter.vel*dt
    t+=dt
    rate(100)

    asteroidpos.append(asteroid.pos)
    asteroidvel.append(asteroid.vel)

file=open("asteroiddata.txt","w")
print >> file, asteroidpos, asteroidvel
file.close()

#----------------------------------------------------------------------
#For a 3:1 ratio the change in the max y value on the graph is much smaller. Also it becomes more frequent
