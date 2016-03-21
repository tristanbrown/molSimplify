# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

########################################################
########### Defines class of custom boxes  #############
########################################################
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
import sys, os

class qBoxFolder(QDialog):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,toptxt,txt):
        super(qBoxFolder,self).__init__()
        self.setParent(window)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Question)
        self.msgBox.setWindowTitle(toptxt)
        self.msgBox.setText(txt)
        self.msgBox.addButton(QPushButton('Keep both'), QMessageBox.YesRole)
        self.msgBox.addButton(QPushButton('Replace'), QMessageBox.NoRole)
        self.msgBox.addButton(QPushButton('Skip'), QMessageBox.RejectRole)
    def getaction(self):
        ret = self.msgBox.exec_()
        if ret==1:
            return 'replace'
        elif ret==2:
            return 'skip'
        elif ret==0:
            return 'keep'
        else:
            return False
            
class qBoxInfo(QDialog):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,toptxt,txt):
        super(qBoxInfo,self).__init__()
        self.setParent(window)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle(toptxt)
        self.msgBox.setText(txt)
        self.msgBox.addButton(QPushButton('OK'), QMessageBox.YesRole)
        self.msgBox.exec_()

class qBoxError(QDialog):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,toptxt,txt):
        super(qBoxError,self).__init__()
        self.setParent(window)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Critical)
        self.msgBox.setWindowTitle(toptxt)
        self.msgBox.setText(txt)
        self.msgBox.addButton(QPushButton('OK'), QMessageBox.YesRole)
        self.msgBox.exec_()

class qBoxWarning(QDialog):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,toptxt,txt):
        super(qBoxWarning,self).__init__()
        self.setParent(window)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setWindowTitle(toptxt)
        self.msgBox.setText(txt)
        self.msgBox.addButton(QPushButton('OK'), QMessageBox.YesRole)
        self.msgBox.exec_()
