'''
Created on Nov 9, 2018

@author: Brandon
'''
from builtins import int
import sys;

from PyQt5.Qt import QWidget, QApplication, QMainWindow
from PyQt5.uic import loadUi
from OOPFastenerCalcs import FastenerCalcs


class myWindwo(QMainWindow):
    def __init__(self):
        super().__init__();
        loadUi("Fastener_StrengthCriteria_110918.ui", self);
        
        self.calculateButton.clicked.connect(self.calculateSafetyMargin);
    
    def calculateSafetyMargin(self):
        yieldStress = float(self.yieldStress.text());
        nominalDiameter = float(self.nominalDiameter.text());
        shearOne = float(self.shearOne.text());
        shearTwo = float(self.shearTwo.text());
        axial = float(self.axial.text());
   
        x = FastenerCalcs(yieldStress, nominalDiameter, shearOne, shearTwo, axial);
        self.safetyMargin.setText(str(round(x.marginOfSafety(),2))); 
    

app = QApplication(sys.argv);
window = myWindwo();
window.show();
sys.exit(app.exec_());
    
