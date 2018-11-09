'''
Created on Nov 9, 2018

@author: Brandon
'''
import sys;
from PyQt5.Qt import QWidget, QApplication, QMainWindow
from PyQt5.uic import loadUi



class myWindwo(QMainWindow):
    def __init__(self):
        super().__init__();
        loadUi("Fastener_StrengthCriteria_110918.ui", self);
        
        
    

app = QApplication(sys.argv);
window = myWindwo();
window.show();
sys.exit(app.exec_());
    
