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
import matplotlib.pyplot as plt


# Constants
Xmin = 0
Xmin = 0
Xmax = (24*math.pi)
Ymin = -(6*math.pi)
Ymax = (5* math.pi)
Zmin = (-6* math.pi)
Zmax = (2* math.pi)
Wishbone = (5 * pow(10,-6))
Wishbone1 = (2 * pow(10,-8))
Wishbone2 = (3 * pow(10,-6))
V = 4838400
tmin = 0

def p1(t):
  step1 = np.arctan(t0(t))             
  step2 = step1 - np.arctan(t0(0))              
  step3 = Wishbone * step2
  return step3

p2 = pow(10,-4)
p3 = 0
p4 = (2* pow(10,-17))
q1 = (1/5)
q2 = (1/8.5)

# Chemical Consentrations

C1 = 0 # NH4 (Ammonia)
C2 = 8.5 # O2 (Oxygen)
C3 = 0 # NO2 (NitrITE)
C4 = 0 # NO3 (NitrATE)

C1i = 0 # NH4 (Ammonia)
C2i = 8.5 # O2 (Oxygen)
C3i = 0 # NO2 (NitrITE)
C4i = 0 # NO3 (NitrATE)

dC1 = [] # Array of NH4 Conc
dC2 = [] # Array of O2 Conc
dC3 = [] # Array of Nitrite Conc
dC4 = [] # Array of Nitrate Conc
dT = [] # Time array

# Define Functions
# Mu s
def mu1(t):
  result = Wishbone1*(np.arctan([t1(t)])-np.arctan([t1(tmin)]))
  return result
  
def mu2(t):
  result = Wishbone2*(np.arctan(t2(t))-np.arctan(t2(tmin)))
  return result
  
def t0(t):
    return(((Xmax - Xmin) / V)*t + Xmin)

def t1(t):
    return(((Ymax - Ymin) / V)*t + Ymin)
    
def t2(t):
    return(((Zmax - Zmin) / V)*t + Zmin)  


# Change of concentration of Nitrate

def changeInAmmonia(t):
  step1 = p1(t) * (1 - ((q1) * C1))
  step2 = step1 - mu1(t) * ((C1 * C1) * (C2 * C2 * C2))
  concentrationChange = step2
  return concentrationChange



def changeInOxygen(t):    # Change of Oxygen concentration over time 
    result = p2*(1-(q1)*(C2))-mu1(t)*pow(C1,2)*pow(C2,3)-mu2(t)*math.sqrt(C2)*C3
    return result
  
def changeInNitrite(t):    # Change of Nitrite concentration over time 
    result = mu1(t)*(pow(C1,2))*(pow(C2,3))-mu2(t)*math.sqrt(C2)*C3-p3*C3
    return result

def changeInNitrate(t):    # Change of Nitrate concentration over time 
  dt = 1
  dC4 = dt*(mu2(t)* math.sqrt(C2)*C3-(p4*C4))
  return dC4


   
   


# Write a plot function

#======================================================================================================================================
# Sim Start 
#======================================================================================================================================
t = 0
while t < V:
    # Update Values
    C1 += changeInAmmonia(t)
    C2 += changeInOxygen(t)
    C3 += changeInNitrite(t)
    C4 += changeInNitrate(t)
    # Append Values to Concetration Arrays
    dC1.append(C1-C1i)
    #dC2.append(C2-C2i)
    dC3.append(C3-C3i)
    dC4.append(C4-C4i)
    # Update Time
    t += 1
    dT.append(t)
#======================================================================================================================================
# Plotting Start
#======================================================================================================================================
 # Create a figure and axis
fig, ax = plt.subplots()

# Plotting the data
ax.plot(dT, dC1, label='Ammonia')
#ax.plot(dT, dC2, label='Oxygen')
ax.plot(dT, dC3, label='Nitrite')
ax.plot(dT, dC4, label='Nitrate')
# Adding a legend, title, and labels
ax.legend()
ax.set_title('Aquarium Chemicals Over Time')
ax.set_xlabel('Time (Seconds)')
ax.set_ylabel('Change in Concentration')



# Display the plot
plt.show() 
  