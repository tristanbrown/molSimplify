# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##################################################
########### Defines class of window  #############
##################################################
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os

class mRtext(QLabel):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,ctip,fontsize,fontype,align):
        super(mRtext,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setText(txt)
        if align in 'Ll':
            self.setAlignment(Qt.AlignLeft)
        elif align in 'Rr':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignCenter)
        self.setGeometry(marginW,marginH,tW,tH)
        if fontype[0] in 'Bb':
            f = QFont("Helvetica",fontsize,QFont.Bold)
        elif fontype[0] in 'Ii':
            f = QFont("Helvetica",fontsize,QFont.Italic)
        else:
            f = QFont("Helvetica",fontsize)
        self.setFont(f)
        self.setToolTip(ctip)
        self.show()
    def settxtfont(self,f):
        self.setFont(f)

class mEtext(QLineEdit):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,ctip,fontsize,fontype,align):
        super(mEtext,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setText(txt)
        self.setGeometry(marginW,marginH,tW,tH)
        if align in 'Ll':
            self.setAlignment(Qt.AlignLeft)
        elif align in 'Rr':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignCenter)
        self.setGeometry(marginW,marginH,tW,tH)
        if fontype[0] in 'Bb':
            f = QFont("Helvetica",fontsize,QFont.Bold)
        elif fontype[0] in 'Ii':
            f = QFont("Helvetica",fontsize,QFont.Italic)
        else:
            f = QFont("Helvetica",fontsize)
        self.setFont(f)
        self.setToolTip(ctip)
        self.show()
    def settxtfont(self,f):
        self.setFont(f)
        
class mEdtext(QTextEdit):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,fontsize,fontype,align):
        super(mEdtext,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setText(txt)
        self.setGeometry(marginW,marginH,tW,tH)
        if align in 'Ll':
            self.setAlignment(Qt.AlignLeft)
        elif align in 'Rr':
            self.setAlignment(Qt.AlignRight)
        else:
            self.setAlignment(Qt.AlignCenter)
        self.setGeometry(marginW,marginH,tW,tH)
        if fontype[0] in 'Bb':
            f = QFont("Helvetica",fontsize,QFont.Bold)
        elif fontype[0] in 'Ii':
            f = QFont("Helvetica",fontsize,QFont.Italic)
        else:
            f = QFont("Helvetica",fontsize)
        self.setFont(f)
        self.show()
    def settxtfont(self,f):
        self.setFont(f)


