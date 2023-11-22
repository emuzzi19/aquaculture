#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: fish.py
#                                                                      Authors: 
#                                                                      Description: 'Fish' object, used to implement fish objects to interact with the system  
#
#
#
#=====================================================================================================================================================================================================================

import random 

class fish:

    def __init__(self, name, eatPercent, poopPercent,peePercent, deathPercent, servingSize, weight):
        self.name = name
        self.eatPercent = eatPercent
        self.poopPercent = poopPercent
        self.peePercent = peePercent
        self.deathPercent = deathPercent
        self.servingSize = servingSize
        self.weight = weight
        self.living = True
        self.status = 'Nothing'
    
    #these still need work, specifically in calculating the chemical changes
    
    def Eat(self):
        self.status = 'Eating'
        result = (self.weight*self.servingSize)
        return result
        
    def Poop(self):
        self.status = 'Pooping'
        result = (self.weight/3)
        return result
        
    def Pee(self,t):
        self.status = 'Peeing'
        hours = t/3600
        result = (pow((0.0014*self.weight),2)-0.4384*self.weight+43.303)
        result = result*hours
        return result
    

    #def Grow(self,t):
        #days = t/86400
       # while self.weight <= 450:
            #self.weight = pow((0.4244*days),2)+(83.729*days) 
            


    def action(self,t):
        fishActionProb = random.random()
        if fishActionProb >= 0.0 and fishActionProb <= self.eatPercent:      #fish eats if the random number is in this range 
            result = self.Eat() 
        if fishActionProb > self.eatPercent and fishActionProb <= self.poopPercent: #fish poops if the random number is in this range   
            result = self.Poop()
        if fishActionProb > self.poopPercent and fishActionProb <= self.peePercent: #fish pees if the random number is in this range
            result = self.Pee(t) 
        else:                                                          #if none of these if statements are fulfilled, the fish is doing no actions
            result = 0
            self.status = "Nothing"
        return result,self.status
            
       


   