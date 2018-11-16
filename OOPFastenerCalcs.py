'''
Created on Nov 3, 2018

@author: Brandon
'''
import math;
import numpy as np;

class FastenerCalcs:
    '''Constructor//////////////////////////////////////////////////////////////////////////////'''
    def __init__(self, yieldStress,minimumDiameter,
                 shearOneComponent, shearTwoComponent,
                 axialComponent, safetyFactor = 1.15, 
                 shearYield = None, preload = None):
        
        self.yieldStress = yieldStress;
        self.minimumDiameter = minimumDiameter;
        self.shearOneComponent = shearOneComponent;
        self.shearTwoComponent = shearTwoComponent;
        self.axialComponent = axialComponent;
        self.safetyFactor = safetyFactor;
        
        'Checks to see if preloads and shear yield stress is specified'
        if shearYield is None:
            self.shearYield = 0.577*self.yieldStress;
        else:
            self.shearYield = shearYield;
        
        if preload is None:
            self.preload = 0.65*self.yieldStress*(math.pi/4)*self.minimumDiameter;
        else:
            self.preload = preload;
    
    "Methods////////////////////////////////////////////////////////////////////////////////////"        
    
    def getShearYield(self):
        return self.shearYield;
        
    def Area(self):
        return (math.pi/4)*self.minimumDiameter
    
    def getPreload(self):
        return self.preload;
    
    def totalShear(self):
        return math.sqrt(self.shearOneComponent**2 + self.shearTwoComponent**2)
    
    def axialStress(self):
        return self.preload + self.safetyFactor*self.shearYield;
    
    def shearLoadRatio(self):
        return self.safetyFactor*(self.totalShear()/self.Area())/self.shearYield
    
    def axialLoadRatio(self):
        return (self.axialStress()/self.Area())/self.yieldStress;
    
    def marginOfSafety(self):
        return (1/(math.sqrt(self.axialLoadRatio()**2 + self.shearLoadRatio()**3)))-1;

"//////////////////////////////////////////////////////////////////////////////////////" 
class BoltBearing():
    def __init__(self, bearingStrengthUpper, bearingStrengthLower, 
                 nominalDiameter, e, thickness, shearOneComponent, shearTwoComponent, 
                 safetyFactor = 1.15 ):
        
        self.bearingStrengthUpper = bearingStrengthUpper;
        self.bearingStrenghtLower = bearingStrengthLower;
        self.nominalDiameter = nominalDiameter;
        self.e = e;
        self.thickness = thickness;
        self.shearOneComponent = shearOneComponent;
        self.shearTwoComponent = shearTwoComponent;
        self.safetyFactor = safetyFactor;
        
    
    def bearingStrengthinterpolation(self):
        eOverD = self.e/self.nominalDiameter;
        return np.interp(eOverD, [1.5,2], [self.bearingStrenghtLower, self.bearingStrengthUpper])
    
    def bearingArea(self):
        return self.nominalDiameter*self.thickness;
    
    def totalShear(self):
        return math.sqrt(self.shearOneComponent**2 + self.shearTwoComponent**2)
    
    def safetyMargin(self):
        return (self.bearingStrengthinterpolation()/(self.safetyFactor*(self.totalShear()/self.bearingArea()))) - 1;

"///////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
class ShearTearOut:
    
    def __init__(self, shearStrength, nominalDiameter, e, thickness, 
                 shearOneComponent, shearTwoComponent, safetyFactor = 1.15  ):
        
        self.shearStrength = shearStrength;
        self.nominalDiameter = nominalDiameter;
        self.e = e;
        self.thickness = thickness;
        self. shearOneComponent = shearOneComponent;
        self.shearTwoComponent = shearTwoComponent;
        self.safetyFactor = safetyFactor;
        
    def shearArea(self):
        return 2*self.thickness*(self.e - (self.nominalDiameter/2));
    
    def totalShear(self):
        return math.sqrt(self.shearOneComponent**2 + self.shearTwoComponent**2)
        
    def safetyMargin(self): 
        return (self.shearStrength/(self.safetyFactor*(self.totalShear()/self.shearArea())))-1
    



    

