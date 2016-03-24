# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

####################################################
########### Defines main class of GUI  #############
####################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *
from Classes.mWindow import *
from Classes.mGUI import *
from Classes.mPic import *
from Classes.mText import *
from Classes.mButton import *
from Classes.mMenubar import *
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
    ### constructor of gui ###
    def __init__(self,app):
        ### get screen size
        refsize = [1920,1080] # monitor size, aspect ratio
        macbook11=[1366,768] # macbook 11"
        macbook13=[2560,1600] # macbook 13" (both pro&air)
        macbook15=[2880,1800] # macbook 15"
        csize = self.getscreensize()
        self.app = app
        # build for regular screen
        if csize[0] < 1400:
        # build for macbook 11"
            small = True
        else:
            small = False
        # build gui
        self.initGUIref(small)

    ### builds the gui
    def initGUIref(self,small):
        '''
        ######################
        ### build main GUI ###
        ######################
        '''
        ### check for configuration file ###
        homedir = os.path.expanduser("~")
        globs = globalvars() # global variables
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
        if small:
            self.mainWindow = mWindow(0.85,0.85) # main window
        else:
            ### create main window
            self.mainWindow = mWindow(0.7,0.8) # main window
        ### build menu bar
        self.menubar0 = mMenubar(self.mainWindow,self)
        ### place title top
        clogo = mPic(self.mainWindow,globs.installdir+'/icons/logo.png',0.375,0.06,0.25)
        ### place logo bottom and developers text
        c = mPic(self.mainWindow,globs.installdir+'/icons/hjklogo.png',0.4,0.9,0.2)
        self.txtdev = mRtext(self.mainWindow,0.175,0.91,0.3,0.05,'Developed by','',14,'r','c')
        ###############################################
        ### generate edit texts for job information ###
        ###############################################
        self.txtgpar = mRtext(self.mainWindow,0.4,0.175,0.2,0.05,'General parameters','',18,'r','c')
        ctip = 'Top directory for job folders'
        self.rtrdir = mRtext(self.mainWindow,0.335,0.245,0.1,0.05,'Jobs dir:',ctip,14,'r','r')
        self.etrdir = mEtext(self.mainWindow,0.445,0.24,0.1,0.05,globs.rundir,ctip,14,'r','l')
        ctip = 'Suffix for job directories'
        self.rtsuff = mRtext(self.mainWindow,0.36,0.31,0.1,0.05,'Suffix for dir:',ctip,14,'r','r')
        self.etsuff = mEtext(self.mainWindow,0.475,0.305,0.15,0.05,'',ctip,14,'r','l')
        ctip = 'Number of structures to be randomly generated'
        self.rtrgen = mRtext(self.mainWindow,0.36,0.375,0.1,0.05,'Random gen:',ctip,14,'r','r')
        self.etrgen = mEtext(self.mainWindow,0.475,0.37,0.04,0.05,'',ctip,14,'r','l')
        ctip = 'Number of ligands connected to the metal'
        self.rcoord = mRtext(self.mainWindow,0.36,0.505,0.1,0.05,'Coordination:',ctip,14,'r','r')
        ctip = 'Metal Oxidation state'
        self.roxstate = mRtext(self.mainWindow,0.325,0.44,0.1,0.05,'Ox State:',ctip,14,'r','r')
        ctip = 'System spin state'
        self.rspstate = mRtext(self.mainWindow,0.40,0.44,0.1,0.05,'Spin:',ctip,14,'r','r')
        ctip = 'Distortion'
        self.distper = mRtext(self.mainWindow,0.4225,0.5675,0.125,0.05,'Distortion:0%','',14,'r','l')
        ctip = 'For random generation: number of different ligand types'
        self.rtlignum = mRtext(self.mainWindow,0.51,0.375,0.075,0.04,'Lig Num:',ctip,14,'r','r')
        self.etlignum = mEtext(self.mainWindow,0.585,0.37,0.04,0.05,'',ctip,14,'r','l')
        ####################################################
        ### generate edit texts for structure generation ###
        ####################################################
        self.txtgpar = mRtext(self.mainWindow,0.075,0.175,0.225,0.05,'Structure specification','',18,'r','c')
        ctip = 'Core of structure'
        self.rtcore = mRtext(self.mainWindow,0.025,0.24,0.1,0.05,'Core:',ctip,14,'r','r')
        self.etcore = mEtext(self.mainWindow,0.14,0.235,0.15,0.05,'',ctip,14,'r','l')
        # Connection atoms for core
        ctip = 'Specify connection atoms for core if using SMILES or custom cores (default: 1)'
        self.rtccat0 = mRtext(self.mainWindow,0.0325,0.28,0.1,0.05,'Core',ctip,13,'c','c')
        self.rtccat1 = mRtext(self.mainWindow,0.0325,0.30,0.1,0.05,'connections',ctip,13,'c','c')
        self.rtccat2 = mRtext(self.mainWindow,0.025,0.30,0.1,0.05,':',ctip,14,'r','r')
        self.etccat = mEtext(self.mainWindow,0.14,0.295,0.075,0.05,'',ctip,14,'r','l')
        # replace option
        ctip = 'Replace ligand at specified connection point'
        self.replig = mCheck(self.mainWindow,0.215,0.295,0.075,0.05,'replace',ctip,16)
        # specify ligands
        ctip = 'Ligand(s) to be used'
        self.rtlig = mRtext(self.mainWindow,0.025,0.36,0.1,0.05,'Ligands:',ctip,14,'r','r')
        self.etlig = mEtext(self.mainWindow,0.14,0.355,0.15,0.05,'',ctip,14,'r','l')
        ctip = 'Occurrence of corresponding ligand(s)'
        self.rtligocc = mRtext(self.mainWindow,0.025,0.42,0.1,0.05,'Lig Freq:',ctip,14,'r','r')
        self.etligocc = mEtext(self.mainWindow,0.14,0.415,0.15,0.05,'',ctip,14,'r','l')
        # force keep hydrogens
        ctip = 'Do not remove hydrogens while connecting ligand to core. default no'
        self.rtkeepHs = mRtext(self.mainWindow,0.025,0.48,0.1,0.05,'Keep Hs:',ctip,14,'r','r')
        ctip = 'Enter yes/1 or no/0 for each corresponding ligand. e.g. yes,no,yes,yes'
        self.etkeepHs = mEtext(self.mainWindow,0.14,0.475,0.15,0.05,'',ctip,14,'r','l')
        # custom M-L bond lengths (A)
        ctip = 'Custom bond length for M-L in Angstrom'
        self.rtMLb = mRtext(self.mainWindow,0.025,0.54,0.1,0.05,'M-L bonds:',ctip,14,'r','r')
        self.etMLb = mEtext(self.mainWindow,0.14,0.535,0.15,0.05,'',ctip,14,'r','l')
        # custom angles for distortion
        ctip = 'Custom angles for connection points (polar theta, azimuthal phi) in degrees separated with /. e.g 10/20 , 30/40'
        self.rtLang = mRtext(self.mainWindow,0.025,0.60,0.1,0.05,'Custom angles:',ctip,14,'r','r')
        self.etLang = mEtext(self.mainWindow,0.14,0.595,0.15,0.05,'',ctip,14,'r','l')
        # SMILES ligands denticity
        #ctip = 'Denticity of corresponding SMILES ligands (default: 1)'
        self.rtsmident = mRtext(self.mainWindow,0.025,0.72,0.1,0.05,'SMI denticity:',ctip,14,'r','r')
        self.etsmident = mEtext(self.mainWindow,0.14,0.715,0.15,0.05,'',ctip,14,'r','l')
        self.rtsmident.hide()
        self.etsmident.hide()
        # SMILES ligands connection atoms
        ctip = 'Connection atom(s) of corresponding SMILES ligands (default: 1)'
        self.rtsmicat = mRtext(self.mainWindow,0.0075,0.64,0.125,0.05,'SMILES',ctip,13,'c','c')
        self.rtsmicat = mRtext(self.mainWindow,0.0075,0.66,0.125,0.05,'connection atoms',ctip,13,'c','c')
        self.rtsmicat = mRtext(self.mainWindow,0.0,0.66,0.125,0.05,':',ctip,14,'r','r')
        self.etsmicat = mEtext(self.mainWindow,0.14,0.655,0.15,0.05,'',ctip,14,'r','l')
        # SMILES names
        ctip = 'Name of corresponding SMILES ligands (default: smi)'
        self.rtsminame = mRtext(self.mainWindow,0.0,0.72,0.125,0.05,'SMILES names:',ctip,14,'r','r')
        self.etsminame = mEtext(self.mainWindow,0.14,0.715,0.15,0.05,'',ctip,14,'r','l')
        ### generate edit texts for additional molecule
        self.txtamol = mRtext(self.mainWindow,0.725,0.175,0.2,0.05,'Additional molecule','',18,'r','c')
        self.txtamol.setDisabled(True)
        # name of binding species
        ctip = 'Binding species'
        self.rtbind = mRtext(self.mainWindow,0.675,0.25,0.1,0.05,'Molecule:',ctip,14,'r','r')
        self.etbind = mEtext(self.mainWindow,0.785,0.25,0.15,0.05,'',ctip,14,'r','l')
        self.rtbind.setDisabled(True)
        self.etbind.setDisabled(True)
        # name of binding molecule from SMILES
        ctip = 'Name of binding molecule using SMILES'
        self.rtbsmi = mRtext(self.mainWindow,0.675,0.325,0.1,0.05,'Name:',ctip,14,'r','r')
        self.etbsmi = mEtext(self.mainWindow,0.785,0.325,0.15,0.05,'',ctip,14,'r','l')
        self.rtbsmi.setDisabled(True)
        self.etbsmi.setDisabled(True)
        # number of binding conformations to generate
        ctip = 'Number of different conformations to be generated'
        self.rtnbind = mRtext(self.mainWindow,0.65,0.405,0.125,0.05,'Conformations:',ctip,14,'r','r')
        self.etnbind = mEtext(self.mainWindow,0.785,0.4,0.05,0.05,'',ctip,14,'r','l')
        self.rtnbind.setDisabled(True)
        self.etnbind.setDisabled(True)
        # charge of binding species
        ctip = 'Charge of binding species'
        self.rtchbind = mRtext(self.mainWindow,0.825,0.405,0.065,0.05,'Charge:',ctip,14,'r','r')
        self.etchbind = mEtext(self.mainWindow,0.895,0.4,0.04,0.05,'',ctip,14,'r','l')
        self.rtchbind.setDisabled(True)
        self.etchbind.setDisabled(True)
        # min/max distance
        ctip = 'Specify placing minimum/maximum distance (in A) and/or axial/equatorial orientation'
        self.rtplace = mRtext(self.mainWindow,0.65,0.48,0.125,0.05,'Distance:',ctip,14,'r','r')
        ctip = 'Minimum distance between the two molecules. 0 corresponds the marginally non-overlapping configuration'
        self.etplacemin = mEtext(self.mainWindow,0.785,0.475,0.025,0.05,'',ctip,14,'r','l')
        ctip = 'Maximum distance between the two molecules. 0 corresponds the marginally non-overlapping configuration'
        self.etplacemax = mEtext(self.mainWindow,0.81,0.475,0.025,0.05,'',ctip,14,'r','l')
        self.rtplace.setDisabled(True)
        self.etplacemin.setDisabled(True)
        self.etplacemax.setDisabled(True)
        # mask for atom/center of mass reference
        ctip = 'Reference atoms in extra molecules to be used for placement(e.g. 1,2 or 1-6 or COM or Fe) Default COM (center mass)'
        self.rtmaskbind = mRtext(self.mainWindow,0.82,0.485,0.075,0.05,'Reference:',ctip,12,'r','r')
        self.etmaskbind = mEtext(self.mainWindow,0.90,0.475,0.035,0.05,'COM',ctip,12,'r','l')
        self.rtmaskbind.setDisabled(True)
        self.etmaskbind.setDisabled(True)
        # angle/orientation
        ctip = 'Specify placement type or angle. Angle overwrites placement.'
        self.rtplacea = mRtext(self.mainWindow,0.65,0.545,0.125,0.05,'Angle:',ctip,14,'r','r')
        ctip = 'Azimouthal angle phi from 0 to 180'
        self.etplacephi = mEtext(self.mainWindow,0.785,0.54,0.04,0.05,'',ctip,14,'r','l')
        ctip = 'Polar angle theta from 0 to 360'
        self.etplacetheta = mEtext(self.mainWindow,0.825,0.54,0.04,0.05,'',ctip,14,'r','l')
        self.rtplacea.setDisabled(True)
        self.etplacephi.setDisabled(True)
        self.etplacetheta.setDisabled(True)
        ####################
        ### push buttons ###
        ####################
        # structure generation
        ctip = 'Generate structures'
        self.butGen = mButton(self.mainWindow,0.35,0.775,0.15,0.085,'Generate',ctip,18)
        self.butGen.clicked.connect(self.runGUI)
        # post-processing setup
        ctip = 'Setup post-processing'
        self.butPost = mButton(self.mainWindow,0.525,0.775,0.15,0.085,'Post-process',ctip,18)
        self.butPost.clicked.connect(self.setupp)
        # view structure
        #ctip = 'View generated structure'
        #self.butView = mButton(self.mainWindow,0.70,0.775,0.15,0.085,'View',ctip,18)
        #self.butView.clicked.connect(self.showmolBrowser)
        # quit button
        ctip = 'Quit program'
        self.butQ = mButton(self.mainWindow,0.875,0.875,0.1,0.065,'Quit',ctip,14)
        self.butQ.clicked.connect(self.mainWindow.qexitM)
        # input for QC calculation
        ctip = 'Enter input for Quantum Chemistry calculations'
        self.butQc = mButton(self.mainWindow,0.7,0.655,0.125,0.05,'Enter QC input',ctip,14)
        self.butQc.setDisabled(True)
        self.butQc.clicked.connect(self.qcinput)
        # input for jobscripts
        ctip = 'Enter input for jobscript files'
        self.butJob = mButton(self.mainWindow,0.83,0.655,0.125,0.05,'Enter job input',ctip,14)
        self.butJob.setDisabled(True)
        self.butJob.clicked.connect(self.jobenable)
        # add to database
        ctip = 'Add core/ligand/binding species to local database'
        self.butADB = mButton(self.mainWindow,0.175,0.84,0.1,0.065,'Add to local DB',ctip,12)
        self.butADB.clicked.connect(self.addDB)
        # add to database
        ctip = 'Search for ligand/binding species in chemical databases'
        self.searchDB = mButton(self.mainWindow,0.065,0.84,0.1,0.065,'Search DB',ctip,12)
        self.searchDB.clicked.connect(self.searchDBW)
        # button for browsing rundir
        ctip = 'Browse running directory'
        self.butpbrdir = mButton(self.mainWindow,0.55,0.2385,0.07,0.05,'Browse..',ctip,12)
        self.butpbrdir.clicked.connect(self.dirload)
        # view ligand
        ctip = 'Generate 2D ligand representation'
        self.butDrl = mButton(self.mainWindow,0.125,0.78,0.085,0.05,'Draw ligands',ctip,12)
        self.butDrl.clicked.connect(self.drawligs)
        ##############################
        ### generate checked boxes ###
        ##############################
        # additional molecule
        ctip = 'Place additional molecule'
        self.chkM = mCheck(self.mainWindow,0.525,0.595,0.15,0.07,'Extra molecule',ctip,14)
        self.chkM.stateChanged.connect(self.enableemol)
        # force field optimization
        ctip = 'Perform Force Field optimization'
        self.chkFF = mCheck(self.mainWindow,0.375,0.575,0.125,0.1,'FF optimize',ctip,14)
        self.chkFF.stateChanged.connect(self.enableffinput)
        # input file generation
        ctip = 'Generate input files'
        self.chkI = mCheck(self.mainWindow,0.525,0.64,0.1,0.07,'Input files',ctip,14)
        self.chkI.stateChanged.connect(self.enableqeinput)
        # jobscript generation
        ctip = 'Generate jobscripts'
        self.chkJ = mCheck(self.mainWindow,0.525,0.685,0.1,0.07,'Jobscripts',ctip,14)
        self.chkJ.stateChanged.connect(self.enablejinput)
         # charge calculation
        ctip = 'Calculate charge based on ox state and ligands'
        self.chch = mCheck(self.mainWindow,0.55,0.425,0.1,0.07,'Calc charge',ctip,14)
        self.chch.setDisabled(True)
        ########################
        ### generate sliders ###
        ########################
        # create distortion slider
        ctip = 'Percent distortion from optimal coordination'
        self.sdist = mSlider(self.mainWindow,0.525,0.5625,0.075,0.05,ctip)
        self.sdist.valueChanged.connect(self.sliderChanged)
        ###############################
        ### generate dropbdox boxes ###
        ###############################
        # ox state
        ctip = 'Metal oxidation state'
        qcav = ['0','I','II','III','IV','V','VI','VII','VIII']
        self.doxs = mDbox(self.mainWindow,0.43,0.435,0.035,0.05,qcav,ctip,14)
        self.doxs.setCurrentIndex(0)
        # spin state
        ctip = 'System spin multiplcity'
        qcav = ['1','2','3','4','5','6','7','8','9','10']
        self.dspin = mDbox(self.mainWindow,0.505,0.435,0.035,0.05,qcav,ctip,14)
        self.dspin.setCurrentIndex(0)
        # coordination
        ctip = 'Number of ligands connected to the metal'
        qcav = ['1','2','3','4','5','6','7']
        self.dcoord = mDbox(self.mainWindow,0.4875,0.5,0.05,0.05,qcav,ctip,14)
        self.dcoord.setCurrentIndex(5)
        self.dcoord.currentIndexChanged.connect(self.matchgeomcoord)
        # geometry of coordination
        ctip = 'Octahedral, Trigonal Prismatic'
        qcav = ['Oct','TPr']
        self.dcoordg = mDbox(self.mainWindow,0.5625,0.5,0.05,0.05,qcav,ctip,14)
        self.dcoordg.setCurrentIndex(0)
        # perform optimization
        ctip = 'Select Force Field'
        qcav = ['MMFF94','UFF','gchemical','GAFF']
        self.dff = mDbox(self.mainWindow,0.375,0.65,0.125,0.05,qcav,ctip,14)
        self.dff.setCurrentIndex(0)
        self.dff.setDisabled(True)
        # optimize before or after
        ctip = 'Optimize before or after building the structure'
        qcav = ['Before','After','Before & After']
        self.dffba = mDbox(self.mainWindow,0.375,0.7,0.125,0.05,qcav,ctip,14)
        self.dffba.setDisabled(True)
        self.dffba.setCurrentIndex(2)
        # select qc code
        ctip = 'Select QC code'
        qcav = ['TeraChem','GAMESS','QChem']
        self.qcode = mDbox(self.mainWindow,0.7,0.705,0.125,0.05,qcav,ctip,14)
        self.qcode.setDisabled(True)
        # select scheduler
        ctip = 'Select job scheduler'
        qcav = ['SGE','SLURM']
        self.scheduler = mDbox(self.mainWindow,0.83,0.705,0.125,0.05,qcav,ctip,14)
        self.scheduler.setDisabled(True)
        # placement of extr molecule
        ctip = 'Orientation for placing additional molecule'
        qcav = ['','axial','equatorial']
        self.dmolp = mDbox(self.mainWindow,0.8675,0.54,0.07,0.05,qcav,ctip,14)
        self.dmolp.setDisabled(True)
        ########################
        ### show main window ###
        self.mainWindow.show()
        ########################
        '''
        #############################
        ### create editor windows ###
        #############################
        '''
        self.EdWindow = mWgen(0.4,0.5,'Editor') # editor window
        '''
        #############################
        ### create pop-up windows ###
        #############################
        '''
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
        self.etcDBoutf = mEtext(self.cDBWindow,0.215,0.58,0.15,0.08,'',ctip,14,'r','l')
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
        self.butpR.clicked.connect(self.postproc)
        # button for return
        ctip = 'Return to main menu'
        self.butpret = mButton(self.pWindow,0.7125,0.7875,0.175,0.09,'Return',ctip,14)
        self.butpret.clicked.connect(self.pWindow.qexitM)
        ############################
        ### create editor window ###
        ############################
        ### editor window
        self.editor = mEdtext(self.EdWindow,0.05,0.05,0.75,0.9,'',12,'r','l')
        self.Ed = mButton(self.EdWindow,0.5,0.5,0.125,0.05,'Enter QC input',ctip,14)
        ### information window
        self.iWind = mWgen(0.5,0.4,'Log') # information window
        self.iWtxt = mEdtext(self.iWind,0.1,0.1,0.8,0.8,'Program started..',14,'n','l')
    '''
    #############################
    ### Callbacks for buttons ###
    #############################
    '''
    ##############################
    ### Local Database window ####
    ##############################
    ### load molecule from file
    def qDBload(self):
        name = QFileDialog.getOpenFileName(self.DBWindow,'Open File','.',"Molecule files *.xyz, *.mol (*.xyz *.mol)")
        if name[0] != '':
            self.etDBsmi.setText(os.path.relpath(name[0]))
    ### enable add to database interface
    def addDB(self):
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
    def postproc(self):
        rdir = self.etpdir.text()
        if rdir[-1]=='/':
            rdir = rdir[:-1]
        defaultparams = ['main.py','-i',rdir+'/postproc.inp']
        grabguivarsP(self)
        self.pWindow.close()
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
    ### close window
    def cwclose(self):
        self.lwindow.hide()
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
        self.iWind.setWindowModality(2)
        self.iWind.show()
        msgBox = QMessageBox()
        if len(args['-rgen']) > 0:
            msgBox.setText("Random generation initiated. This process might take some time.")
        #else:
            #msgBox.setText("Structure generation initiated. This process might take some time.")
        msgBox.setIcon(1)
        msgBox.setInformativeText('Please be patient. OK?')
        msgBox.setWindowTitle('Running..')
        msgBox.exec_()
        # do the generation
        emsg = startgen(defaultparams,True,self)
        if not emsg:
            QMessageBox.information(self.mainWindow,'Done','Structure generation terminated successfully!')
        else:
            QMessageBox.warning(self.mainWindow,'Problem',emsg)
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
            QMessageBox.warning(self.mainWindow,'Warning','No ligands are specified.')
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
                self.lwclose.clicked.connect(self.cwclose)
    ### def enable FF input
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
    def qloadM(self):
        name = QFileDialog.getOpenFileName(self.EdWindow,'Open File')[0]
        if name != '':
            loadfrominputfile(self,name)
    ### load directory
    def dirload(self):
        name = QFileDialog.getExistingDirectory(self.mainWindow,'Select Directory')
        if len(name) >0 and name[0] != '':
            self.etrdir.setText(name)
    ### save as input file
    def qdumpS(self,gui):
        name = QFileDialog.getSaveFileName(self.mainWindow,'Save as..','.',"Input files * (*)")[0]
        if name != '':
            varsg = grabguivars(self)
            writeinputc(varsg,name)
    ### show help menu
    def qhelpM(self):
        a = 1
    def getscreensize(self):
        screenShape = QDesktopWidget().screenGeometry()
        width = int(screenShape.width())
        height = int(screenShape.height())
        return [width,height]
    ### slider changed value
    def sliderChanged(self,val):
        self.distper.setText('Distortion: '+str(val)+'%')
    ### match index with coordination
    def matchgeomcoord(self):
        # get current index
        dc=self.dcoord.currentIndex()
        qcav = [['-'],['TPl'],['Thd','Sqp'],['TBP','SPy'],['Oct','TPr'],['PBP']]
        ctip = ['','Trigonal Planar, Pyramidal','Tetrahedral, Square Planar',
                'Square Pyramidal','Trigonal Bipyramidal','Octahedral',
                'Trigonal Prismatic', 'Pentagonal Bipyramidal']
        # empty the box
        for i in range(0,self.dcoordg.count()):
            self.dcoordg.removeItem(0)
        if dc < 2 or dc > 6:
            qc = ['-']
            ct = ''
        else:
            qc = qcav[dc-1]
            ct = ctip[dc-1]
        # add to box
        for i,t in enumerate(qc):
            self.dcoordg.insertItem(i,t)
        # set default geometry
        self.dcoordg.setCurrentIndex(0)
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
            self.rtmaskbind.setDisabled(False)
            self.etmaskbind.setDisabled(False)
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
            self.rtmaskbind.setDisabled(True)
            self.etmaskbind.setDisabled(True)
    #####################
    #### QEt/g input ####
    #####################
    ### callback for QE input
    def qcinput(self):
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

