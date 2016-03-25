# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##################################################
########### Defines class of window  #############
##################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Classes.globalvars import *
import os, imghdr, struct

##################################################
########### Defines class of window  #############
##################################################

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


class mRtext(QLabel):
    # constructor needs window, marginW, marginH and Font size
    # margins and scale are fractional 
    def __init__(self,window,mW,mH,tW,tH,txt,ctip,fontsize,fontype,align):
        super(mRtext,self).__init__()
        wgeom = window.getGeometry()
        self.setParent(window)
        # define margins
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        tW = tW*wgeom[2]
        tH = tH*wgeom[3]
        self.setText(txt) # set text
        # alignment
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


def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height


class mPic(QLabel):
    # constructor needs window, picture path, marginW, marginH and scale
    # margins and scale are fractional 
    def __init__(self,window,picpath,mW,mH,sc):
        super(mPic,self).__init__()
        self = QLabel(window)
        # get picture size
        [pw,ph] = get_image_size(picpath)
        wgeom = window.getGeometry()
        # rescale image        
        initR = float(ph)/float(pw)
        pw = wgeom[2]*sc
        ph = int(initR*pw)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        pixmap = QPixmap(picpath)
        pixmap = pixmap.scaledToHeight(ph)
        self.setGeometry(marginW,marginH,pw,ph)
        self.setPixmap(pixmap)
        self.show()

class mPic2(QLabel):
    # constructor needs window, picture path, marginW, marginH and scale
    # margins and scale are fractional 
    def __init__(self,window,picpath,mW,mH,W,H):
        super(mPic2,self).__init__()
        self = QLabel(window)
        # get picture size
        [pw,ph] = get_image_size(picpath)
        wgeom = window.getGeometry()
        # rescale image        
        initR = float(ph)/float(pw)
        wgR = float(wgeom[3])/float(wgeom[2])
        if wgR < initR : 
            rsc = float(wgeom[3])/float(ph)
        else:
            rsc = float(wgeom[2])/float(pw)
        [pw,ph] = [rsc*pw,rsc*ph]
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        pixmap = QPixmap(picpath)
        pixmap = pixmap.scaled(pw,ph)
        self.setGeometry(marginW,marginH,pw,ph)
        self.setPixmap(pixmap)
        self.show()
        

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

