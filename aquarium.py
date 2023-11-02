#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: aquarium.py
#                                                                      Authors: 
#                                                                      Description: Keeps track of the values of relevant chemicals in an aquarium system over time.
#
#
#
#=====================================================================================================================================================================================================================
# Imports 
import numpy as np
import math
# =============================

# Constants
Xmin = 0
Xmax = (24*math.pi)
Ymin = -(6*math.pi)
Ymax = (5* math.pi)
Zmin = (-6* math.pi)
Zmax = (2* math.pi)
Wishbone = (5 * Math.pow(10,-6))
Wishbone1 = (2 * Math.pow(10,-8))
Wishbone2 = (3 * Math.pow(10,-6))
V = 3628800
tmin = 0
t = 0

def p1(t):
  step1 = numpy.arctan(t0(t))             
  step2 = step1 - numpy.arctan(t0(0))              
  step3 = Wishbone * step2

return step3

p2 = Math.pow(10,-4)
p3 = 0
p4 = (2* Math.pow(10,-17))
q1 = (1/5)
q2 = (1/8.5)

# Chemical Consentrations

C1 = 0 # NH4 (Ammonia)
C2 = 8.5 # O2 (Oxygen)
C3 = 0 # NO2 (NitrITE)
C4 = 0 # NO3 (NitrATE)

# Mu s

def mu1(t):
  result = Wishbone1*(np.acrtan(T1(t))-np.arctan(T1(tmin)))
  return result
  
def mu2(t):
  result = Wishbone2*(np.arctan(T2(t))-np.arctan(tmin))
  return result
  
def t0(t):
    return(((Xmax - Xmin) / V)*t + Xmin)

def t1(t):
    return(((Ymax - Ymin) / V)*t + Ymin)
    
def t2(t):
    return(((Zmax - Zmin) / V)*t + Zmin)  


# Change of concentration of Nitrate

def changeInAmmonia(t):
  oldAmmonia = C1
  step1 = p1 * (1 - ((1/5) * C1)
  step2 = step1 - mu1 * ((C1 * C1) * (C3 * C3))
  concentrationChange = step2
  return concentrationChange

def dC2(t):
    return p2(1-(1/5)(C2))-mu1(t)*pow(C1,2)*pow(C2,3)-mu2(t)*sqrt(C2)*C3
  
def dC3(t):
    return mu1(t)*(pow(C1,2))*(pow(C2,3))-mu2(t)*math.sqrt(C2)*C3-p3*C3

def dC4(t):    # Change of Nitrate concentration over time 
  dt = (Math.abs(0-t))
  dC4 = dt(mu2*Math.sqrt(C2)*C3-(p4*C4))
  return dC4
  
  
