'''
Created on Nov 9, 2018

@author: Brandon
'''
from builtins import int
import sys;

from PyQt5.Qt import QWidget, QApplication, QMainWindow, QMessageBox,\
    QErrorMessage
from PyQt5.uic import loadUi
from OOPFastenerCalcs import FastenerCalcs
from sympy.core.exprtools import _isnumber


class myWindwo(QMainWindow):
    def __init__(self):
        super().__init__();
        #Loads the interface
        loadUi("Fastener_StrengthCriteria_110918.ui", self);
        
        #Rename Tabs
        self.tabFastenerWidget.setTabText(0, "TensionAndShear");
        self.tabFastenerWidget.setTabText(1, "ShearTearOut");
        self.tabFastenerWidget.setTabText(2, "BoltBearing");
        self.safetyFactor.setText("1.15");
        self.safetyMargin.setReadOnly(True);
        
        #button click event
        self.calculateButton.clicked.connect(self.calculateSafetyMargin);
        
    #handler
    def calculateSafetyMargin(self):
        
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
    

app = QApplication(sys.argv);
window = myWindwo();
window.show();
sys.exit(app.exec_());
    
