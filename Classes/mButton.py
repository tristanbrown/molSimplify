# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##################################################
########### Defines class of window  #############
##################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class mButton(QPushButton):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,ctip,fontsize):
        super(mButton,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setText(txt)
        self.setToolTip(ctip)
        self.setGeometry(marginW,marginH,tW,tH)
        f = QFont("Helvetica",fontsize)
        self.setFont(f)
        self.setMouseTracking(True)
        self.show()
    def settxtfont(self,f):
        self.setFont(f)
    def enterEvent(self,event):
        self.setStyleSheet("background-color:#F3BEAC;")
    def leaveEvent(self,event):
        self.setStyleSheet("background-color:;")

class mCheck(QCheckBox):
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,ctip,fontsize):
        super(mCheck,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        self.state = False
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setText(txt)
        self.setGeometry(marginW,marginH,tW,tH)
        f = QFont("Helvetica",fontsize)
        self.stateChanged.connect(self.changestate)
        self.setFont(f)
        self.setToolTip(ctip)
        self.show()
    def changestate(self):
        if self.isChecked():
            self.state = False
        else:
            self.state = True
    def getState(self):
        if self.isChecked():
            return 1
        else:
            return 0

class mDbox(QComboBox):
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,ctip,fontsize):
        super(mDbox,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        self.state = 0
        for t in txt:
            self.addItem(t)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setGeometry(marginW,marginH,tW,tH)
        f = QFont("Helvetica",fontsize)
        self.setToolTip(ctip)
        self.setFont(f)
    def getState(self):
        return self.currentIndex()
    def getText(self):
        return self.currentText()

class mSlider(QSlider):
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,ctip):
        super(mSlider,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        self.setOrientation(Qt.Horizontal)
        self.setRange(0,100)
        self.setValue(0)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setGeometry(marginW,marginH,tW,tH)
