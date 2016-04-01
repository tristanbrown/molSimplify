# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

####################################################
########### Defines main class of GUI  #############
####################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *
from Classes.mWidgets import *
from Classes.mGUI import *
from Classes.globalvars import *
from Classes.mol3D import mol3D
from Scripts.generator import startgen
from Scripts.grabguivars import *
from Scripts.io import *
from Scripts.addtodb import *
import sys, os, random, shutil, unicodedata, inspect, glob, time
from imolecule import *
import pybel


class mGUI():
    getgeoms()
    ### constructor of gui ###
    def __init__(self,app):
        # build gui
        self.app = app
        self.initGUIref(app)

    ### builds the gui
    def initGUIref(self,app):
        '''
        ######################
        ### build main GUI ###
        ######################
        '''
        ### check for configuration file ###
        homedir = os.path.expanduser("~")
        globs = globalvars() # global variables
        overX = True if 'localhost' in os.environ['DISPLAY'].lower() else False # detect running over X
        configfile = False if not glob.glob(homedir+'/.molSimplify') else True
        if not configfile:
            self.wwindow = QMainWindow() 
            self.wwindow.resize(0.5,0.5)
            QMessageBox.information(self.wwindow,'Setup',"It looks like the configuration file '~/.molSimplify' does not exist!Please follow the next steps to configure the file.")
            QMessageBox.information(self.wwindow,'Installation directory',"Please select the top installation directory for the program.")
            f = open(homedir+'/.molSimplify','w')
            if len(instdir) > 1: 
                f.write("INSTALLDIR="+instdir+'\n')
        ### end set-up configuration file ###
        ### main window widget
        self.wmain = QWidget()
        self.wmain.setWindowTitle("molSimplify")
        self.wmain.setMinimumSize(1000,700)
        # for some reason it forces the widgets to reset and the window to come up properly
        #mQMessageBox('','','info',True)
        # set background color
        p = QPalette()
        p.setColor(QPalette.Background,QtCore.Qt.white)
        self.wmain.setPalette(p)
        ### main grid layout ###
        self.grid = QGridLayout()
        ### stacked layouts ###
        self.sgrid = QStackedLayout()
        self.sgrid.setStackingMode(1)
        self.sgrid.addWidget(self.wmain)
        ### create menubar and callbacks ###
        menubar = QMenuBar()
        menu0 = menubar.addMenu('&File')
        menu1 = menubar.addMenu('&Load')
        menu2 = menubar.addMenu('&Help')
        exitAction = QAction('&Exit',self.wmain) 
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.qexit)
        menu0.addAction(exitAction)
        saveAction = QAction('&Save As..',self.wmain)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current input settings')
        saveAction.triggered.connect(self.qsaveinput)
        menu0.addAction(saveAction)
        loadAction = QAction('&Load',self.wmain)
        loadAction.setShortcut('Ctrl+O')
        loadAction.setStatusTip('Load input file')
        loadAction.triggered.connect(self.qloadinput)
        menu1.addAction(loadAction)
        helpAction = QAction('&Help',self.wmain)
        helpAction.setShortcut('Ctrl+H')
        helpAction.setStatusTip('Show input options')
        helpAction.triggered.connect(self.qshowhelp)
        menu2.addAction(helpAction)
        # set menubar
        self.menubar = menubar
        self.grid.setMenuBar(self.menubar)
        ### place title top ###
        self.grid.setRowMinimumHeight(0,15)
        self.grid.setRowMinimumHeight(3,15)
        self.grid.setRowMinimumHeight(4,50)
        clogo = mQPixmap(globs.installdir+'/icons/logo.png')
        self.grid.addWidget(clogo,1,10,2,18)
        self.txtdev = mQLabel('Developed by Kulik group @ MIT','','c',16)
        self.grid.addWidget(self.txtdev,19,10,2,18)
        ###################################################
        ###################################################
        ########## STRUCTURE GENERATION INPUTS ############
        ###################################################
        ###################################################
        ### title ###
        self.txtgpar = mQLabel('Structure specification','','c',20)
        self.grid.addWidget(self.txtgpar,4,0,2,14)
        ### core structure specification ###
        ctip = 'Core of structure'
        self.rtcore = mQLabel('Core:',ctip,'C',14)
        f = QFont("Helvetica",14,75)
        self.rtcore.setFont(f)
        self.grid.addWidget(self.rtcore,7,2,1,1)
        self.etcore = mQLineEdit('',ctip,'l',14)
        self.grid.addWidget(self.etcore,7,3,1,3)
        ### Connection atoms for core ###
        ctip = 'Specify connection atoms for core if using SMILES or custom cores (default: 1)'
        self.rtccat = mQLabel('Core connections:',ctip,'C',11)
        self.rtccat.setWordWrap(True)
        self.grid.addWidget(self.rtccat,7,6,1,2)
        self.etccat = mQLineEdit('',ctip,'l',14)
        self.grid.addWidget(self.etccat,7,8,1,2)
        ### replace option ###
        ctip = 'Replace ligand at specified connection point'
        self.replig = mQCheckBox('replace',ctip,16)
        self.grid.addWidget(self.replig,7,10,1,4)
        # coordination
        ctip = 'Number of ligands connected to the metal.'
        self.rcoord = mQLabel('Coordination:',ctip,'Cr',12)
        self.grid.addWidget(self.rcoord,8,2,1,2)
        qcav = ['1','2','3','4','5','6','7']
        self.dcoord = mQComboBox(qcav,ctip,12)
        self.dcoord.setCurrentIndex(5)
        self.dcoord.currentIndexChanged.connect(self.matchgeomcoord)
        self.grid.addWidget(self.dcoord,8,4,1,1)
        # geometry of coordination
        self.dcoordg = mQComboBox('','',12)
        self.dcoordg.setCurrentIndex(0)
        self.matchgeomcoord()
        self.grid.addWidget(self.dcoordg,8,5,1,2)
        # add new coordination
        ctip = 'Add geometry'
        self.butaddg = mQPushButton('Add geometry',ctip,12)
        self.butaddg.clicked.connect(self.addgeom)
        self.grid.addWidget(self.butaddg,8,7,1,3)
        #############################################
        ################## LIGANDS ##################
        ### ligands tables ###
        ctip0 = 'Ligand(s) to be used' 
        self.rtligh = mQLabel('Ligands',ctip0,'c',12) # ligand header
        f = QFont("Helvetica",12,75)
        self.rtligh.setFont(f)
        ctip1 = 'Occurrence of corresponding ligand(s)'
        self.rtligocch = mQLabel('Frequency',ctip1,'c',12) # occurrence header
        ctip2 = 'Connection atom(s) of ligands (default: 1).'
        self.rtsmicath = mQLabel('Connections',ctip2,'c',12) # connection atom header
        ctip3 = 'Do not remove hydrogens while connecting ligand to core. default False' # keep Hs header
        self.keepHh = mQLabel('keep\nHs',ctip3,'c',10) # occurrence header
        ctip4 = 'Custom bond length for M-L in Angstrom' 
        self.MLbondsh = mQLabel('M-L bond',ctip4,'c',11)# custom metal ligand bond length header
        ctip5 = 'Custom angles for connection points (polar theta, azimuthal phi) in degrees separated with /. e.g 10/20'
        self.canglesh = mQLabel('Angle',ctip5,'c',12) # custom angles for distortion header
        ctip6 = 'Name of ligand'
        self.nameligh = mQLabel('Name',ctip6,'c',12) # name of ligand header
        ctip7 = 'Force ligand order and disable smart reordering'
        self.ligforder = mQCheckBox('Force\norder',ctip7,11) 
        # add to layout
        self.grid.addWidget(self.rtligh,9,0,1,2)
        self.grid.addWidget(self.rtligocch,9,2,1,2)
        self.grid.addWidget(self.rtsmicath,9,4,1,2)
        self.grid.addWidget(self.keepHh,9,6,1,1)
        self.grid.addWidget(self.MLbondsh,9,7,1,2)
        self.grid.addWidget(self.canglesh,9,9,1,2)
        self.grid.addWidget(self.nameligh,9,11,1,2)
        self.grid.addWidget(self.ligforder,9,13,1,1)
        ## ligands ##
        self.lig0 = mQLineEdit('',ctip0,'l',12)
        self.lig1 = mQLineEdit('',ctip0,'l',12)
        self.lig2 = mQLineEdit('',ctip0,'l',12)
        self.lig3 = mQLineEdit('',ctip0,'l',12)
        self.lig4 = mQLineEdit('',ctip0,'l',12)
        self.lig5 = mQLineEdit('',ctip0,'l',12)
        self.lig6 = mQLineEdit('',ctip0,'l',12)
        self.lig7 = mQLineEdit('',ctip0,'l',12)
        # disable
        self.lig1.setDisabled(True)
        self.lig2.setDisabled(True)
        self.lig3.setDisabled(True)
        self.lig4.setDisabled(True)
        self.lig5.setDisabled(True)
        self.lig6.setDisabled(True)
        self.lig7.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0,10,0,1,2)
        self.grid.addWidget(self.lig1,11,0,1,2)
        self.grid.addWidget(self.lig2,12,0,1,2)
        self.grid.addWidget(self.lig3,13,0,1,2)
        self.grid.addWidget(self.lig4,14,0,1,2)
        self.grid.addWidget(self.lig5,15,0,1,2)
        self.grid.addWidget(self.lig6,16,0,1,2)
        self.grid.addWidget(self.lig7,17,0,1,2)
        ## occurrences ##
        self.lig0occ = mQSpinBox(ctip1)
        self.lig1occ = mQSpinBox(ctip1)
        self.lig2occ = mQSpinBox(ctip1)
        self.lig3occ = mQSpinBox(ctip1)
        self.lig4occ = mQSpinBox(ctip1)
        self.lig5occ = mQSpinBox(ctip1)
        self.lig6occ = mQSpinBox(ctip1)
        self.lig7occ = mQSpinBox(ctip1)
        # disable
        self.lig1occ.setDisabled(True)
        self.lig2occ.setDisabled(True)
        self.lig3occ.setDisabled(True)
        self.lig4occ.setDisabled(True)
        self.lig5occ.setDisabled(True)
        self.lig6occ.setDisabled(True)
        self.lig7occ.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0occ,10,2,1,2)
        self.grid.addWidget(self.lig1occ,11,2,1,2)
        self.grid.addWidget(self.lig2occ,12,2,1,2)
        self.grid.addWidget(self.lig3occ,13,2,1,2)
        self.grid.addWidget(self.lig4occ,14,2,1,2)
        self.grid.addWidget(self.lig5occ,15,2,1,2)
        self.grid.addWidget(self.lig6occ,16,2,1,2)
        self.grid.addWidget(self.lig7occ,17,2,1,2)
        ## connections ##
        self.lig0conn = mQLineEdit('',ctip2,'l',12)
        self.lig1conn = mQLineEdit('',ctip2,'l',12)
        self.lig2conn = mQLineEdit('',ctip2,'l',12)
        self.lig3conn = mQLineEdit('',ctip2,'l',12)
        self.lig4conn = mQLineEdit('',ctip2,'l',12)
        self.lig5conn = mQLineEdit('',ctip2,'l',12)
        self.lig6conn = mQLineEdit('',ctip2,'l',12)
        self.lig7conn = mQLineEdit('',ctip2,'l',12)
        # disable
        self.lig1conn.setDisabled(True)
        self.lig2conn.setDisabled(True)
        self.lig3conn.setDisabled(True)
        self.lig4conn.setDisabled(True)
        self.lig5conn.setDisabled(True)
        self.lig6conn.setDisabled(True)
        self.lig7conn.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0conn,10,4,1,2)
        self.grid.addWidget(self.lig1conn,11,4,1,2)
        self.grid.addWidget(self.lig2conn,12,4,1,2)
        self.grid.addWidget(self.lig3conn,13,4,1,2)
        self.grid.addWidget(self.lig4conn,14,4,1,2)
        self.grid.addWidget(self.lig5conn,15,4,1,2)
        self.grid.addWidget(self.lig6conn,16,4,1,2)
        self.grid.addWidget(self.lig7conn,17,4,1,2)
        ## keep Hydrogens #
        self.lig0H = mQComboBox(['no','yes'],ctip3,12)
        self.lig1H = mQComboBox(['no','yes'],ctip3,12)
        self.lig2H = mQComboBox(['no','yes'],ctip3,12)
        self.lig3H = mQComboBox(['no','yes'],ctip3,12)
        self.lig4H = mQComboBox(['no','yes'],ctip3,12)
        self.lig5H = mQComboBox(['no','yes'],ctip3,12)
        self.lig6H = mQComboBox(['no','yes'],ctip3,12)
        self.lig7H = mQComboBox(['no','yes'],ctip3,12)
        # disable
        self.lig1H.setDisabled(True)
        self.lig2H.setDisabled(True)
        self.lig3H.setDisabled(True)
        self.lig4H.setDisabled(True)
        self.lig5H.setDisabled(True)
        self.lig6H.setDisabled(True)
        self.lig7H.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0H,10,6,1,1)
        self.grid.addWidget(self.lig1H,11,6,1,1)
        self.grid.addWidget(self.lig2H,12,6,1,1)
        self.grid.addWidget(self.lig3H,13,6,1,1)
        self.grid.addWidget(self.lig4H,14,6,1,1)
        self.grid.addWidget(self.lig5H,15,6,1,1)
        self.grid.addWidget(self.lig6H,16,6,1,1)
        self.grid.addWidget(self.lig7H,17,6,1,1)
        ## ML bonds ##
        self.lig0ML = mQLineEdit('',ctip4,'l',12)
        self.lig1ML = mQLineEdit('',ctip4,'l',12)
        self.lig2ML = mQLineEdit('',ctip4,'l',12)
        self.lig3ML = mQLineEdit('',ctip4,'l',12)
        self.lig4ML = mQLineEdit('',ctip4,'l',12)
        self.lig5ML = mQLineEdit('',ctip4,'l',12)
        self.lig6ML = mQLineEdit('',ctip4,'l',12)
        self.lig7ML = mQLineEdit('',ctip4,'l',12)
        # disable
        self.lig1ML.setDisabled(True)
        self.lig2ML.setDisabled(True)
        self.lig3ML.setDisabled(True)
        self.lig4ML.setDisabled(True)
        self.lig5ML.setDisabled(True)
        self.lig6ML.setDisabled(True)
        self.lig7ML.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0ML,10,7,1,2)
        self.grid.addWidget(self.lig1ML,11,7,1,2)
        self.grid.addWidget(self.lig2ML,12,7,1,2)
        self.grid.addWidget(self.lig3ML,13,7,1,2)
        self.grid.addWidget(self.lig4ML,14,7,1,2)
        self.grid.addWidget(self.lig5ML,15,7,1,2)
        self.grid.addWidget(self.lig6ML,16,7,1,2)
        self.grid.addWidget(self.lig7ML,17,7,1,2)
        ## custom angles ##
        self.lig0an = mQLineEdit('',ctip5,'l',12)
        self.lig1an = mQLineEdit('',ctip5,'l',12)
        self.lig2an = mQLineEdit('',ctip5,'l',12)
        self.lig3an = mQLineEdit('',ctip5,'l',12)
        self.lig4an = mQLineEdit('',ctip5,'l',12)
        self.lig5an = mQLineEdit('',ctip5,'l',12)
        self.lig6an = mQLineEdit('',ctip5,'l',12)
        self.lig7an = mQLineEdit('',ctip5,'l',12)
        # disable
        self.lig1an.setDisabled(True)
        self.lig2an.setDisabled(True)
        self.lig3an.setDisabled(True)
        self.lig4an.setDisabled(True)
        self.lig5an.setDisabled(True)
        self.lig6an.setDisabled(True)
        self.lig7an.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0an,10,9,1,2)
        self.grid.addWidget(self.lig1an,11,9,1,2)
        self.grid.addWidget(self.lig2an,12,9,1,2)
        self.grid.addWidget(self.lig3an,13,9,1,2)
        self.grid.addWidget(self.lig4an,14,9,1,2)
        self.grid.addWidget(self.lig5an,15,9,1,2)
        self.grid.addWidget(self.lig6an,16,9,1,2)
        self.grid.addWidget(self.lig7an,17,9,1,2)
        ## ligand names ##
        self.lig0nam = mQLineEdit('',ctip6,'l',12)
        self.lig1nam = mQLineEdit('',ctip6,'l',12)
        self.lig2nam = mQLineEdit('',ctip6,'l',12)
        self.lig3nam = mQLineEdit('',ctip6,'l',12)
        self.lig4nam = mQLineEdit('',ctip6,'l',12)
        self.lig5nam = mQLineEdit('',ctip6,'l',12)
        self.lig6nam = mQLineEdit('',ctip6,'l',12)
        self.lig7nam = mQLineEdit('',ctip6,'l',12)
        # disable
        self.lig1nam.setDisabled(True)
        self.lig2nam.setDisabled(True)
        self.lig3nam.setDisabled(True)
        self.lig4nam.setDisabled(True)
        self.lig5nam.setDisabled(True)
        self.lig6nam.setDisabled(True)
        self.lig7nam.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0nam,10,11,1,1)
        self.grid.addWidget(self.lig1nam,11,11,1,1)
        self.grid.addWidget(self.lig2nam,12,11,1,1)
        self.grid.addWidget(self.lig3nam,13,11,1,1)
        self.grid.addWidget(self.lig4nam,14,11,1,1)
        self.grid.addWidget(self.lig5nam,15,11,1,1)
        self.grid.addWidget(self.lig6nam,16,11,1,1)
        self.grid.addWidget(self.lig7nam,17,11,1,1)
        ## add buttons ##
        ctip = 'Add new ligand.'
        self.lig0add = mQPushButton('+',ctip,12)
        self.lig1add = mQPushButton('+',ctip,12)
        self.lig2add = mQPushButton('+',ctip,12)
        self.lig3add = mQPushButton('+',ctip,12)
        self.lig4add = mQPushButton('+',ctip,12)
        self.lig5add = mQPushButton('+',ctip,12)
        self.lig6add = mQPushButton('+',ctip,12)
        # add callbacks
        self.lig0add.clicked.connect(self.addlig0)
        self.lig1add.clicked.connect(self.addlig1)
        self.lig2add.clicked.connect(self.addlig2)
        self.lig3add.clicked.connect(self.addlig3)
        self.lig4add.clicked.connect(self.addlig4)
        self.lig5add.clicked.connect(self.addlig5)
        self.lig6add.clicked.connect(self.addlig6)
        # hide and disable
        self.lig1add.hide()
        self.lig1add.setDisabled(True)
        self.lig2add.hide()
        self.lig2add.setDisabled(True)
        self.lig3add.hide()
        self.lig3add.setDisabled(True)
        self.lig4add.hide()
        self.lig4add.setDisabled(True)
        self.lig5add.hide()
        self.lig5add.setDisabled(True)
        self.lig6add.hide()
        self.lig6add.setDisabled(True)
        # add to layout
        self.grid.addWidget(self.lig0add,10,13,1,1)
        self.grid.addWidget(self.lig1add,11,13,1,1)
        self.grid.addWidget(self.lig2add,12,13,1,1)
        self.grid.addWidget(self.lig3add,13,13,1,1)
        self.grid.addWidget(self.lig4add,14,13,1,1)
        self.grid.addWidget(self.lig5add,15,13,1,1)
        self.grid.addWidget(self.lig6add,16,13,1,1)
        #############################################
        ## Draw ligand button ##
        ctip = 'Generate 2D ligand representation.'
        self.butDrl = mQPushButton('Draw ligands',ctip,12)
        self.butDrl.clicked.connect(self.drawligs)
        self.grid.addWidget(self.butDrl,18,2,1,2)
        ## Search DB button ##
        ctip = 'Search for ligands in chemical databases.'
        self.searchDB = mQPushButton('Search DB',ctip,12)
        self.searchDB.clicked.connect(self.searchDBW)
        self.grid.addWidget(self.searchDB,18,4,1,3)
        ## Local database button ##
        ctip = 'Add core/ligand/binding species to local database.'
        self.butADB = mQPushButton('Add to local DB',ctip,11)
        self.butADB.clicked.connect(self.enableDB)
        self.grid.addWidget(self.butADB,18,7,1,3)
        ##################################################
        ##################################################
        ########### GENERAL PARAMETERS INPUTS ############
        ##################################################
        ##################################################
        self.txtgp = mQLabel('General parameters','','c',20)
        self.grid.addWidget(self.txtgp,4,21,2,9)
        ### jobs dir ###
        ctip = 'Top directory for job folders.'
        self.rtrdir = mQLabel('Jobs dir:',ctip,'Cr',12)
        self.grid.addWidget(self.rtrdir,7,23,1,1)
        self.etrdir = mQLineEdit(globs.rundir,ctip,'l',12)
        self.grid.addWidget(self.etrdir,7,24,1,2)
        # button for browsing rundir
        ctip = 'Browse running directory.'
        self.butpbrdir = mQPushButton('Browse..',ctip,12)
        self.butpbrdir.clicked.connect(self.dirload)
        self.grid.addWidget(self.butpbrdir,7,26,1,2)
        # suffix
        ctip = 'Suffix for job directories.'
        self.rtsuff = mQLabel('Suffix:',ctip,'Cr',12)
        self.etsuff = mQLineEdit('',ctip,'l',14)
        self.grid.addWidget(self.rtsuff,8,23,1,1)
        self.grid.addWidget(self.etsuff,8,24,1,2)
        # random generation
        ctip = 'Enable random generation.'
        self.randomchk = mQCheckBox('Random generation',ctip,12)
        self.randomchk.stateChanged.connect(self.enablerandom)
        self.grid.addWidget(self.randomchk,9,23,1,2)
        # charge calculation
        ctip = 'Calculate charge based on ox state and ligands'
        self.chch = mQCheckBox('Calculate charge',ctip,12)
        self.chch.setDisabled(True)
        self.grid.addWidget(self.chch,9,25,1,2)
        # number of random generated structures
        ctip = 'Number of structures to be randomly generated.'
        self.rtrgen = mQLabel('Structures:',ctip,'Cr',12)
        self.etrgen = mQLineEdit('',ctip,'l',12)
        self.grid.addWidget(self.rtrgen,10,23,1,1)
        self.grid.addWidget(self.etrgen,10,24,1,1)
        self.rtrgen.setDisabled(True)
        self.etrgen.setDisabled(True)
        # number of different ligands to use
        ctip = 'For random generation: number of different ligand types.'
        self.rtlignum = mQLabel('Different ligands:',ctip,'Cr',12)
        self.etlignum = mQLineEdit('',ctip,'l',12)
        self.grid.addWidget(self.rtlignum,10,25,1,2)
        self.grid.addWidget(self.etlignum,10,27,1,1)
        self.rtlignum.setDisabled(True)
        self.etlignum.setDisabled(True)
        # oxidation state
        ctip = 'Metal Oxidation state'
        self.roxstate = mQLabel('Ox State:',ctip,'Cr',12)
        qcav = ['0','I','II','III','IV','V','VI','VII','VIII']
        self.doxs = mQComboBox(qcav,ctip,12)
        self.doxs.setCurrentIndex(0)
        self.grid.addWidget(self.roxstate,11,23,1,1)
        self.grid.addWidget(self.doxs,11,24,1,1)
        # spin state
        ctip = 'System spin multiplicity'
        self.rspstate = mQLabel('Spin:',ctip,'Cr',12)
        qcav = ['1','2','3','4','5','6','7','8','9','10']
        self.dspin = mQComboBox(qcav,ctip,12)
        self.dspin.setCurrentIndex(0)
        self.grid.addWidget(self.rspstate,11,26,1,1)
        self.grid.addWidget(self.dspin,11,27,1,1)
        # create distortion slider
        ctip = 'Percent random distortion from default coordination geometry.'
        self.distper = mQLabel('Distort:0%',ctip,'Cr',12)
        self.sdist = mQSlider(ctip)
        self.sdist.valueChanged.connect(self.sliderChanged)
        self.grid.addWidget(self.distper,12,23,1,2)
        self.grid.addWidget(self.sdist,12,25,1,2)
        # force field optimization
        ctip = 'Perform Force Field optimization'
        self.chkFF = mQCheckBox('FF optimize',ctip,12)
        self.chkFF.stateChanged.connect(self.enableffinput)
        self.grid.addWidget(self.chkFF,13,23,1,2)
        # generate all
        ctip = 'Generate structure with and without optimization.'
        self.chkgenall = mQCheckBox('Generate all',ctip,14)
        self.chkgenall.stateChanged.connect(self.disableffinput)
        self.grid.addWidget(self.chkgenall,14,23,1,2)
        # perform optimization
        ctip = 'Select Force Field'
        qcav = ['MMFF94','UFF','gchemical','GAFF']
        self.dff = mQComboBox(qcav,ctip,12)
        self.dff.setCurrentIndex(0)
        self.dff.setDisabled(True)
        self.grid.addWidget(self.dff,13,25,1,3)
        # optimize before or after
        ctip = 'Optimize before or after building the structure'
        qcav = ['Before','After','Before & After']
        self.dffba = mQComboBox(qcav,ctip,12)
        self.dffba.setDisabled(True)
        self.dffba.setCurrentIndex(2)
        self.grid.addWidget(self.dffba,14,25,1,3)
        # structure generation
        ctip = 'Generate structures'
        self.butGen = mQPushButton('Generate',ctip,18)
        self.butGen.clicked.connect(self.runGUI)
        self.grid.addWidget(self.butGen,16,23,2,2)
        # post-processing setup
        ctip = 'Setup post-processing'
        self.butPost = mQPushButton('Post-process',ctip,16)
        self.butPost.clicked.connect(self.setupp)
        self.grid.addWidget(self.butPost,16,26,2,2)
        ###################################################
        ###################################################
        ########### ADDITIONAL MOLECULE INPUTS ############
        ###################################################
        ###################################################
        ### generate edit texts for additional molecule
        self.txtamol = mQLabel('Additional molecule','','c',20)
        self.txtamol.setDisabled(True)
        self.grid.addWidget(self.txtamol,4,34,2,5)
        # additional molecule
        ctip = 'Place additional molecule'
        self.chkM = mQCheckBox('Extra molecule',ctip,16)
        self.chkM.stateChanged.connect(self.enableemol)
        self.grid.addWidget(self.chkM,7,35,1,3)
        # name of binding species
        ctip = 'Binding species'
        self.rtbind = mQLabel('Molecule:',ctip,'Cr',12)
        self.etbind = mQLineEdit('',ctip,'l',12)
        self.rtbind.setDisabled(True)
        self.etbind.setDisabled(True)
        self.grid.addWidget(self.rtbind,8,34,1,1)
        self.grid.addWidget(self.etbind,8,35,1,2)
        # name of binding molecule from SMILES
        ctip = 'Name of binding molecule using SMILES'
        self.rtbsmi = mQLabel('Name:',ctip,'Cr',12)
        self.etbsmi = mQLineEdit('',ctip,'l',12)
        self.rtbsmi.setDisabled(True)
        self.etbsmi.setDisabled(True)
        self.grid.addWidget(self.rtbsmi,9,34,1,1)
        self.grid.addWidget(self.etbsmi,9,35,1,1)
        # separate in xyz file
        ctip = 'Separate molecules in xyz or input file with ------'
        self.chsep = mQCheckBox('separate',ctip,14)
        self.chsep.setDisabled(True)    
        self.grid.addWidget(self.chsep,9,36,1,2)
        # number of binding conformations to generate
        ctip = 'Number of different conformations to be generated'
        self.rtnbind = mQLabel('Conformations:',ctip,'Cr',12)
        self.etnbind = mQLineEdit('',ctip,'l',12)
        self.rtnbind.setDisabled(True)
        self.etnbind.setDisabled(True)
        self.grid.addWidget(self.rtnbind,10,34,1,1)
        self.grid.addWidget(self.etnbind,10,35,1,1)
        # charge of binding species
        ctip = 'Charge of binding species'
        self.rtchbind = mQLabel('Charge:',ctip,'Cr',12)
        self.etchbind = mQLineEdit('',ctip,'l',12)
        self.rtchbind.setDisabled(True)
        self.etchbind.setDisabled(True)
        self.grid.addWidget(self.rtchbind,10,36,1,1)
        self.grid.addWidget(self.etchbind,10,37,1,1)
        # min/max distance
        ctip = 'Specify placing minimum/maximum distance (in A) and/or axial/equatorial orientation'
        self.rtplace = mQLabel('Distance:',ctip,'Cr',12)
        ctip = 'Minimum distance between the two molecules. 0 corresponds the marginally non-overlapping configuration'
        self.etplacemin = mQLineEdit('',ctip,'l',12)
        ctip = 'Maximum distance between the two molecules. 0 corresponds the marginally non-overlapping configuration'
        self.etplacemax = mQLineEdit('',ctip,'l',12)
        self.rtplace.setDisabled(True)
        self.etplacemin.setDisabled(True)
        self.etplacemax.setDisabled(True)
        self.grid.addWidget(self.rtplace,11,34,1,1)
        self.grid.addWidget(self.etplacemin,11,35,1,1)
        self.grid.addWidget(self.etplacemax,11,36,1,1)
        # mask for atom/center of mass reference
        ctip = 'Reference atoms in extra molecules to be used for placement(e.g. 1,2 or 1-6 or COM or Fe) Default COM (center mass)'
        #self.rtmaskbind = mQLabel('Reference:',ctip,'r',14)
        self.etmaskbind = mQLineEdit('COM',ctip,'l',12)
        #self.rtmaskbind.setDisabled(True)
        self.etmaskbind.setDisabled(True)
        #self.grid.addWidget(self.rtmaskbind,11,37,1,1)
        self.grid.addWidget(self.etmaskbind,11,37,1,1)
        # angle/orientation
        ctip = 'Specify placement type or angle. Angle overwrites placement.'
        self.rtplacea = mQLabel('Angle:',ctip,'Cr',12)
        ctip = 'Azimouthal angle phi from 0 to 180'
        self.etplacephi = mQLineEdit('',ctip,'l',12)
        ctip = 'Polar angle theta from 0 to 360'
        self.etplacetheta = mQLineEdit('',ctip,'l',12)
        self.rtplacea.setDisabled(True)
        self.etplacephi.setDisabled(True)
        self.etplacetheta.setDisabled(True)
        self.grid.addWidget(self.rtplacea,12,34,1,1)
        self.grid.addWidget(self.etplacephi,12,35,1,1)
        self.grid.addWidget(self.etplacetheta,12,36,1,1)
        # placement of extr molecule
        ctip = 'Orientation for placing additional molecule'
        qcav = ['','axial','equatorial']
        self.dmolp = mQComboBox(qcav,ctip,14)
        self.dmolp.setDisabled(True)
        self.grid.addWidget(self.dmolp,12,37,1,1)
        # input file generation
        ctip = 'Generate input files'
        self.chkI = mQCheckBox('Input files',ctip,14)
        self.chkI.stateChanged.connect(self.enableqeinput)
        self.grid.addWidget(self.chkI,13,34,1,2)
        # jobscript generation
        ctip = 'Generate jobscripts'
        self.chkJ = mQCheckBox('Jobscripts',ctip,14)
        self.chkJ.stateChanged.connect(self.enablejinput)
        self.grid.addWidget(self.chkJ,13,36,1,2)
        # input for QC calculation
        ctip = 'Enter input for Quantum Chemistry calculations'
        self.butQc = mQPushButton('Enter QC input',ctip,12)
        self.butQc.setDisabled(True)
        self.butQc.clicked.connect(self.qcinput)
        ctip = 'Select QC code'
        qcav = ['TeraChem','GAMESS','QChem']
        self.qcode = mQComboBox(qcav,ctip,12)
        self.qcode.setDisabled(True)
        self.grid.addWidget(self.butQc,14,34,1,2)
        self.grid.addWidget(self.qcode,15,34,1,2)
        # input for jobscripts
        ctip = 'Enter input for jobscript files'
        self.butJob = mQPushButton('Enter job input',ctip,12)
        self.butJob.setDisabled(True)
        self.butJob.clicked.connect(self.jobenable)
        ctip = 'Select job scheduler'
        qcav = ['SGE','SLURM']
        self.scheduler = mQComboBox(qcav,ctip,12)
        self.scheduler.setDisabled(True)
        self.grid.addWidget(self.butJob,14,36,1,2)
        self.grid.addWidget(self.scheduler,15,36,1,2)
        # quit button
        ctip = 'Quit program'
        self.butQ = mQPushButton('Quit',ctip,14)
        self.butQ.clicked.connect(self.qexit)
        self.grid.addWidget(self.butQ,17,37,1,1)
        ################################################
        ################################################
        ################################################
        ##########################
        ### information window ###
        ##########################
        self.iWind = QWidget()
        self.iWind.setWindowTitle('Running')
        self.iWtxt = mQTextEdit('Program started..','l',14)
        self.iWtxt.setParent(self.iWind)
        self.sgrid.addWidget(self.iWind)
        
        ####################
        ### Run main GUI ###
        ####################
        self.wmain.setLayout(self.grid)
        self.wmain.showMaximized()
        center(self.wmain)
        # resize other windows
        relresize(self.iWind,self.wmain,0.7)
        relresize(self.iWtxt,self.iWind,1.0)
        app.processEvents()
        app.exec_()





























        ##########################################
        ### create local DB interaction window ###
        ##########################################
        self.DBWindow = mWgen(0.3,0.4,'Insert/remove to/from Database') # DB window
        # top text
        self.txtdb = mRtext(self.DBWindow,0.3,0.05,0.4,0.1,'Database Update','',18,'r','c')
        ctip = 'Select what type of molecule you want to add/remove to/from the database'
        # text for selecting type
        self.rtDBsel = mRtext(self.DBWindow,0.14,0.20,0.3,0.1,'Select type:',ctip,14,'r','r')
        # text for selecting type
        ctip = 'Type SMILES string for molecule'
        self.rtDBsmi = mRtext(self.DBWindow,0.14,0.3,0.3,0.1,'SMILES or file:',ctip,14,'r','r')
        self.etDBsmi = mEtext(self.DBWindow,0.465,0.3,0.25,0.08,'',ctip,14,'r','l')
        # text for specifying name
        ctip = 'Type name for molecule'
        self.rtDBname = mRtext(self.DBWindow,0.14,0.4,0.3,0.1,'Name:',ctip,14,'r','r')
        self.etDBname = mEtext(self.DBWindow,0.465,0.4,0.25,0.08,'',ctip,14,'r','l')
        # text for typing denticity
        ctip = 'Type denticity for SMILES molecule'
        self.rtDBsmident = mRtext(self.DBWindow,0.14,0.50,0.3,0.1,'Denticity:',ctip,14,'r','r')
        # drop menu for selecting type
        qcav = ['1','2','3','4','5','6','7','8']
        self.DBdent = mDbox(self.DBWindow,0.465,0.49,0.1,0.08,qcav,ctip,14)
        self.DBdent.setCurrentIndex(0)
        self.rtDBsmident.setDisabled(True)
        self.DBdent.setDisabled(True)
        # text for typing input atoms 
        ctip = 'Type indices for connection atoms, default: 1'
        self.rtDBsmicat = mRtext(self.DBWindow,0.14,0.60,0.3,0.1,'Catoms:',ctip,14,'r','r')
        self.etDBsmicat = mEtext(self.DBWindow,0.465,0.60,0.25,0.08,'',ctip,14,'r','l')
        self.rtDBsmicat.setDisabled(True)
        self.etDBsmicat.setDisabled(True)
        # drop menu for selecting type
        qcav = ['core','ligand','binding']
        self.DBsel = mDbox(self.DBWindow,0.465,0.20,0.2,0.08,qcav,ctip,14)
        self.DBsel.currentIndexChanged.connect(self.dbchange)
        self.DBsel.setCurrentIndex(1)
        # button for addition
        ctip = 'Load example input'
        self.butDBAlf = mButton(self.DBWindow,0.0625,0.7675,0.175,0.09,'Load file',ctip,14)
        self.butDBAlf.clicked.connect(self.qDBload)
        # button for addition
        ctip = 'Add new molecule to database'
        self.butDBAub = mButton(self.DBWindow,0.285,0.75,0.2,0.125,'Add',ctip,14)
        self.butDBAub.clicked.connect(self.qaddDB)
        # button for removal
        ctip = 'Remove molecule database'
        self.butDBDub = mButton(self.DBWindow,0.525,0.75,0.2,0.125,'Remove',ctip,14)
        self.butDBDub.clicked.connect(self.qdelDB)
        # button for return
        ctip = 'Return to main menu'
        self.butDBRet = mButton(self.DBWindow,0.7625,0.7675,0.175,0.09,'Return',ctip,14)
        self.butDBRet.clicked.connect(self.DBWindow.qexitM)
        #############################################
        ### create chemical DB interaction window ###
        #############################################
        self.cDBWindow = mWgen(0.4,0.6,'Chemical Database Search') # DB window
        c = mPic(self.cDBWindow,globs.installdir+'/icons/chemdb.png',0.05,0.75,0.2)
        # top text
        self.txtcdb = mRtext(self.cDBWindow,0.3,0.05,0.4,0.1,'Database Search','',18,'r','c')
        ctip = 'Select the database you want to use. Please not that fastsearch indexes DBs allow for much faster screening.'
        # text for reference
        ctip = 'Reference molecule could be either a SMILES string or a molecule loaded from a file.'
        self.rtcDBref = mRtext(self.cDBWindow,0.05,0.15,0.3,0.1,'Similarity search',ctip,16,'r','r')
        # text for screening options
        ctip = 'Specify screening options or similarity search.'
        self.rtcDBsc = mRtext(self.cDBWindow,0.55,0.15,0.3,0.1,'Screening options',ctip,16,'r','r')
        # text for selecting database
        self.rtcDBsel = mRtext(self.cDBWindow,0.425,0.265,0.3,0.1,'Select database:',ctip,14,'r','r')
        # get existing databases
        dbdir = globs.chemdbdir
        dbs0 = glob.glob(dbdir+"/*.sdf")
        dbs1 = [d.rsplit('/',1)[-1] for d in dbs0]
        dbs = [d.split('.',1)[0] for d in dbs1]
        self.cDBsel = mDbox(self.cDBWindow,0.75,0.255,0.15,0.07,dbs,ctip,14)
        # text for selecting fingerprint
        self.rtcDBsf = mRtext(self.cDBWindow,0.425,0.455,0.3,0.07,'Select Fingerprint:',ctip,14,'r','r')
        # select fingerprint
        opts = ['FP2','FP3','FP4','MACCS']
        self.cDBsf = mDbox(self.cDBWindow,0.75,0.45,0.15,0.06,opts,ctip,14)
        # get options for screening
        ctip = 'Specify minimum and maximum values for filters.'
        self.rtcDBminmax = mRtext(self.cDBWindow,0.575,0.52,0.3,0.07,'min    max',ctip,14,'r','r')
        ctip = 'Total number of atoms.'
        self.rtcDBat0 = mRtext(self.cDBWindow,0.625,0.56,0.1,0.05,'atoms:',ctip,14,'r','r')
        ctip = 'Minimum number of atoms.'
        self.etcDBsatoms0 = mEtext(self.cDBWindow,0.7575,0.56,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Maximum number of atoms.'
        self.etcDBsatoms1 = mEtext(self.cDBWindow,0.8275,0.56,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Total number of bonds.'
        self.rtcDBb0 = mRtext(self.cDBWindow,0.625,0.62,0.1,0.05,'bonds:',ctip,14,'r','r')
        ctip = 'Minimum number of total bonds.'
        self.etcDBsbonds0 = mEtext(self.cDBWindow,0.7575,0.62,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Maximum number of total bonds.'
        self.etcDBsbonds1 = mEtext(self.cDBWindow,0.8275,0.62,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Total number of aromatic.'
        self.rtcDBba0 = mRtext(self.cDBWindow,0.525,0.68,0.2,0.05,'aromatic bonds:',ctip,14,'r','r')
        ctip = 'Minimum number of aromatic bonds.'
        self.etcDBsabonds0 = mEtext(self.cDBWindow,0.7575,0.68,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Maximum number of aromatic bonds.'
        self.etcDBsabonds1 = mEtext(self.cDBWindow,0.8275,0.68,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Total number of single bonds.'
        self.rtcDBbs0 = mRtext(self.cDBWindow,0.575,0.74,0.15,0.05,'single bonds:',ctip,14,'r','r')
        ctip = 'Minimum number of single bonds.'
        self.etcDBsbondss0 = mEtext(self.cDBWindow,0.7575,0.74,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Maximum number of single bonds.'
        self.etcDBsbondss1 = mEtext(self.cDBWindow,0.8275,0.74,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Molecular weight.'
        self.rtcDBbtmw0 = mRtext(self.cDBWindow,0.575,0.80,0.15,0.05,'MW:',ctip,14,'r','r')
        ctip = 'Minimum molecular weight.'
        self.etcDBmw0 = mEtext(self.cDBWindow,0.7575,0.80,0.05,0.05,'',ctip,14,'r','l')
        ctip = 'Maximum molecular weight.'
        self.etcDBmw1 = mEtext(self.cDBWindow,0.8275,0.80,0.05,0.05,'',ctip,14,'r','l')
        # text for selecting type
        ctip = 'Type SMILES string or molecule name for reference molecule in similarity search'
        self.rtcDBsmi = mRtext(self.cDBWindow,0.05,0.2625,0.1,0.1,'SMILES:',ctip,14,'r','r')
        self.etcDBsmi = mEtext(self.cDBWindow,0.16,0.25,0.225,0.08,'',ctip,14,'r','l')
        # text for SMARTS pattern
        ctip = 'Type SMARTS pattern for matching'
        self.rtcDBsmarts = mRtext(self.cDBWindow,0.525,0.3625,0.125,0.1,'SMARTS:',ctip,14,'r','r')
        self.etcDBsmarts = mEtext(self.cDBWindow,0.675,0.35,0.225,0.08,'',ctip,14,'r','l')
        # text for output file
        ctip = 'Please type in output file'
        self.etcDBoutf = mEtext(self.cDBWindow,0.215,0.58,0.15,0.08,'dbres',ctip,14,'r','l')
        self.rtcDBsoutf = mRtext(self.cDBWindow,0.0,0.595,0.175,0.08,'Output file:',ctip,14,'r','r')
        # drop menu for output file
        qcav = ['.smi']#,'.mol','.sdf']
        self.cDBdent = mDbox(self.cDBWindow,0.375,0.58,0.1,0.08,qcav,ctip,14)
        # button for loading from file
        ctip = 'Load reference molecule from file'
        self.rtcDBAlf = mRtext(self.cDBWindow,0.03,0.375,0.125,0.1,'From file:',ctip,14,'r','r')
        self.butcDBAlf = mButton(self.cDBWindow,0.175,0.365,0.15,0.075,'Load..',ctip,14)
        self.butcDBAlf.clicked.connect(self.qcDBload)
        # how many molecules to return
        ctip = 'Specify the number of results you want.'
        self.rtcDBres = mRtext(self.cDBWindow,0.03,0.475,0.125,0.1,'Results:',ctip,14,'r','r')
        self.etcDBnres = mEtext(self.cDBWindow,0.18,0.465,0.05,0.07,'',ctip,14,'r','l')
        # connection atoms for smarts/smiles
        ctip = 'Specify the connection atoms in SMARTS/SMILES. Default: 1'
        self.rtcDBcatoms = mRtext(self.cDBWindow,0.235,0.475,0.15,0.1,'Conn atoms:',ctip,14,'r','r')
        self.etcDBcatoms = mEtext(self.cDBWindow,0.395,0.465,0.075,0.07,'1',ctip,14,'r','l')
        # button for addition
        ctip = 'Search database:'
        self.butcDBAub = mButton(self.cDBWindow,0.325,0.8,0.2,0.125,'Search',ctip,14)
        self.butcDBAub.clicked.connect(self.qaddcDB)
        # button for addition
        ctip = 'Draw results'
        self.butcDBd0 = mButton(self.cDBWindow,0.175,0.675,0.15,0.085,'Draw',ctip,14)
        self.butcDBd0.clicked.connect(self.drawres)
        # button for return
        ctip = 'Return to main menu'
        self.butcDBRet = mButton(self.cDBWindow,0.6,0.875,0.15,0.08,'Return',ctip,14)
        self.butcDBRet.clicked.connect(self.cDBWindow.qexitM)
        #######################################
        ### create terachem-qc input window ###
        #######################################
        self.qctWindow = mWgen(0.3,0.4,'TeraChem input') # QC window
        c0 = mPic(self.qctWindow,globs.installdir+'/icons/petachem.png',0.025,0.025,0.2)
        # top text
        self.txtqc = mRtext(self.qctWindow,0.3,0.05,0.4,0.1,'TeraChem Input','',18,'r','c')
        # text for specifying charge
        ctip = 'Charge of the system, default: 0'
        self.rtqctch = mRtext(self.qctWindow,0.14,0.2,0.15,0.1,'Charge:',ctip,14,'r','r')
        self.etqctch = mEtext(self.qctWindow,0.315,0.2,0.1,0.08,'0',ctip,14,'r','l')
        # text for specifying spin state
        ctip = 'Spin multiplicity of the system, default: 1'
        self.rtqctspin = mRtext(self.qctWindow,0.50,0.2,0.15,0.1,'Spin:',ctip,14,'r','r')
        self.etqctspin = mEtext(self.qctWindow,0.675,0.2,0.1,0.08,'1',ctip,14,'r','l')
        # drop menu for selecting type of calculation
        qcav = ['energy','minimize','ts']
        ctip = 'Specify calculation type, default: minimize'
        self.rtqctcalc = mRtext(self.qctWindow,0.09,0.3,0.2,0.1,'Calculation:',ctip,14,'r','r')
        self.qctcalc = mDbox(self.qctWindow,0.315,0.3,0.2,0.08,qcav,ctip,14)
        # text for specifying electronic structure method
        ctip = 'Select electronic structure method, default: ub3lyp'
        self.rtqctmethod = mRtext(self.qctWindow,0.50,0.3,0.15,0.1,'Method:',ctip,14,'r','r')
        self.etqctmethod = mEtext(self.qctWindow,0.675,0.3,0.2,0.08,'ub3lyp',ctip,14,'r','l')
        # text for specifying basis set
        ctip = 'Select basis set, default: lacvp_s'
        self.rtqctbasis = mRtext(self.qctWindow,0.14,0.4,0.15,0.1,'Basis:',ctip,14,'r','r')
        self.etqctbasis = mEtext(self.qctWindow,0.315,0.4,0.2,0.08,'lacvps_ecp',ctip,14,'r','l')
        # drop menu for selecting dispersion
        qcav = ['yes','no','d2','d3']
        ctip = 'Select dispersion correction'
        self.rtqcdisp = mRtext(self.qctWindow,0.5,0.4,0.15,0.1,'Disp:',ctip,14,'r','r')
        self.qctsel = mDbox(self.qctWindow,0.675,0.4,0.2,0.08,qcav,ctip,14)
        self.qctsel.setCurrentIndex(1)
        # editor for additional input
        ctip='Specify additional input here'
        self.rtqctadd1 = mRtext(self.qctWindow,0.23,0.55,0.15,0.1,'Additional',ctip,14,'r','c')
        self.rtqctadd2 = mRtext(self.qctWindow,0.23,0.60,0.15,0.1,'input',ctip,14,'r','c')
        self.qceditor = mEdtext(self.qctWindow,0.425,0.515,0.375,0.215,'',12,'r','l')
        # button for addition
        ctip = 'make default'
        self.butqctlf = mButton(self.qctWindow,0.1125,0.7875,0.225,0.09,'Make default',ctip,14)
        self.butqctlf.clicked.connect(self.qctdef)
        # button for addition
        ctip = 'Submit input for Quantum Chemistry'
        self.butqctSub = mButton(self.qctWindow,0.4125,0.775,0.2,0.125,'Submit',ctip,14)
        self.butqctSub.clicked.connect(self.qctWindow.qexitM)
        # button for return
        ctip = 'Return to main menu'
        self.butqctRet = mButton(self.qctWindow,0.7125,0.7875,0.175,0.09,'Return',ctip,14)
        self.butqctRet.clicked.connect(self.qctWindow.qexitM)
        # load defaults if existing
        if glob.glob(globs.homedir+'/.tcdefinput.inp'):
                loadfrominputtc(self,globs.homedir+'/.tcdefinput.inp')
        #######################################
        #### create Qchem-qc input window #####
        #######################################
        self.qcQWindow = mWgen(0.3,0.4,'Qchem Input') # QC window
        # top text
        self.txtqc = mRtext(self.qcQWindow,0.3,0.05,0.4,0.1,'QChem Input','',18,'r','c')
        # text for specifying charge
        ctip = 'Charge of the system, default: 0'
        self.rtqcQch = mRtext(self.qcQWindow,0.1,0.2,0.15,0.1,'Charge:',ctip,14,'r','r')
        self.etqcQch = mEtext(self.qcQWindow,0.265,0.2,0.1,0.08,'0',ctip,14,'r','l')
        # text for specifying spin state
        ctip = 'Spin multiplicity of the system, default: 1'
        self.rtqcQspin = mRtext(self.qcQWindow,0.315,0.2,0.15,0.1,'Spin:',ctip,14,'r','r')
        self.etqcQspin = mEtext(self.qcQWindow,0.49,0.2,0.1,0.08,'1',ctip,14,'r','l')
        # additional molecule
        ctip = 'Unrestricted calculation?'
        self.chQun = mCheck(self.qcQWindow,0.60,0.2,0.25,0.07,'Unrestricted',ctip,14)
        self.chQun.setChecked(True)
        # drop menu for selecting type of calculation
        qcav = ['energy','minimize','ts']
        ctip = 'Specify calculation type, default: minimize'
        self.rtqcQcalc = mRtext(self.qcQWindow,0.09,0.3,0.2,0.1,'Calculation:',ctip,14,'r','r')
        self.qcQcalc = mDbox(self.qcQWindow,0.315,0.3,0.175,0.08,qcav,ctip,14)
        # text for specifying basis set
        ctip = 'Select basis set, default: lanl2dz'
        self.rtqcQbasis = mRtext(self.qcQWindow,0.50,0.3,0.15,0.1,'Basis:',ctip,14,'r','r')
        self.etqcQbasis = mEtext(self.qcQWindow,0.675,0.3,0.2,0.08,'lanl2dz',ctip,14,'r','l')
        # text for specifying exchange
        ctip = 'Select exchange, default: b3lyp'
        self.rtqcQex = mRtext(self.qcQWindow,0.10,0.4,0.175,0.1,'Exchange:',ctip,14,'r','r')
        self.etqcQex = mEtext(self.qcQWindow,0.275,0.4,0.175,0.08,'b3lyp',ctip,14,'r','l')
        # text for specifying electronic structure method
        ctip = 'Select correlation, default: none'
        self.rtqcQcor = mRtext(self.qcQWindow,0.50,0.4,0.175,0.1,'Correlation:',ctip,14,'r','r')
        self.etqcQcor = mEtext(self.qcQWindow,0.675,0.4,0.2,0.08,'none',ctip,14,'r','l')
        # editor for additional input
        ctip='Specify additional input here'
        self.rtqcQadd1 = mRtext(self.qcQWindow,0.23,0.55,0.15,0.1,'Additional',ctip,14,'r','c')
        self.rtqcQadd2 = mRtext(self.qcQWindow,0.23,0.60,0.15,0.1,'input',ctip,14,'r','c')
        self.qcQeditor = mEdtext(self.qcQWindow,0.425,0.515,0.375,0.215,'',12,'r','l')
        # button for addition
        ctip = 'make default'
        self.butqcQlf = mButton(self.qcQWindow,0.1125,0.7875,0.225,0.09,'Make default',ctip,14)
        self.butqcQlf.clicked.connect(self.qcqdef)
        # button for addition
        ctip = 'Submit input for Quantum Chemistry'
        self.butqcQSub = mButton(self.qcQWindow,0.4125,0.775,0.2,0.125,'Submit',ctip,14)
        self.butqcQSub.clicked.connect(self.qcQWindow.qexitM)
        # button for return
        ctip = 'Return to main menu'
        self.butqcQRet = mButton(self.qcQWindow,0.7125,0.7875,0.175,0.09,'Return',ctip,14)
        self.butqcQRet.clicked.connect(self.qcQWindow.qexitM)
        # load defaults if existing
        if glob.glob(globs.homedir+'/.qchdefinput.inp'):
            loadfrominputqch(self,globs.homedir+'/.qchdefinput.inp')
        #####################################
        ### create gamess-qc input window ###
        #####################################
        self.qcgWindow = mWgen(0.4,0.5,'GAMESS Input') # QC window
        # top text
        self.txtqcg = mRtext(self.qcgWindow,0.3,0.04,0.4,0.1,'GAMESS Input','',18,'r','c')
        # text for specifying charge
        ctip = 'Charge of the system, default: 0'
        self.rtqcgch = mRtext(self.qcgWindow,0.14,0.155,0.125,0.1,'Charge:',ctip,14,'r','r')
        self.etqcgch = mEtext(self.qcgWindow,0.315,0.15,0.06,0.07,'0',ctip,14,'r','l')
        # text for specifying spin state
        ctip = 'Spin multiplicity of the system, default: 1'
        self.rtqcgspin = mRtext(self.qcgWindow,0.50,0.155,0.125,0.1,'Spin:',ctip,14,'r','r')
        self.etqcgspin = mEtext(self.qcgWindow,0.675,0.15,0.06,0.07,'1',ctip,14,'r','l')
        # drop menu for selecting type of calculation
        qcav = ['energy','minimize','ts']
        ctip = 'Specify calculation type, default: minimize'
        self.rtqcgcalc = mRtext(self.qcgWindow,0.09,0.235,0.2,0.1,'Calculation:',ctip,14,'r','r')
        self.qcgcalc = mDbox(self.qcgWindow,0.315,0.23,0.2,0.07,qcav,ctip,14)
        # text for specifying electronic structure method
        ctip = 'Select electronic structure method, default: ub3lyp'
        self.rtqcgmethod = mRtext(self.qcgWindow,0.50,0.235,0.15,0.1,'Method:',ctip,14,'r','r')
        self.etqcgmethod = mEtext(self.qcgWindow,0.675,0.23,0.15,0.07,'ubl3yp',ctip,14,'r','l')
        # text for specifying basis set
        ctip = 'Select GBASIS input, default: 6'
        self.rtqcgbasis = mRtext(self.qcgWindow,0.14,0.315,0.15,0.1,'GBASIS:',ctip,14,'r','r')
        self.etqcgbasis = mEtext(self.qcgWindow,0.315,0.31,0.15,0.07,'6',ctip,14,'r','l')
        # text for specifying basis set
        ctip = 'Select NGAUSS input, default: N31'
        self.rtqcngauss = mRtext(self.qcgWindow,0.50,0.315,0.15,0.1,'NGAUSS:',ctip,14,'r','r')
        self.etqcngauss = mEtext(self.qcgWindow,0.675,0.31,0.15,0.07,'N31',ctip,14,'r','l')
        # text for specifying polarization functions
        ctip = 'Select NPFUNC input, default: 0'
        self.rtqcnpfunc = mRtext(self.qcgWindow,0.14,0.395,0.15,0.1,'NPFUNC:',ctip,14,'r','r')
        self.etqcnpfunc = mEtext(self.qcgWindow,0.315,0.39,0.15,0.07,'',ctip,14,'r','l')
        # text for specifying polarization functions
        ctip = 'Select NDFUNC input, default: 0'
        self.rtqcndfunc = mRtext(self.qcgWindow,0.50,0.395,0.15,0.1,'NDFUNC:',ctip,14,'r','r')
        self.etqcndfunc = mEtext(self.qcgWindow,0.675,0.39,0.15,0.07,'',ctip,14,'r','l')
        # editor for additional input
        ctip='Specify additional input for block SYS here'
        self.rtqcgadd1 = mRtext(self.qcgWindow,0.12,0.485,0.15,0.1,'SYS input:',ctip,14,'r','c')
        self.qcgedsys = mEdtext(self.qcgWindow,0.275,0.475,0.225,0.125,'',12,'r','l')
        # editor for additional input
        ctip='Specify additional input for block CTRL here'
        self.rtqcgadd2 = mRtext(self.qcgWindow,0.5,0.485,0.15,0.1,'CTRL input:',ctip,14,'r','c')
        self.qcgedctrl = mEdtext(self.qcgWindow,0.655,0.475,0.225,0.125,'',12,'r','l')
        # editor for additional input
        ctip='Specify additional input for block SCF here'
        self.rtqcgadd3 = mRtext(self.qcgWindow,0.12,0.63,0.15,0.1,'SCF input:',ctip,14,'r','c')
        self.qcgedscf = mEdtext(self.qcgWindow,0.275,0.62,0.225,0.125,'',12,'r','l')
        # editor for additional input
        ctip='Specify additional input for block STAT here'
        self.rtqcgadd4 = mRtext(self.qcgWindow,0.5,0.63,0.15,0.1,'STAT input:',ctip,14,'r','c')
        self.qcgedstat = mEdtext(self.qcgWindow,0.655,0.62,0.225,0.125,'',12,'r','l')
        # button for addition
        ctip = 'make default'
        self.butqcglf = mButton(self.qcgWindow,0.1125,0.7875,0.225,0.09,'Make default',ctip,14)
        self.butqcglf.clicked.connect(self.qcgdef)
        # button for addition
        ctip = 'Submit input for Quantum Chemistry'
        self.butqcgSub = mButton(self.qcgWindow,0.4125,0.775,0.2,0.125,'Submit',ctip,14)
        self.butqcgSub.clicked.connect(self.qcgWindow.qexitM)
        # button for return
        ctip = 'Return to main menu'
        self.butqcgRet = mButton(self.qcgWindow,0.7125,0.7875,0.175,0.09,'Return',ctip,14)
        self.butqcgRet.clicked.connect(self.qcgWindow.qexitM)
        # load defaults if existing
        if glob.glob(globs.homedir+'/.gamdefinput.inp'):
                loadfrominputgam(self,globs.homedir+'/.gamdefinput.inp')
        #####################################
        ### create jobscript input window ###
        #####################################
        self.jWindow = mWgen(0.4,0.5,'Jobscript parameters') # jobscript window
        c1 = mPic(self.jWindow,globs.installdir+'/icons/sge.png',0.025,0.035,0.2)
        c2 = mPic(self.jWindow,globs.installdir+'/icons/slurm.png',0.88,0.025,0.1)
        # top text
        self.txtj = mRtext(self.jWindow,0.3,0.025,0.4,0.1,'Jobscript Input','',18,'r','c')
        # text for main job identifier
        ctip = 'Job main identifier, e.g. feII'
        self.rtjname = mRtext(self.jWindow,0.14,0.155,0.125,0.1,'Job name:',ctip,14,'r','r')
        self.etjname = mEtext(self.jWindow,0.315,0.15,0.15,0.07,'myjob',ctip,14,'r','l')
        # text for specifying spin state
        ctip = 'Queue to use, e.g. gpus'
        self.rtjqueue = mRtext(self.jWindow,0.50,0.155,0.125,0.1,'Queue:',ctip,14,'r','r')
        self.etjqueue = mEtext(self.jWindow,0.675,0.15,0.15,0.07,'',ctip,14,'r','l')
        # text for specifying wall time
        ctip = 'Wall time request, e.g. 48'
        self.rtjwallt = mRtext(self.jWindow,0.14,0.235,0.125,0.1,'Wall time:',ctip,14,'r','r')
        self.etjwallt = mEtext(self.jWindow,0.315,0.23,0.15,0.07,'48h',ctip,14,'r','l')
        # text for specifying memory
        ctip = 'Memory request, e.g. 10G'
        self.rtjmem = mRtext(self.jWindow,0.50,0.235,0.125,0.1,'Memory:',ctip,14,'r','r')
        self.etjmem = mEtext(self.jWindow,0.675,0.23,0.15,0.07,'10G',ctip,14,'r','l')
        # text for specifying charge
        ctip = 'Number of CPUs requested, default: 0'
        self.rtjcpus = mRtext(self.jWindow,0.14,0.315,0.125,0.1,'CPUs:',ctip,14,'r','r')
        self.etjcpus = mEtext(self.jWindow,0.315,0.31,0.06,0.07,'',ctip,14,'r','l')
        # text for specifying spin state
        ctip = 'Number of GPUs requested, default: 0'
        self.rtjgpus = mRtext(self.jWindow,0.50,0.315,0.125,0.1,'GPUs:',ctip,14,'r','r')
        self.etjgpus = mEtext(self.jWindow,0.675,0.31,0.06,0.07,'',ctip,14,'r','l')
        # text for modules to be loaded
        ctip = 'Modules to be loaded, e.g. terachem, openmpi'
        self.rtjmod = mRtext(self.jWindow,0.14,0.395,0.125,0.1,'Modules:',ctip,14,'r','r')
        self.etjmod = mEtext(self.jWindow,0.315,0.39,0.325,0.07,'',ctip,14,'r','l')
        # editor for additional input
        ctip='Specify additional input for initial options, e.g. -j y'
        self.rtjadd1 = mRtext(self.jWindow,0.12,0.525,0.15,0.1,'Options:',ctip,14,'r','c')
        self.etjopt = mEdtext(self.jWindow,0.275,0.485,0.225,0.20,'',12,'r','l')
        # editor for additional input
        ctip='Specify additional commands, e.g. mkdir $WORKDIR/test'
        self.rtjadd2 = mRtext(self.jWindow,0.5,0.525,0.15,0.1,'Commands:',ctip,14,'r','c')
        self.jcomm = mEdtext(self.jWindow,0.655,0.485,0.225,0.20,'',12,'r','l')
        # button for addition
        ctip = 'make default'
        self.butqcJlf = mButton(self.jWindow,0.1125,0.7875,0.225,0.09,'Make default',ctip,14)
        self.butqcJlf.clicked.connect(self.jobdef)
        # button for addition
        ctip = 'Submit input for Quantum Chemistry'
        self.butqcgSub = mButton(self.jWindow,0.4125,0.775,0.2,0.125,'Submit',ctip,14)
        self.butqcgSub.clicked.connect(self.jWindow.qexitM)
        # button for return
        ctip = 'Return to main menu'
        self.butqcgRet = mButton(self.jWindow,0.7125,0.7875,0.175,0.09,'Return',ctip,14)
        self.butqcgRet.clicked.connect(self.jWindow.qexitM)
        # load defaults if existing
        if glob.glob(globs.homedir+'/.jobdefinput.inp'):
            loadfrominputjob(self,globs.homedir+'/.jobdefinput.inp')
        ###########################
        ### post-process window ###
        ###########################
        # create window
        self.pWindow = mWgen(0.4,0.5,'Post-processing') # jobscript window
        #c1p = mPic(self.pWindow,globs.installdir+'/icons/wft1.png',0.04,0.7,0.2)
        c3p = mPic(self.pWindow,globs.installdir+'/icons/wft3.png',0.04,0.4,0.2)
        #c2p = mPic(self.pWindow,globs.installdir+'/icons/wft2.png',0.04,0.035,0.2)
        # top text
        self.txtp = mRtext(self.pWindow,0.3,0.05,0.4,0.1,'Post-processing setup','',18,'r','c')
        # input for jobscripts
        ctip = 'Select top jobs directory'
        self.butpd = mButton(self.pWindow,0.15,0.2,0.2,0.1,'Select directory',ctip,14)
        self.butpd.clicked.connect(self.pdload)
        self.etpdir = mEtext(self.pWindow,0.375,0.215,0.2,0.07,globs.rundir,ctip,14,'r','l')
        # select qc code
        ctip = 'Select QC code'
        qcav = ['TeraChem','GAMESS']
        self.txtpqe= mRtext(self.pWindow,0.575,0.2,0.15,0.1,'QC code:','',14,'r','c')
        self.pqcode = mDbox(self.pWindow,0.725,0.21,0.15,0.085,qcav,ctip,14)
        # general summary
        ctip = 'Generate results summary'
        self.psum = mCheck(self.pWindow,0.325,0.325,0.2,0.1,'Summary',ctip,16)
        # metal charges
        ctip = 'Calculate metal charge'
        self.pch = mCheck(self.pWindow,0.55,0.325,0.2,0.1,'Charge',ctip,16)
        # wavefunction properties
        ctip = 'Generate average properties of the wavefunction'
        self.pwfnav = mCheck(self.pWindow,0.325,0.425,0.2,0.1,'Wavefunction',ctip,16)
        # cube files
        ctip = 'Generate cubefiles'
        self.pcub = mCheck(self.pWindow,0.55,0.425,0.2,0.1,'Cubes',ctip,16)
        # molecular orbital information
        ctip = 'Molecular Orbital information'
        self.porbs = mCheck(self.pWindow,0.325,0.525,0.2,0.1,'MO',ctip,16)
        # d-orbital information
        #ctip = 'd-orbital information'
        #self.pdorbs = mCheck(self.pWindow,0.55,0.525,0.2,0.1,'d-orbitals',ctip,16)
        # delocalization indices
        ctip = 'Localization and delocalization indices'
        self.pdeloc = mCheck(self.pWindow,0.325,0.625,0.2,0.1,'Deloc',ctip,16)
        # NBO analysis
        ctip = 'NBO analysis'
        self.pnbo = mCheck(self.pWindow,0.55,0.525,0.2,0.1,'NBO',ctip,16)
        # button for addition
        ctip = 'Run post-processing'
        self.butpR = mButton(self.pWindow,0.4125,0.775,0.2,0.125,'Run',ctip,14)
        self.butpR.clicked.connect(self.postprocGUI)
        # button for return
        ctip = 'Return to main menu'
        self.butpret = mButton(self.pWindow,0.7125,0.7875,0.175,0.09,'Return',ctip,14)
        self.butpret.clicked.connect(self.pWindow.qexitM)
    '''
    #############################
    ### Callbacks for buttons ###
    #############################
    '''
    ###################################
    ###### Add new ligands input ######
    ###################################
    def addlig0(self):
        txt0 = self.lig0.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig0add.setDisabled(True)
            self.lig0add.hide()
            self.lig1add.setDisabled(False)
            self.lig1add.show()
            self.lig1.setDisabled(False)
            self.lig1occ.setDisabled(False)
            self.lig1conn.setDisabled(False)
            self.lig1H.setDisabled(False)
            self.lig1ML.setDisabled(False)
            self.lig1an.setDisabled(False)
            self.lig1nam.setDisabled(False)
    def addlig1(self):
        txt0 = self.lig1.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig1add.setDisabled(True)
            self.lig1add.hide()
            self.lig2add.setDisabled(False)
            self.lig2add.show()
            self.lig2.setDisabled(False)
            self.lig2occ.setDisabled(False)
            self.lig2conn.setDisabled(False)
            self.lig2H.setDisabled(False)
            self.lig2ML.setDisabled(False)
            self.lig2an.setDisabled(False)
            self.lig2nam.setDisabled(False)
    def addlig2(self):
        txt0 = self.lig2.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig2add.setDisabled(True)
            self.lig2add.hide()
            self.lig3add.setDisabled(False)
            self.lig3add.show()
            self.lig3.setDisabled(False)
            self.lig3occ.setDisabled(False)
            self.lig3conn.setDisabled(False)
            self.lig3H.setDisabled(False)
            self.lig3ML.setDisabled(False)
            self.lig3an.setDisabled(False)
            self.lig3nam.setDisabled(False)
    def addlig3(self):
        txt0 = self.lig3.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig3add.setDisabled(True)
            self.lig3add.hide()
            self.lig4add.setDisabled(False)
            self.lig4add.show()
            self.lig4.setDisabled(False)
            self.lig4occ.setDisabled(False)
            self.lig4conn.setDisabled(False)
            self.lig4H.setDisabled(False)
            self.lig4ML.setDisabled(False)
            self.lig4an.setDisabled(False)
            self.lig4nam.setDisabled(False)
    def addlig4(self):
        txt0 = self.lig4.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig4add.setDisabled(True)
            self.lig4add.hide()
            self.lig5add.setDisabled(False)
            self.lig5add.show()
            self.lig5.setDisabled(False)
            self.lig5occ.setDisabled(False)
            self.lig5conn.setDisabled(False)
            self.lig5H.setDisabled(False)
            self.lig5ML.setDisabled(False)
            self.lig5an.setDisabled(False)
            self.lig5nam.setDisabled(False)
    def addlig5(self):
        txt0 = self.lig0.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig5add.setDisabled(True)
            self.lig5add.hide()
            self.lig6add.setDisabled(False)
            self.lig6add.show()
            self.lig6.setDisabled(False)
            self.lig6occ.setDisabled(False)
            self.lig6conn.setDisabled(False)
            self.lig6H.setDisabled(False)
            self.lig6ML.setDisabled(False)
            self.lig6an.setDisabled(False)
            self.lig6nam.setDisabled(False)
    def addlig6(self):
        txt0 = self.lig0.text().replace(' ','')
        if len(txt0)==0:
            mQDialogWarn('No ligand specified','Please specify a ligand before adding another one.')
        else:
            self.lig6add.setDisabled(True)
            self.lig6add.hide()
            self.lig7.setDisabled(False)
            self.lig7occ.setDisabled(False)
            self.lig7conn.setDisabled(False)
            self.lig7H.setDisabled(False)
            self.lig7ML.setDisabled(False)
            self.lig7an.setDisabled(False)
            self.lig7nam.setDisabled(False)
    ### enable add new geometry
    def addgeom(self):
        a=1
    ##############################
    ### Local Database window ####
    ##############################
    ### load molecule from file
    def qDBload(self):
        name = QFileDialog.getOpenFileName(self.DBWindow,'Open File','.',"Molecule files *.xyz, *.mol (*.xyz *.mol)")
        if name[0] != '':
            self.etDBsmi.setText(os.path.relpath(name[0]))
    ### enable add to database interface
    def enableDB(self):
        self.DBWindow.setWindowModality(2)
        self.DBWindow.show()
    ### callback for addition button, adds to database
    def qaddDB(self):
        coption = self.DBsel.currentText()
        smimol = self.etDBsmi.text()
        sminame = self.etDBname.text()
        smident = self.DBdent.currentText()
        smicat = self.etDBsmicat.text()
        if smimol=='' or sminame=='':
            choice = QMessageBox.warning(self.DBWindow,'Error','Please specify molecule and name!')
        else:
            # add to database
            if 'ligand' in coption:
                emsg = addtoldb(smimol,sminame,smident,smicat)
            elif 'core' in coption:
                emsg = addtocdb(smimol,sminame,smicat)
            elif 'bind' in coption:
                emsg = addtobdb(smimol,sminame)
            if emsg:
                choice = QMessageBox.warning(self.DBWindow,'Error',emsg)
            else:
                choice = QMessageBox.information(self.DBWindow,'Add','Successfully added to the database!')
    ### callback for removal button, removes from db
    def qdelDB(self):
        coption = self.DBsel.currentIndex()
        sminame = self.etDBname.text()
        if sminame=='':
            choice = QMessageBox.warning(self.DBWindow,'Error','Please specify name!')
        else:
            # remove from database
            emsg = removefromDB(sminame,int(coption))
            if emsg:
                choice = QMessageBox.warning(self.DBWindow,'Error',emsg)
            else:
                choice = QMessageBox.information(self.DBWindow,'Remove','Removed from the database!')
    ### db type change
    def dbchange(self):
        ci = self.DBsel.currentIndex()
        if (ci==1):
            self.rtDBsmident.setDisabled(False)
            self.DBdent.setDisabled(False)
            self.rtDBsmicat.setDisabled(False)
            self.etDBsmicat.setDisabled(False)
        elif(ci==0):
            self.rtDBsmident.setDisabled(True)
            self.DBdent.setDisabled(True)
            self.rtDBsmicat.setDisabled(False)
            self.etDBsmicat.setDisabled(False)
        else:
            self.rtDBsmident.setDisabled(True)
            self.DBdent.setDisabled(True)
            self.rtDBsmicat.setDisabled(True)
            self.etDBsmicat.setDisabled(True)
    ### perform post-processing
    def postprocGUI(self):
        rdir = self.etpdir.text()
        if rdir[-1]=='/':
            rdir = rdir[:-1]
        defaultparams = ['main.py','-i',rdir+'/postproc.inp']
        grabguivarsP(self)
        self.pWindow.close()
        self.sgrid.setCurrentWidget(self.iWind)
        emsg = startgen(defaultparams,True,self)
        if not emsg:
            choice = QMessageBox.information(self.pWindow,'DONE','Your results are ready..')
    #############################
    ### Chem Database window ####
    #############################
    ### load molecule from file
    def qcDBload(self):
        name = QFileDialog.getOpenFileName(self.DBWindow,'Open File','.',"Molecule files *.xyz, *.mol *.sdf *.smi (*.xyz *.mol *.sdf *.smi)")
        if name[0] != '':
            self.etcDBsmi.setText(os.path.relpath(name[0]))
    ### enable add to database interface
    def searchDBW(self):
        globs = globalvars()
        self.cDBWindow.setWindowModality(2)
        self.cDBWindow.show()
        writef = False
        instdir = globs.installdir
        mwfn = globs.multiwfn
        cdbdir = globs.chemdbdir
        if not os.path.isdir(globs.chemdbdir):
            choice = QMessageBox.question(self.cDBWindow,'Database setup','It looks like the Chemical Database directory is not configured or does not exist. Would you like to configure it now?',
                QMessageBox.Yes, QMessageBox.No)
            if choice == QMessageBox.Yes:
                QMessageBox.information(self.cDBWindow,'Chem DB',"Please select the directory containing chemical databases.")
                cdbdir = QFileDialog.getExistingDirectory(self.cDBWindow,'Select the directory containing chemical databases.')
                if len(cdbdir) > 0:
                    writef = True
        if writef:
            f = open(globs.homedir+'/.molSimplify','w')
            f.write("INSTALLDIR="+instdir+'\n')
            f.write("CHEMDBDIR="+cdbdir+'\n')
            if len(mwfn) > 1 :
                f.write("MULTIWFN="+mwfn[0]+'\n')
            f.close()
            # get existing databases
            globsnew = globalvars()
            dbdir = globsnew.chemdbdir
            dbs0 = glob.glob(dbdir+"/*.sdf")
            dbs1 = [d.rsplit('/',1)[-1] for d in dbs0]
            dbs = [d.split('.',1)[0] for d in dbs1]
            for d in dbs:
                self.cDBsel.addItem(d)
    ### callback for database search
    def qaddcDB(self):
        # search database
        dbinfw = mWindow(0.2,0.2)
        tt = mRtext(dbinfw,0.5,0.5,0.1,0.1,'Searching...','',14,'r','c')
        dbinfw.show()
         ### collects all the info and passes it to molSimplify ###
        rdir = self.etrdir.text()
        if rdir[-1]=='/':
            rdir = rdir[:-1]
        # create running dir if not existing
        if not os.path.isdir(rdir):
            os.mkdir(rdir)
        args = grabdbguivars(self)
        defaultparams = ['main.py','-i',rdir+'/dbinput.inp']
        emsg = startgen(defaultparams,True,self)
        if not emsg:
            choice = QMessageBox.information(self.DBWindow,'DONE','Search is done..')
        self.cDBWindow.show()
    ### db type change
    def cdbchange(self):
        ci = self.DBsel.currentIndex()
        if (ci==1):
            self.rtDBsmident.setDisabled(False)
            self.DBdent.setDisabled(False)
            self.rtDBsmicat.setDisabled(False)
            self.etDBsmicat.setDisabled(False)
        else:
            self.rtDBsmident.setDisabled(True)
            self.DBdent.setDisabled(True)
            self.rtDBsmicat.setDisabled(True)
            self.etDBsmicat.setDisabled(True)
    ####################
    ### Main window ####
    ####################
    ### run generation
    def runGUI(self):
        ### collects all the info and passes it to molSimplify ###
        rdir = self.etrdir.text()
        if rdir[-1]=='/':
            rdir = rdir[:-1]
        # creat running dir if not existing
        if not os.path.isdir(rdir):
            os.mkdir(rdir)
        # get parameters
        args = grabguivars(self)
        defaultparams = ['main.py','-i',rdir+'/geninput.inp']
        self.sgrid.setCurrentWidget(self.iWind)
        msgBox = QMessageBox()
        if len(args['-rgen']) > 0:
            msgBox.setText("Random generation initiated. This process might take some time.")
            msgBox.setIcon(1)
            msgBox.setInformativeText('Please be patient. OK?')
            msgBox.setWindowTitle('Running..')
            msgBox.exec_()
        # do the generation
        emsg = startgen(defaultparams,True,self)
        if not emsg:
            QMessageBox.information(self.wmain,'Done','Structure generation terminated successfully!')
        else:
            QMessageBox.warning(self.wmain,'Problem',emsg)
    ### draw ligands
    def drawligs(self):
        ### collects all the info and passes it to molSimplify ###
        rdir = self.etrdir.text()
        if rdir[-1]=='/':
            rdir = rdir[:-1]
        # creat running dir if not existing
        if not os.path.isdir(rdir):
            os.mkdir(rdir)
        args = grabguivars(self)
        if len(args['-lig']) < 1:
            qm = QMessageBox.warning('Warning','No ligands are specified.')
            qm.setParent(self.wmain)
            return False
        else:
            args['-lig']=args['-lig'].replace(' ','')
            lls = args['-lig'].split(',')
            liglist = []
            # check if multiple ligands in .smi file
            for l in lls:
                if '.smi' in l:
                    f = open(l,'r')
                    smis = filter(None,f.read().splitlines())
                    liglist += smis
                else:
                    liglist.append(l)
            globs = globalvars()
            licores = readdict(globs.installdir+'/Ligands/ligands.dict')
            ligs = []
            for l in liglist:
                if isinstance(l,unicode):
                    ll = unicodedata.normalize('NFKD',l).encode('ascii','ignore')
                else:
                    ll = l
                lig,emsg = lig_load(globs.installdir+'/',ll,licores)
                if emsg:
                    QMessageBox.warning(self.mainWindow,'Error',emsg)
                else:
                    ligs.append(lig.OBmol)
            if len(ligs)==0:
                return
            fcount = 0
            while glob.glob(rdir+'/ligs'+str(fcount)+'.png'):
                fcount += 1
            outputf  = 'ligs.smi'
            locf = 'ligs'+str(fcount)
            outbase = rdir+'/'+locf
            outf = pybel.Outputfile("smi",outputf,overwrite=True)
            for mol in ligs:
                outf.write(mol)
            # convert to svg
            if globs.osx:
                cmd = "/usr/local/bin/obabel -ismi "+outputf+" -O "+locf+".svg -xC -xi"
            else:
                cmd = "obabel -ismi "+outputf+" -O "+locf+".svg -xC -xi"
            t = mybash(cmd)
            print t
            if glob.glob(outputf):
                os.remove(outputf)
            else:
                QMessageBox.information(self.mainWindow,'Error','Image could not be generated\n.')
                return
            ####################
            ### draw ligands ###
            ####################
            if globs.osx:
                cmd = '/usr/local/bin/convert -density 1200 '+locf+'.svg '+locf+'.png'
            else:
                cmd = 'convert -density 1200 '+locf+'.svg '+locf+'.png'
            s = mybash(cmd)
            print s
            if not glob.glob(locf+'.png') :
                QMessageBox.information(self.mainWindow,'Done','2D representation of ligands generated in file ' +outbase+'.svg ! Conversion to png failed.')
            else:
                os.remove(locf+".svg")
                shutil.move(locf+'.png',outbase+'.png')
                # create window
                self.lwindow = mWgen(0.4,0.5,'Ligands') # jobscript window
                c1p = mPic2(self.lwindow,outbase+'.png',0.0,0.0,0.5,0.5)
                self.lwindow.show()
                # button for closing window
                ctip = 'Close current window'
                self.lwclose = mButton(self.lwindow,0.40,0.85,0.2,0.1,'Close',ctip,14)
                self.lwclose.clicked.connect(self.qexit)
    ### draw results from db search
    def drawres(self):
        ### collects all the info and passes it to molSimplify ###
        rdir = self.etrdir.text()
        if rdir[-1]=='/':
            rdir = rdir[:-1]
        # creat running dir if not existing
        if not os.path.isdir(rdir):
            os.mkdir(rdir)
        outf = rdir+'/'+self.etcDBoutf.text()
        outf = outf.replace(' ','')+'.smi'
        print outf
        if not glob.glob(outf):
            QMessageBox.warning(self.cDBWindow,'Warning','No database results file in '+rdir)
            return False
        else:
            lls = [outf]
            liglist = []
            # check if multiple ligands in .smi file
            for l in lls:
                if '.smi' in l:
                    f = open(l,'r')
                    smis = filter(None,f.read().splitlines())
                    liglist += smis
                else:
                    liglist.append(l)
            globs = globalvars()
            licores = readdict(globs.installdir+'/Ligands/ligands.dict')
            ligs = []
            for l in liglist:
                if isinstance(l,unicode):
                    ll = unicodedata.normalize('NFKD',l).encode('ascii','ignore')
                else:
                    ll = l
                lig,emsg = lig_load(globs.installdir+'/',ll,licores)
                if emsg:
                    QMessageBox.warning(self.mainWindow,'Error',emsg)
                else:
                    ligs.append(lig.OBmol)
            if len(ligs)==0:
                return
            fcount = 0
            while glob.glob(rdir+'/ligs'+str(fcount)+'.png'):
                fcount += 1
            outputf  = 'ligs.smi'
            locf = 'ligs'+str(fcount)
            outbase = rdir+'/'+locf
            outf = pybel.Outputfile("smi",outputf,overwrite=True)
            for mol in ligs:
                outf.write(mol)
            # convert to svg
            if globs.osx:
                cmd = "/usr/local/bin/obabel -ismi "+outputf+" -O "+locf+".svg -xC -xi"
            else:
                cmd = "obabel -ismi "+outputf+" -O "+locf+".svg -xC -xi"
            t = mybash(cmd)
            print t
            if glob.glob(outputf):
                os.remove(outputf)
            else:
                QMessageBox.information(self.cDBWindow,'Error','Image could not be generated\n.')
                return
            ####################
            ### draw ligands ###
            ####################
            if globs.osx:
                cmd = '/usr/local/bin/convert -density 1200 '+locf+'.svg '+locf+'.png'
            else:
                cmd = 'convert -density 1200 '+locf+'.svg '+locf+'.png'
            s = mybash(cmd)
            print s
            if not glob.glob(locf+'.png') :
                QMessageBox.information(self.cDBWindow,'Done','2D representation of ligands generated in file ' +outbase+'.svg ! Conversion to png failed.')
            else:
                os.remove(locf+".svg")
                shutil.move(locf+'.png',outbase+'.png')
                # create window
                self.lwindow = mWgen(0.4,0.5,'Ligands') # jobscript window
                c1p = mPic2(self.lwindow,outbase+'.png',0.0,0.0,0.5,0.5)
                self.lwindow.setWindowModality(2)
                self.lwindow.show()
                # button for closing window
                ctip = 'Close current window'
                self.lwclose = mButton(self.lwindow,0.40,0.85,0.2,0.1,'Close',ctip,14)
                self.lwclose.clicked.connect(self.qexit)
    ### enable random input
    def enablerandom(self):
        if self.randomchk.isChecked():
            self.rtrgen.setDisabled(False)
            self.etrgen.setDisabled(False)
            self.rtlignum.setDisabled(False)
            self.etlignum.setDisabled(False)
        else:
            self.rtrgen.setDisabled(True)
            self.etrgen.setDisabled(True)
            self.rtlignum.setDisabled(True)
            self.etlignum.setDisabled(True)
    ### generate all enable FF input
    def disableffinput(self):
        if self.chkgenall.isChecked():
            self.dff.setDisabled(True)
            self.dffba.setDisabled(True)
            self.chkFF.state = True
            self.chkFF.setDisabled(True)
        else:
            self.dff.setDisabled(False)
            self.dffba.setDisabled(False)
            self.chkFF.setDisabled(False)
            self.enableffinput()
    ### enable FF input
    def enableffinput(self):
        if self.chkFF.isChecked():
            self.chkFF.state = False
            self.dff.setDisabled(False)
            self.dffba.setDisabled(False)
        else:
            self.dff.setDisabled(True)
            self.dffba.setDisabled(True)
            self.chkFF.state = True
    ### load file for editing
    def qloadinput(self):
        name = QFileDialog.getOpenFileName(self.wmain,'Open File')[0]
        if name != '':
            loadfrominputfile(self,name)
    ### load directory
    def dirload(self):
        name = QFileDialog.getExistingDirectory(self.wmain,'Select Directory')
        if len(name) >0 and name[0] != '':
            self.etrdir.setText(name)
    ### save as input file
    def qsaveinput(self,gui):
        name = QFileDialog.getSaveFileName(self.wmain,'Save as..','.',"Input files * (*)")[0]
        if name != '':
            varsg = grabguivars(self)
            writeinputc(varsg,name)
    ### show help menu
    def qshowhelp(self):
        a = 1
    def getscreensize(self):
        screenShape = QDesktopWidget().screenGeometry()
        width = int(screenShape.width())
        height = int(screenShape.height())
        return [width,height]
    ### slider changed value
    def sliderChanged(self,val):
        self.distper.setText('Distort:'+str(val)+'%')
    ### match index with coordination
    def matchgeomcoord(self):
        # get current index
        dc=self.dcoord.currentIndex()
        coords,geomnames,geomshorts,geomgroups = getgeoms()
        qcav = geomgroups
        ctip = geomnames
        # empty the box
        for i in range(0,self.dcoordg.count()):
            self.dcoordg.removeItem(0)
        qc = qcav[dc]
        # add to box
        for i,t in enumerate(qc):
            self.dcoordg.insertItem(i,t)
        # set default geometry
        self.dcoordg.setCurrentIndex(0)
        # get global index
        elem = [i for i,s in enumerate(geomshorts) if s in self.dcoordg.currentText()]
        ct = ''
        for ii in range(elem[0],elem[0]+len(geomgroups[dc])):
            ct += ctip[ii]+', '
        ct = ct[:-2]
        # set correct tooltip
        self.dcoordg.setToolTip(ct)
    ### start window in browser to visualize molecule
    def showmolBrowser(self):
        if len(self.etrdir.text()) > 0 :
            fd = self.etrdir.text()
        else:
            fd = '.'
        fname = QFileDialog.getOpenFileName(self.qctWindow,'Open File',fd,"Molecule files *.xyz, *.mol *.sdf *.smi (*.xyz *.mol *.sdf *.smi)")[0]
        if fname != '':
            fname = os.path.relpath(fname)
            fname = unicodedata.normalize('NFKD',fname).encode('ascii','ignore')
            notebook.draw(fname) # draw molecule in browser
    ### enable extra molecule input
    def enableemol(self):
        if self.chkM.isChecked():
            self.chkM.state = False
            self.txtamol.setDisabled(False)
            self.rtbind.setDisabled(False)
            self.etbind.setDisabled(False)
            self.rtbsmi.setDisabled(False)
            self.etbsmi.setDisabled(False)
            self.rtnbind.setDisabled(False)
            self.etnbind.setDisabled(False)    
            self.rtplace.setDisabled(False)
            self.etplacemin.setDisabled(False)
            self.etplacemax.setDisabled(False)
            self.dmolp.setDisabled(False)
            self.rtchbind.setDisabled(False)
            self.etchbind.setDisabled(False)
            self.rtplacea.setDisabled(False)
            self.etplacephi.setDisabled(False)
            self.etplacetheta.setDisabled(False)
            #self.rtmaskbind.setDisabled(False)
            self.etmaskbind.setDisabled(False)
            self.chsep.setDisabled(False)
        else:
            self.txtamol.setDisabled(True)
            self.rtbind.setDisabled(True)
            self.etbind.setDisabled(True)
            self.rtbsmi.setDisabled(True)
            self.etbsmi.setDisabled(True)
            self.rtnbind.setDisabled(True)
            self.etnbind.setDisabled(True)    
            self.rtplace.setDisabled(True)
            self.etplacemin.setDisabled(True)
            self.etplacemax.setDisabled(True)
            self.dmolp.setDisabled(True)
            self.chkM.state = True
            self.rtchbind.setDisabled(True)
            self.etchbind.setDisabled(True)
            self.rtplacea.setDisabled(True)
            self.etplacephi.setDisabled(True)
            self.etplacetheta.setDisabled(True)
            #self.rtmaskbind.setDisabled(True)
            self.etmaskbind.setDisabled(True)
            self.chsep.setDisabled(True)
    #####################
    #### QEt/g input ####
    #####################
    ### callback for QE input
    def qcinput(self):
        if self.chch.getState():
            self.etqcgch.setDisabled(True)
            self.etqctch.setDisabled(True)
            self.etqcQch.setDisabled(True)
        if self.qcode.currentIndex()==0: # generate terachem input
            self.qctWindow.setWindowModality(2)
            self.qctWindow.show()
        elif self.qcode.currentIndex()==1: # generate GAMESS input
            self.qcgWindow.setWindowModality(2)
            self.qcgWindow.show()
        elif self.qcode.currentIndex()==2: # generate Qchem input
            self.qcQWindow.setWindowModality(2)
            self.qcQWindow.show()
    # make default button callback
    def jobdef(self):
        grabguivarsjob(self)
        QMessageBox.information(self.mainWindow,'Done','The current settings are the default ones now.')
    def qctdef(self):
        grabguivarstc(self)
        QMessageBox.information(self.mainWindow,'Done','The current settings are the default ones now.')
    def qcgdef(self):
        grabguivarsgam(self)
        QMessageBox.information(self.mainWindow,'Done','The current settings are the default ones now.')
    def qcqdef(self):
        grabguivarsqch(self)
        QMessageBox.information(self.mainWindow,'Done','The current settings are the default ones now.')
    def qcgload(self):
        name = QFileDialog.getOpenFileName(self.qctWindow,'Open File','.',"GAMESS input files")
        if name[0] != '':
            f = open(name[0],'r')
            self.qcgWindow.molf = f.read()
            f.close()
    ### enable QE input
    def enableqeinput(self):
        if self.chkI.isChecked():
            self.chkI.state = False
            self.qcode.setDisabled(False)
            self.butQc.setDisabled(False)
            self.chch.setDisabled(False)
        else:
            self.qcode.setDisabled(True)
            self.butQc.setDisabled(True)
            self.chch.setDisabled(True)
            self.chkI.state = True
    #########################
    #### jobscript input ####
    #########################
    ### enable Jobscript input
    def enablejinput(self):
        if self.chkJ.isChecked():
            self.chkJ.state = False
            self.scheduler.setDisabled(False)
            self.butJob.setDisabled(False)
        else:
            self.scheduler.setDisabled(True)
            self.butJob.setDisabled(True)
            self.chkJ.state = True
    def jobenable(self):
            self.jWindow.setWindowModality(2)
            self.jWindow.show()
    ### load file
    def jload(self):
        name = QFileDialog.getOpenFileName(self.qctWindow,'Open File','.',"Jobscript files")
        if name[0] != '':
            f = open(name[0],'r')
            self.jWindow.molf = f.read()
            f.close()
    ###############################
    #### post-processing input ####
    ###############################
    ### enable Post processing input
    def setupp(self):
        self.pWindow.setWindowModality(2)
        self.pWindow.show()
        # check if Multiwfn exists
        globs = globalvars()
        inputtxt = '0\n0\n' 
        f = open('input1','w')
        f.write(inputtxt)
        f.close()
        writef = False
        instdir = globs.installdir
        mwfn = globs.multiwfn
        cdbdir = globs.chemdbdir
        if not os.path.isfile(globs.multiwfn[1:-1]):
            choice = QMessageBox.question(self.pWindow,'Multiwfn setup','It looks like the Multiwfn executable is not configured or does not exist. Would you like to configure it now?',
                QMessageBox.Yes, QMessageBox.No)
            if choice == QMessageBox.Yes:
                QMessageBox.information(self.pWindow,'Multiwfn',"Please select the Multiwfn executable.")
                mwfn = QFileDialog.getOpenFileName(self.pWindow,'Select the Multiwfn executable.','.')
                if len(mwfn[0]) > 1:
                    writef = True
        if writef:
            f = open(globs.homedir+'/.molSimplify','w')
            f.write("INSTALLDIR="+instdir+'\n')
            if len(cdbdir) > 0:
                f.write("CHEMDBDIR="+cdbdir+'\n')
            if len(mwfn) > 0 :
                f.write("MULTIWFN="+mwfn[0]+"\n")
            f.close()
        newglobs = globalvars()
        com = newglobs.multiwfn
        tt = mybash(com + '< input1')
        os.remove('input1')
        if not 'Multifunctional Wavefunction Analyzer' in tt:
            self.pch.setDisabled(True)
            self.pwfnav.setDisabled(True)
            self.pcub.setDisabled(True)
            self.pdeloc.setDisabled(True)
    ### load directory
    def pdload(self):
        name = QFileDialog.getExistingDirectory(self.pWindow,'Select Directory')
        if len(name) >0 and name[0] != '':
            self.etpdir.setText(name)
    ###############################
    ###### general callbacks ######
    ###############################
    ### exit application ###
    def qexit(self):
        choice = QMessageBox.question(self.wmain,'Exit','Are you sure you want to quit?',
                QMessageBox.Yes, QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass
    ### hide current widget ###
    def qhide(self):
        self.hide()
