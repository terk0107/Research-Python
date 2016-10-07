# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:41:24 2016

@author: KaeCee

Code created in Spyder 2.3.9 (Python 3.5)

"""
import numpy
import matplotlib.pyplot as plt
from scipy import *
import math

DiaThree = 68./1000
DiaTwo = 42.8/1000
DiaOne = 17.4/1000
AthreeIn = math.pi*(DiaThree/2)**2
AtwoIn = math.pi*(DiaTwo/2)**2
AoneIn = math.pi*(DiaOne/2)**2
flowRate = []
VthreeIn = []
VtwoIn = []
VoneIn = []
VelocityHeadThree = []
VelocityHeadTwo = []
VelocityHeadOne = []

ReynoldsThree = numpy.empty([15,450])
ReynoldsTwo = numpy.empty([15,450])
ReynoldsOne = numpy.empty([15,450])



for k in range(1, 16, 1): # for k = 1:15, range(first, end (not included), step)
    flowRate.append(k/3600)
    VthreeIn.append(flowRate[k-1]/AthreeIn)
    VtwoIn.append(flowRate[k-1]/AtwoIn)
    VoneIn.append(flowRate[k-1]/AoneIn)
    
    VelocityHeadThree.append((VthreeIn[k-1])**2/(2*9.8))
    VelocityHeadTwo.append((VtwoIn[k-1])**2/(2*9.8))
    VelocityHeadOne.append((VoneIn[k-1])**2/(2*9.8))
    
    T = []
    DensityPb = []
    ViscosityPb = []
    
    for i in range(1, 451): # range is limited to intergers, NumPy adds "arange" function for floats
        T.append(249+273+i)
        DensityPb.append(11441-1.2795*T[i-1]) # kg/m^3
        ViscosityPb.append(4.55e-4*math.exp(1069/T[i-1])*(1/DensityPb[i-1])) # m^2/s
            
        ReynoldsThree[k-1][i-1] = (flowRate[k-1]*DiaThree)/(ViscosityPb[i-1]*AthreeIn)
        ReynoldsTwo[k-1,i-1] = (flowRate[k-1]*DiaTwo)/(ViscosityPb[i-1]*AtwoIn)
        ReynoldsOne[k-1,i-1] = (flowRate[k-1]*DiaOne)/(ViscosityPb[i-1]*AoneIn)
        


plt.plot(T, DensityPb)
plt.title('Temperature vs Density')
plt.xlabel('Temperature (K)')
plt.ylabel('Density of Pb (kg/m^3)')
plt.show()


plt.plot(T, ViscosityPb)
plt.title('Temperature vs Viscosity')
plt.xlabel('Temperature (K)')
plt.ylabel('Viscosity of Lead (m^2/s)')
#plt.ylim(min(ViscosityPb), max(ViscosityPb))
plt.show()

plt.plot(T, ReynoldsThree[0], label='1 m^3/hr')
plt.plot(T, ReynoldsThree[1], label='2 m^3/hr')
plt.plot(T, ReynoldsThree[2], label='3 m^3/hr')
plt.plot(T, ReynoldsThree[3], label='4 m^3/hr')
plt.plot(T, ReynoldsThree[4], label='5 m^3/hr')
plt.plot(T, ReynoldsThree[5], label='6 m^3/hr')
plt.plot(T, ReynoldsThree[6], label='7 m^3/hr')
plt.plot(T, ReynoldsThree[7], label='8 m^3/hr')
plt.plot(T, ReynoldsThree[8], label='9 m^3/hr')
plt.plot(T, ReynoldsThree[9], label='10 m^3/hr')
plt.plot(T, ReynoldsThree[10], label='11 m^3/hr')
plt.plot(T, ReynoldsThree[11], label='12 m^3/hr')
plt.plot(T, ReynoldsThree[12], label='13 m^3/hr')
plt.plot(T, ReynoldsThree[13], label='14 m^3/hr')
plt.plot(T, ReynoldsThree[14], label='15 m^3/hr')
plt.title('Temperature vs Reynolds No. for Three inch Pipe')
plt.xlabel('Temperature (K)')
plt.ylabel('Reynolds Number')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()


plt.plot(T, ReynoldsTwo[0], label='1 m^3/hr')
plt.plot(T, ReynoldsTwo[1], label='2 m^3/hr')
plt.plot(T, ReynoldsTwo[2], label='3 m^3/hr')
plt.plot(T, ReynoldsTwo[3], label='4 m^3/hr')
plt.plot(T, ReynoldsTwo[4], label='5 m^3/hr')
plt.plot(T, ReynoldsTwo[5], label='6 m^3/hr')
plt.plot(T, ReynoldsTwo[6], label='7 m^3/hr')
plt.plot(T, ReynoldsTwo[7], label='8 m^3/hr')
plt.plot(T, ReynoldsTwo[8], label='9 m^3/hr')
plt.plot(T, ReynoldsTwo[9], label='10 m^3/hr')
plt.plot(T, ReynoldsTwo[10], label='11 m^3/hr')
plt.plot(T, ReynoldsTwo[11], label='12 m^3/hr')
plt.plot(T, ReynoldsTwo[12], label='13 m^3/hr')
plt.plot(T, ReynoldsTwo[13], label='14 m^3/hr')
plt.plot(T, ReynoldsTwo[14], label='15 m^3/hr')
plt.title('Temperature vs Reynolds No. for Two inch Pipe')
plt.xlabel('Temperature (K)')
plt.ylabel('Reynolds Number')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()


plt.plot(T, ReynoldsOne[0], label='1 m^3/hr')
plt.plot(T, ReynoldsOne[1], label='2 m^3/hr')
plt.plot(T, ReynoldsOne[2], label='3 m^3/hr')
plt.plot(T, ReynoldsOne[3], label='4 m^3/hr')
plt.plot(T, ReynoldsOne[4], label='5 m^3/hr')
plt.plot(T, ReynoldsOne[5], label='6 m^3/hr')
plt.plot(T, ReynoldsOne[6], label='7 m^3/hr')
plt.plot(T, ReynoldsOne[7], label='8 m^3/hr')
plt.plot(T, ReynoldsOne[8], label='9 m^3/hr')
plt.plot(T, ReynoldsOne[9], label='10 m^3/hr')
plt.plot(T, ReynoldsOne[10], label='11 m^3/hr')
plt.plot(T, ReynoldsOne[11], label='12 m^3/hr')
plt.plot(T, ReynoldsOne[12], label='13 m^3/hr')
plt.plot(T, ReynoldsOne[13], label='14 m^3/hr')
plt.plot(T, ReynoldsOne[14], label='15 m^3/hr')
plt.title('Temperature vs Reynolds No. for One inch Pipe')
plt.xlabel('Temperature (K)')
plt.ylabel('Reynolds Number')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()


plt.plot(flowRate, VelocityHeadOne)
plt.title('Flow Rate vs Velocity Head for One inch Pipe')
plt.xlabel('Flow rate (m/s)')
plt.ylabel('Velocity Head (m)')
plt.show()

'''plotting resources
http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut1.html
http://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend

python resources
https://docs.python.org/3.5/search.html

'''