#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: aquarium.py
#                                                                      Authors: 
#                                                                      Description: Keeps track of the values of relevant chemicals in an aquarium system over time.
#
#
#
#=====================================================================================================================================================================================================================


# Constants
Xmin = 0
Xmax = (24*math.pi)
Ymin = -(6*math.pi)
Ymax = (5* math.pi)
Zmin = (2* math.pi)
Zmax = (5* math.pow(10,-6))
Wishbone1 = (2 * Math.pow(10,-8))
Wishbone2 = (3 * Math.pow(10,-6))
V = 3628800
tmin = 0
t = 0

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

  


# Change of concentration of Nitrate

def dC4(t):    # Change of Nitrate concentration over time 
  dt = (Math.abs(0-t))
  dC4 = dt(mu2*Math.sqrt(C2)*C3-(p4*C4))
  return dC4
  
  
