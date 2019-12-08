import numpy as np
import sys
import matplotlib.pyplot as plt
import math as mt

ho = float(input('Please input the Height of the object with reference to the ground: '))
vo = float(input('Please input the Initial velocity of the object: '))
theta = float(input('Please input the angle it exited the initial height: '))
ax = float(input('Please input the acceleration in the x axis: '))
ay = float(input('Please input the acceleration in the y axis: '))
#Asks for user input of the initial height, velocity, angle theta, and acceleration
#in x and y components

if ay == 0:
    sys.exit('Please input a non zero vertical acceleration component. Thank you')
#exits the program when a zero vertical acceleration is given

realth= mt.radians(theta)            #Code block for computation of
vox = vo*mt.cos(realth)              #Variables to find x and y 
voy = vo*mt.sin(realth)
d = mt.sqrt(voy**2 - 4*(1/2*ay)*ho)
t1 = (-voy + d )/ ay
t2 = (-voy - d )/ ay

if t1 <= 0:                          #Conditional statement checking for the positive time
    t1 = t2                          #From the two roots given by the kinematic equation
    x = vox*np.linspace(0,t1) + 1/2*ax*np.linspace(0,t1)**2
    y = voy*np.linspace(0,t1) + 1/2*ay*np.linspace(0,t1)**2
else:
    x = vox*np.linspace(0,t1) + 1/2*ax*np.linspace(0,t1)**2
    y = voy*np.linspace(0,t1) + 1/2*ay*np.linspace(0,t1)**2
    
plt.plot(x,y)                        #Plots the x and y as it goes through the whole plane
plt.xlabel('Trajectory as it goes in the X direction')
plt.ylabel('Trajectory as it goes in the Y direction')
plt.grid()
plt.show()