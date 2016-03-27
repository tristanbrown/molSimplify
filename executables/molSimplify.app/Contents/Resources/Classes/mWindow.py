# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##################################################
########### Defines class of window  #############
##################################################
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from mText import *
from Classes.globalvars import *
import sys

def getscreensize():
    screenShape = QDesktopWidget().screenGeometry()
    return [screenShape.width(),screenShape.height()]

class mWindow(QMainWindow):
    ### constructor of window ###
    def __init__(self,w=0.5,h=0.5):
        super(mWindow,self).__init__()
        globs = globalvars()
        self.resize(w,h)
        self.setWindowTitle(globs.PROGRAM)
        self.setWindowIcon(QIcon(globs.installdir+'/icons/pythonlogo.png'))
        ### change background color
        p = QPalette()
        p.setColor(QPalette.Background,QtCore.Qt.white)
        self.setPalette(p)
    ### get geometry of window ###
    def getGeometry(self):
        geom = self.frameGeometry()
        return [geom.x(),geom.y(),geom.width(),geom.height()]
    ### maximize window in current screen ###
    def maximize():
        self.showMaximized()
    ### resize window in either fractional or absolute size ###
    def resize(self,w,h):
        [scW,scH] = getscreensize() # get screen size
        # check for fractional coords
        if (w <= 1.0):
            marginW = 0.5*(1.0-w)*scW # margin in pixels
            w = w*scW # width in pixels
        else:
            marginW = 0.5*(scW-w)
        if (h <= 1.0):
            marginH = 0.5*(1.0-h)*scH # margin in pixels
            h = h*scH # height in pixels
        else:
            marginH = 0.5*(scH-h)
        self.setGeometry(marginW,marginH,w,h)
    ### define action for exiting, pop-up dialog
    def qexitM(self):
        choice = QMessageBox.question(self,'Exit','Are you sure you want to quit?',
                QMessageBox.Yes, QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
class mWgen(QMainWindow):
    ### constructor of window ###
    def __init__(self,w=0.5,h=0.5,txt=''):
        super(mWgen,self).__init__()
        globs = globalvars()
        self.resize(w,h)
        self.setWindowTitle(txt)
        self.setWindowIcon(QIcon(globs.installdir+'/icons/pythonlogo.png'))
        ### change background color
        p = QPalette()
        p.setColor(QPalette.Background,QtCore.Qt.white)
        self.setPalette(p)
    ### resize window in either fractional or absolute size ###
    def resize(self,w,h):
        [scW,scH] = getscreensize() # get screen size
        # check for fractional coords
        if (w <= 1.0):
            marginW = 0.5*(1.0-w)*scW # margin in pixels
            w = w*scW # width in pixels
        else:
            marginW = 0.5*(scW-w)
        if (h <= 1.0):
            marginH = 0.5*(1.0-h)*scH # margin in pixels
            h = h*scH # height in pixels
        else:
            marginH = 0.5*(scH-h)
        self.setGeometry(marginW,marginH,w,h)
    ### get geometry of window ###
    def getGeometry(self):
        geom = self.frameGeometry()
        return [geom.x(),geom.y(),geom.width(),geom.height()]
    ### define action for exiting, pop-up dialog
    def qexitM(self):
        self.hide()
    
