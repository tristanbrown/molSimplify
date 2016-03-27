# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##################################################
########### Defines class of window  #############
##################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import struct
import sys
import imghdr
import os

class mMenubar(QMainWindow):
    # margins and scale are fractional 
    def __init__(self,window,gui):
        super(mMenubar,self).__init__()
        self = window.menuBar()
        self.setParent(window)
        self.filemenup = self.addMenu('')
        self.filemenu0 = self.addMenu('&File')
        self.filemenu1 = self.addMenu('&Load')
        self.filemenu2 = self.addMenu('&Help')
        exitAction = QAction('&Exit',window)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(window.qexitM)
        self.filemenu0.addAction(exitAction)
        saveAction = QAction('&Save As..',window)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current input settings')
        saveAction.triggered.connect(gui.qdumpS)
        self.filemenu0.addAction(saveAction)
        loadAction = QAction('&Load',window)
        loadAction.setShortcut('Ctrl+O')
        loadAction.setStatusTip('Load input file')
        loadAction.triggered.connect(gui.qloadM)
        self.filemenu1.addAction(loadAction)
        helpAction = QAction('&Help',window)
        helpAction.setShortcut('Ctrl+H')
        helpAction.setStatusTip('Show input options')
        helpAction.triggered.connect(gui.qhelpM)
