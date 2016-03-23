# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##########################################################
########## This script handles input/output  #############
##########################################################

# import std modules
import pybel, glob, os, re, argparse, sys
from Classes.mol3D import *

##############################################
### function to print available geometries ###
##############################################
def getgeoms():
    geomnames = ['none','linear','trigonal planar','tetrahedral','square planar',
                'trigonal bipyramidal','square pyramidal','octahedral', 
                'trigonal prismatic','pentagonal bipyramidal']
    geomshorts = ['one','li','tpl','thd','sqp','tbp','spy','oct','tpr','pbp']
    coords = [1,2,3,3,4,4,5,5,6,6,7]
    for i,g in enumerate(geomnames):
        print "Coordination: %d, geometry: %s,\t short name: %s " %(coords[i],g,geomshorts[i])
    print ''

###################################
### function to read dictionary ###
###################################
def readdict(fname):
    d = dict()
    f = open(fname,'r')
    txt = f.read()
    lines = filter(None,txt.splitlines())
    f.close()
    for line in lines:
        if (line[0]!='#'):
            key = filter(None,line.split(':')[0])
            val = filter(None,line.split(':')[1])
            d[key] = filter(None,re.split(',| ',val))
    return d 

##############################
### get ligands dictionary ###
##############################
def getligs(installdir):
    licores = readdict(installdir+'Ligands/ligands.dict')
    a=[]
    for key in licores:
        a.append(key)
    a = sorted(a)
    a = ' '.join(a)
    return a

###################################
### put [] on metals for SMILES ###
###################################
def checkTMsmiles(smi):
    g = globalvars()
    for m in g.metals():
        if m in smi:
            smi = smi.replace(m,'['+m+']')
    return smi


##############################
### get ligands dictionary ###
##############################
def getbinds(installdir):
    bindcores = readdict(installdir+'Bind/bind.dict')
    a=[]
    for key in bindcores:
        a.append(key)
    a = sorted(a)
    a = ' '.join(a)
    return a

############################
### get cores dictionary ###
############################
def getcores(installdir):
    mcores = readdict(installdir+'Cores/cores.dict')
    a=[]
    for key in mcores:
            a.append(key)
    a = sorted(a)
    a = ' '.join(a)
    return a

#######################
### load bonds data ###
#######################
def loaddata(fname):
    # loads ML data from ML.dat file and
    # store to dictionary
    d = dict()
    f = open(fname)
    txt = f.read()
    lines = filter(None,txt.splitlines())
    for line in lines[1:]:
        if '#'!=line[0]: # skip comments
            l = filter(None,line.split(None))
            d[(l[0],l[1],l[2],l[3],l[4])] = l[5] # read dictionary
    f.close()
    return d

###########################
###    load backbone    ###
###########################
def loadcoord(installdir,coord):
    f = open(installdir+'Data/'+coord+'.dat')
    txt = filter(None,f.read().splitlines())
    f.close()
    b = []
    for line in txt:
        l = filter(None,line.split(None))
        b.append([float(l[0]),float(l[1]),float(l[2])])
    return b
    
###########################
###    load core and    ###
### convert to molecule ###
###########################
def core_load(installdir,usercore,mcores):
    if '~' in usercore:
        homedir = os.path.expanduser("~")
        usercore = usercore.replace('~',homedir)
    emsg = False
    core = mol3D() # initialize core molecule
    ### check if core exists in dictionary
    if usercore in mcores:
        # load core mol file (with hydrogens)
        fcore = installdir+'Cores/'+mcores[usercore][0]
        # check if core xyz/mol file exists
        if not glob.glob(fcore):
            emsg ="We can't find the core structure file %s right now! Something is amiss. Exiting..\n" % fcore
            print emsg
            return False,emsg
        if ('.xyz' in fcore):
            core.OBmol = core.getOBmol(fcore,'xyzf')
        elif ('.mol' in fcore):
            core.OBmol = core.getOBmol(fcore,'molf')
        elif ('.smi' in fcore):
            core.OBmol = core.getOBmol(fcore,'smif')
            core.OBmol.make3D('mmff94',0) # generate 3D coords
        core.cat = [int(l) for l in filter(None,mcores[usercore][1:])]
        core.denticity = mcores[usercore][-1]
        core.ident = mcores[usercore][0].split('.')[0]
    ### load from file
    elif ('.mol' in usercore or '.xyz' in usercore or '.smi' in usercore):
        if glob.glob(usercore):
            ftype = usercore.split('.')[-1]
            # try and catch error if conversion doesn't work
            try:
                core.OBmol = core.getOBmol(usercore,ftype+'f') # convert from file
                if 'smi' in usercore:
                    core.OBmol.make3D('mmff94',0)
            except IOError:
                emsg = 'Failed converting file ' +usercore+' to molecule..Check your file.\n'
                print emsg
                return False,emsg
            core.ident = usercore.split('.')[0]
            core.ident = core.ident.rsplit('/')[-1]
        else:
            emsg = 'Core file '+usercore+' does not exist. Exiting..\n'
            print emsg
            return False,emsg
    ### if not, try converting from SMILES
    else:
        # check for transition metals
        usercore = checkTMsmiles(usercore)
        # try and catch error if conversion doesn't work
        try:
            core.OBmol = core.getOBmol(usercore,'smi') # convert from smiles
            core.OBmol.make3D('mmff94',0) # add hydrogens and coordinates
        except IOError:
            emsg = "We tried converting the string '%s' to a molecule but it wasn't a valid SMILES string.\n" % usercore
            emsg += "Furthermore, we couldn't find the core structure: '%s' in the cores dictionary. Try again!\n" % usercore
            emsg += "\nAvailable cores are: %s\n" % getcores(installdir)
            print emsg
            return False,emsg
        core.cat = [0]
        core.denticity = 1
        core.ident = 'core'
    return core,emsg
    
