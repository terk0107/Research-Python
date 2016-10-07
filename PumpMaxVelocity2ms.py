# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:15:52 2016

@author: KaeCee
Code created in Spyder 2.3.9 (Python 3.5)

"""
import numpy
import matplotlib.pyplot as plt
from scipy import *
import math

plt.close("all")

DiaThree = 68./1000
DiaTwo = 42.8/1000
DiaOne = 17.4/1000
AthreeIn = math.pi*(DiaThree/2)**2
AtwoIn = math.pi*(DiaTwo/2)**2
AoneIn = math.pi*(DiaOne/2)**2
flowRate3 = []
flowRate2 = []
flowRate1 = []
m=.14 
velocity = []
VelocityHeadThree = []
VelocityHeadTwo = []
VelocityHeadOne = []

ReynoldsThree = numpy.empty([15,450])
ReynoldsTwo = numpy.empty([15,450])
ReynoldsOne = numpy.empty([15,450])

for k in range(1, 16, 1): # for k = 1:15, range(first, end (not included), step)
      
    velocity.append(m)
    
    flowRate3.append(velocity[k-1]*AthreeIn)
    flowRate2.append(velocity[k-1]*AtwoIn)
    flowRate1.append(velocity[k-1]*AoneIn)
     
    VelocityHeadThree.append((velocity[k-1])**2/(2*9.8))
    VelocityHeadTwo.append((velocity[k-1])**2/(2*9.8))
    VelocityHeadOne.append((velocity[k-1])**2/(2*9.8))
    
    T = []
    DensityPb = []
    ViscosityPb = []
    
    for i in range(1, 451): # range is limited to intergers, NumPy adds "arange" function for floats
        T.append(249+273+i)
        DensityPb.append(11441-1.2795*T[i-1]) # kg/m^3
        ViscosityPb.append(4.55e-4*math.exp(1069/T[i-1])*(1/DensityPb[i-1])) # m^2/s
            
        ReynoldsThree[k-1][i-1] = (flowRate3[k-1]*DiaThree)/(ViscosityPb[i-1]*AthreeIn)
        ReynoldsTwo[k-1,i-1] = (flowRate2[k-1]*DiaTwo)/(ViscosityPb[i-1]*AtwoIn)
        ReynoldsOne[k-1,i-1] = (flowRate1[k-1]*DiaOne)/(ViscosityPb[i-1]*AoneIn)
        
    m=m+.14

plt.figure(1)
plt.plot(flowRate3, VelocityHeadThree)
plt.title('Flow Rate vs Velocity Head for Three inch Pipe')
plt.xlabel('Flow rate (m^3/s)')
plt.ylabel('Velocity Head (m)')
plt.show()

plt.figure(2)
plt.scatter(velocity[0], flowRate3[0]*3600)
plt.scatter(velocity[1], flowRate3[1]*3600)
plt.scatter(velocity[2], flowRate3[2]*3600)
plt.scatter(velocity[3], flowRate3[3]*3600)
plt.scatter(velocity[4], flowRate3[4]*3600)
plt.scatter(velocity[5], flowRate3[5]*3600)
plt.scatter(velocity[6], flowRate3[6]*3600)
plt.scatter(velocity[7], flowRate3[7]*3600)
plt.scatter(velocity[8], flowRate3[8]*3600)
plt.scatter(velocity[9], flowRate3[9]*3600)
plt.scatter(velocity[10], flowRate3[10]*3600)
plt.scatter(velocity[11], flowRate3[11]*3600)
plt.scatter(velocity[12], flowRate3[12]*3600)
plt.scatter(velocity[13], flowRate3[13]*3600)
plt.scatter(velocity[14], flowRate3[14]*3600)
plt.title('Velocity vs Flow Rate for Three inch Pipe')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Flow Rate (m^3/hr)')
#plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

plt.figure(3)
plt.plot(T, ReynoldsThree[0], label=str(round(flowRate3[0]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[1], label=str(round(flowRate3[1]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[2], label=str(round(flowRate3[2]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[3], label=str(round(flowRate3[3]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[4], label=str(round(flowRate3[4]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[5], label=str(round(flowRate3[5]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[6], label=str(round(flowRate3[6]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[7], label=str(round(flowRate3[7]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[8], label=str(round(flowRate3[8]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[9], label=str(round(flowRate3[9]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[10], label=str(round(flowRate3[10]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[11], label=str(round(flowRate3[11]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[12], label=str(round(flowRate3[12]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[13], label=str(round(flowRate3[13]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsThree[14], label=str(round(flowRate3[14]*3600,2))+' m^3/hr')
plt.title('Temperature vs Reynolds No. for Three inch Pipe')
plt.xlabel('Temperature (K)')
plt.ylabel('Reynolds Number')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

plt.figure(4)
plt.plot(flowRate2, VelocityHeadTwo)
plt.title('Flow Rate vs Velocity Head for Two inch Pipe')
plt.xlabel('Flow rate (m^3/s)')
plt.ylabel('Velocity Head (m)')
plt.show()

plt.figure(5)
plt.scatter(velocity[0], flowRate2[0]*3600)
plt.scatter(velocity[1], flowRate2[1]*3600)
plt.scatter(velocity[2], flowRate2[2]*3600)
plt.scatter(velocity[3], flowRate2[3]*3600)
plt.scatter(velocity[4], flowRate2[4]*3600)
plt.scatter(velocity[5], flowRate2[5]*3600)
plt.scatter(velocity[6], flowRate2[6]*3600)
plt.scatter(velocity[7], flowRate2[7]*3600)
plt.scatter(velocity[8], flowRate2[8]*3600)
plt.scatter(velocity[9], flowRate2[9]*3600)
plt.scatter(velocity[10], flowRate2[10]*3600)
plt.scatter(velocity[11], flowRate2[11]*3600)
plt.scatter(velocity[12], flowRate2[12]*3600)
plt.scatter(velocity[13], flowRate2[13]*3600)
plt.scatter(velocity[14], flowRate2[14]*3600)
plt.title('Velocity vs Flow Rate for Two inch Pipe')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Flow Rate (m^3/hr)')
#plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

plt.figure(6)
plt.plot(T, ReynoldsTwo[0], label=str(round(flowRate2[0]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[1], label=str(round(flowRate2[1]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[2], label=str(round(flowRate2[2]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[3], label=str(round(flowRate2[3]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[4], label=str(round(flowRate2[4]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[5], label=str(round(flowRate2[5]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[6], label=str(round(flowRate2[6]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[7], label=str(round(flowRate2[7]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[8], label=str(round(flowRate2[8]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[9], label=str(round(flowRate2[9]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[10], label=str(round(flowRate2[10]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[11], label=str(round(flowRate2[11]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[12], label=str(round(flowRate2[12]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[13], label=str(round(flowRate2[13]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsTwo[14], label=str(round(flowRate2[14]*3600,2))+' m^3/hr')
plt.title('Temperature vs Reynolds No. for Two inch Pipe')
plt.xlabel('Temperature (K)')
plt.ylabel('Reynolds Number')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

plt.figure(7)
plt.plot(flowRate1, VelocityHeadOne)
plt.title('Flow Rate vs Velocity Head for One inch Pipe')
plt.xlabel('Flow rate (m^3/s)')
plt.ylabel('Velocity Head (m)')
plt.show()

plt.figure(8)
plt.scatter(velocity[0], flowRate1[0]*3600)
plt.scatter(velocity[1], flowRate1[1]*3600)
plt.scatter(velocity[2], flowRate1[2]*3600)
plt.scatter(velocity[3], flowRate1[3]*3600)
plt.scatter(velocity[4], flowRate1[4]*3600)
plt.scatter(velocity[5], flowRate1[5]*3600)
plt.scatter(velocity[6], flowRate1[6]*3600)
plt.scatter(velocity[7], flowRate1[7]*3600)
plt.scatter(velocity[8], flowRate1[8]*3600)
plt.scatter(velocity[9], flowRate1[9]*3600)
plt.scatter(velocity[10], flowRate1[10]*3600)
plt.scatter(velocity[11], flowRate1[11]*3600)
plt.scatter(velocity[12], flowRate1[12]*3600)
plt.scatter(velocity[13], flowRate1[13]*3600)
plt.scatter(velocity[14], flowRate1[14]*3600)
plt.title('Velocity vs Flow Rate for One inch Pipe')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Flow Rate (m^3/hr)')
#plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

plt.figure(9)
plt.plot(T, ReynoldsOne[0], label=str(round(flowRate1[0]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[1], label=str(round(flowRate1[1]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[2], label=str(round(flowRate1[2]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[3], label=str(round(flowRate1[3]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[4], label=str(round(flowRate1[4]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[5], label=str(round(flowRate1[5]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[6], label=str(round(flowRate1[6]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[7], label=str(round(flowRate1[7]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[8], label=str(round(flowRate1[8]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[9], label=str(round(flowRate1[9]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[10], label=str(round(flowRate1[10]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[11], label=str(round(flowRate1[11]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[12], label=str(round(flowRate1[12]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[13], label=str(round(flowRate1[13]*3600,2))+' m^3/hr')
plt.plot(T, ReynoldsOne[14], label=str(round(flowRate1[14]*3600,2))+' m^3/hr')
plt.title('Temperature vs Reynolds No. for One inch Pipe')
plt.xlabel('Temperature (K)')
plt.ylabel('Reynolds Number')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

