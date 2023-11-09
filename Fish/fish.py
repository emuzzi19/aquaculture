#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: fish.py
#                                                                      Authors: 
#                                                                      Description: 'Fish' object, used to implement fish objects to interact with the system  
#
#
#
#=====================================================================================================================================================================================================================

class Fish:
     def __init__(self, EatChance, PoopChance, DeathChance,ServingSize,PoopAmount,Living):
        self.EatChance = EatChance
        self.PoopChance = PoopChance
        self.DeathChance = DeathChance
        self.ServingSize = ServingSize
        self.PoopAmount = PoopAmount
        self.Living = Living
        
     
        
    
        
