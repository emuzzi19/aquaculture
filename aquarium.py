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
Xmax = (24*Math.pi)
Ymin = -(6*Math.pi)
Ymax = (5* Math.pi)
Zmin = (2* Math.pi)
Zmax = (5* Math.pow(10,-6))
Wishbone1 = (2 * Math.pow(10,-8))
Wishbone2 = (3 * Math.pow(10,-6))
V = 3628800


# Chemical Consentrations

C1 = 0 # NH4 (Ammonia)
C2 = 0 # O2 (Oxygen)
C3 = 0 # NO2 (NitrITE)
C4 = 0 # NO3 (NitrATE)