###########################
###   load ligand and   ###
### convert to molecule ###
###########################
def lig_load(installdir,userligand,licores):
    if '~' in userligand:
        homedir = os.path.expanduser("~")
        userligand = userligand.replace('~',homedir)
    emsg = False
    lig = mol3D() # initialize ligand molecule
    ### check if ligand exists in dictionary
    if userligand in licores:
        # load lig mol file (with hydrogens)
        flig = installdir+'Ligands/'+licores[userligand][0]
        # check if ligand xyz/mol file exists
        if not glob.glob(flig):
            emsg = "We can't find the ligand structure file %s right now! Something is amiss. Exiting..\n" % flig
            print emsg
            return False, emsg
        if ('.xyz' in flig):
            lig.OBmol = lig.getOBmol(flig,'xyzf')
        elif ('.mol' in flig):
            lig.OBmol = lig.getOBmol(flig,'molf')
        elif ('.smi' in flig):
            lig.OBmol = lig.getOBmol(flig,'smif')
            lig.OBmol.make3D('mmff94',0) # generate 3D coords
        lig.cat = [int(l) for l in licores[userligand][2:]]
        lig.denticity = len(licores[userligand][2:])
        lig.ident = licores[userligand][1]
        lig.charge = lig.OBmol.charge
        ### load from file
    elif ('.mol' in userligand or '.xyz' in userligand or '.smi' in userligand or '.sdf' in userligand):
        if glob.glob(userligand):
            ftype = userligand.split('.')[-1]
            # try and catch error if conversion doesn't work
            try:
                lig.OBmol = lig.getOBmol(userligand,ftype+'f') # convert from smiles
                if 'smi' not in userligand:
                    lig.OBmol.make3D('mmff94',0) # add hydrogens and coordinates
                lig.charge = lig.OBmol.charge
            except IOError:
                emsg = 'Failed converting file ' +userligand+' to molecule..Check your file.\n'
                return False,emsg
            lig.ident = userligand.rsplit('/')[-1]
            lig.ident = lig.ident.split('.'+ftype)[0]
        else:
            emsg = 'Ligand file '+userligand+' does not exist. Exiting..\n'
            return False,emsg
    ### if not, try converting from SMILES
    else:
        # check for transition metals
        userligand = checkTMsmiles(userligand)
        # try and catch error if conversion doesn't work
        try:
            lig.OBmol = lig.getOBmol(userligand,'smi') # convert from smiles
            lig.OBmol.make3D('mmff94',0) # add hydrogens and coordinates
            lig.charge = lig.OBmol.charge
        except IOError:
            emsg = "We tried converting the string '%s' to a molecule but it wasn't a valid SMILES string.\n" % userligand
            emsg += "Furthermore, we couldn't find the ligand structure: '%s' in the ligands dictionary. Try again!\n" % userligand
            emsg += "\nAvailable ligands are: %s\n" % getligs(installdir)
            print emsg
            return False,emsg
        lig.cat = [0]
        lig.denticity = 1
        lig.ident = 'smi'        
    return lig,emsg

####################################
###   load binding species and   ###
#####   convert to molecule    #####
####################################
def bind_load(installdir,userbind,bindcores):
    if '~' in userbind:
        homedir = os.path.expanduser("~")
        userbind = userbind.replace('~',homedir)
    emsg = False
    bind = mol3D() # initialize binding molecule
    bsmi = False # flag for smiles
    ### check if binding molecule exists in dictionary
    if userbind in bindcores:
        # load bind mol file (with hydrogens)
        fbind = installdir+'Bind/'+bindcores[userbind][0]
        # check if bind xyz/mol file exists
        if not glob.glob(fbind):
            emsg = "We can't find the binding species structure file %s right now! Something is amiss. Exiting..\n" % fbind
            print emsg
            return False,False,emsg
        if ('.xyz' in fbind):
            bind.OBmol = bind.getOBmol(fbind,'xyzf')
        elif ('.mol' in fbind):
            bind.OBmol = bind.getOBmol(fbind,'molf')
        elif ('.smi' in fbind):
            bind.OBmol = core.getOBmol(fcore,'smif')
        bind.charge = bind.OBmol.charge
    ### load from file
    elif ('.mol' in userbind or '.xyz' in userbind or '.smi' in userbind):
        if glob.glob(userbind):
            ftype = userbind.split('.')[-1]
            # try and catch error if conversion doesn't work
            try:
                bind.OBmol = bind.getOBmol(userbind,ftype+'f') # convert from file
                bind.OBmol.make3D('mmff94',0) # add hydrogens and coordinates
                bind.charge = bind.OBmol.charge
            except IOError:
                emsg = 'Failed converting file ' +userbind+' to molecule..Check your file.\n'
                return False,emsg
        else:
            emsg = 'Binding species file '+userbind+' does not exist. Exiting..\n'
            return False,emsg
    ### if not, try converting from SMILES
    else:
        # check for transition metals
        userbind = checkTMsmiles(userbind)
        # try and catch error if conversion doesn't work
        try:
            bind.OBmol = bind.getOBmol(userbind,'smi') # convert from smiles
            bind.OBmol.make3D('mmff94',0) # add hydrogens and coordinates
            bind.charge = bind.OBmol.charge
            bsmi = True
        except IOError:
            emsg = "We tried converting the string '%s' to a molecule but it wasn't a valid SMILES string.\n" % userbind
            emsg += "Furthermore, we couldn't find the binding species structure: '%s' in the binding species dictionary. Try again!\n" % userbind
            print emsg
            return False,False,emsg
    return bind, bsmi, emsg


