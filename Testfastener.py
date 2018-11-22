'''
Created on Nov 9, 2018

@author: Brandon
'''
from builtins import int
import sys;

from PyQt5.Qt import QWidget, QApplication, QMainWindow, QMessageBox,\
    QErrorMessage
from PyQt5.uic import loadUi
from OOPFastenerCalcs import FastenerCalcs, ShearTearOut, BoltBearing
from sympy.core.exprtools import _isnumber
import os #Used in Testing Script

#runs the code at the command prompt
#os.system("pyuic5 Fastener_StrengthCriteria_110918.ui -o Fastener_StrengthCriteria_110918.py")

import Fastener_StrengthCriteria_110918;

class myWindwo(QMainWindow, Fastener_StrengthCriteria_110918.Ui_MainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi(self);
        #Loads the interface
        #loadUi(r"C:\Users\Brandon\Documents\RAYTHEON\PYTHON\PROJECTS\GUIFastener\Fastener_StrengthCriteria_110918.ui", self);
        
        #Rename Tabs
        self.tabFastenerWidget.setTabText(0, "TensionAndShear");
        self.tabFastenerWidget.setTabText(1, "ShearTearOut");
        self.tabFastenerWidget.setTabText(2, "BoltBearing");
        self.safetyFactor.setText("1.15");
        self.safetyMargin.setReadOnly(True);
        
        #button click event
        self.calculateButton.clicked.connect(self.calculateSafetyMargin);
        self.calculateShearMargin.clicked.connect(self.calculateShearSafetyMargin);
        self.calculateBoltBearing.clicked.connect(self.calculateBearingSafetyMargin);
    #handler
    def calculateSafetyMargin(self):
        #error check to see if numbers were put in
        try:
            yieldStress = float(self.yieldStress.text());
            nominalDiameter = float(self.nominalDiameter.text());
            shearOne = float(self.shearOne.text());
            shearTwo = float(self.shearTwo.text());
            axial = float(self.axial.text());
            safetyFactor =float(self.safetyFactor.text());
        
            x = FastenerCalcs(yieldStress, nominalDiameter, shearOne, shearTwo, axial, safetyFactor);
            self.safetyMargin.setText(str(round(x.marginOfSafety(),2)));
        except Exception as e:
            self.errorDialog = QMessageBox();
            self.errorDialog.warning(self, "Warning!!", str(e));
    ###################################################################################################################
    def calculateShearSafetyMargin(self):
        try:
            shearStrength = float(self.shearStrength.text());
            nominalDiameter = float(self.nominalDiameter_2.text());
            e = float(self.e.text());
            thickness = float(self.thickness.text());
            shearOneComponent = float(self.shearOneComponent.text());
            shearTwoComponent = float(self.shearTwoComponent.text());
            safetyFactor2 = float(self.safetyFactor2.text());
            
            x= ShearTearOut(shearStrength, nominalDiameter, e, thickness, shearOneComponent, shearTwoComponent, safetyFactor2);
            
            self.shearSafetyMargin.setText(str(round(x.safetyMargin(),2)));
                
        except Exception as e:
            self.errorDialog = QMessageBox();
            self.errorDialog.warning(self, "Warning!!", str(e));
    
    #################################################################################################################
    def calculateBearingSafetyMargin(self):
        
        try:
            bearingUpper = float(self.bearingUpper.text());
            bearingLower = float(self.bearingLower.text());
            nominalDiameter = float(self.nominalDiameter3.text());
            e = float(self.e_2.text());
            thickness = float(self.thickness2.text());
            shearOne = float(self.shearOne2.text());
            shearTwo = float(self.shearTwo2.text());
            safetyFactor = float(self.safetyFactor3.text());
            
            x = BoltBearing(bearingUpper, bearingLower, nominalDiameter, e, thickness, shearOne, shearTwo, safetyFactor);
            
            self.bearingSafetyMargin.setText(str(round(x.safetyMargin(),2)));
        
        except Exception as e:
            self.errorDialog = QMessageBox();
            self.errorDialog.warning(self, "Warning!!", str(e));

def main():        
    app = QApplication(sys.argv);
    window = myWindwo();
    window.show();
    sys.exit(app.exec_());
    
if __name__ == '__main__':
    main();
