# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

#####################################################
######## This script interacts with mutiwfn  ########
###########  and postprocess results. ###############
#####################################################

# import custom modules
from Classes.globalvars import *
from Scripts.postparse import *
from Scripts.postmold import *
from Scripts.postmwfn import *
# import std modules
import os, sys, glob, subprocess, time, math, shutil

########################################
### module for running bash commands ###
########################################
def mybash(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)        
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)


######################
### check multiwfn ###
######################
def checkmultiwfn(mdir):
    if not glob.glob(mdir):
        return False
    else:
        return True

####################################
#### Main postprocessing driver ####
####################################
def postproc(rundir,args,globs):
    globs = globalvars()
    if args.gui:
        from Classes.qBox import qBoxInfo
        from Classes.qBox import qBoxError
        from Classes.mWindow import mWgen
        from Classes.mText import mRtext
        from Classes.mText import mEdtext
        args.gui.pwind = mWgen(0.5,0.4,'Log') # information window
        args.gui.mEd = mEdtext(args.gui.pwind,0.1,0.1,0.8,0.8,'Post-processing started..',12,'n','c')
        args.gui.pwind.setWindowModality(2)
        args.gui.pwind.show()
        choice = qBoxInfo(args.gui.pWindow,'Post processing','Parsing the results will take a while..Please be patient. Start?')
    # locate output files
    pdir = args.postdir if args.postdir else globs.rundir
    cmd = "find . -name *out"
    logfile = pdir+'/post.log'
    flog = open(logfile,'a')
    flog.write('\n\n\n##### Date: '+time.strftime('%m/%d/%Y %H:%M')+'#####\n\n')
    t = mybash(cmd)
    resf = t.splitlines()
    # run summary report
    if args.pres:
        print '\nGetting runs summary..\n\n'
        flog.write('\nGetting runs summary..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nGetting runs summary..\n\n'+args.gui.mEd.toPlainText())
        terapost(resf,pdir,args.gui,flog)
        gampost(resf,pdir,args.gui,flog)
    # run nbo analysis
    if args.pnbo:
        print '\nGetting NBO summary..\n\n'
        flog.write('\nGetting NBO summary..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nGetting NBO summary..\n\n'+args.gui.mEd.toPlainText())
        nbopost(resf,pdir,args.gui,flog)
    # locate molden files
    cmd = "find . -name *molden"
    t = mybash(cmd)
    molf = t.splitlines()
    # parse molecular orbitals
    if args.porbinfo:
        print '\nGetting MO information..\n\n'
        flog.write('\nGetting MO information..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nGetting MO information..\n\n'+args.gui.mEd.toPlainText())
        if not os.path.isdir(pdir+'/MO_files'):
            os.mkdir(pdir+'/MO_files')
        moldpost(molf,pdir,args.gui,flog)
    # calculate delocalization indices
    if args.pdeloc:
        print '\nCalculating delocalization indices..\n\n'
        flog.write('\nCalculating delocalization indices..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nCalculating delocalization indices..\n\n'+args.gui.mEd.toPlainText())
        if not os.path.isdir(pdir+'/Deloc_files'):
            os.mkdir(pdir+'/Deloc_files')
        deloc(molf,pdir,args.gui,flog)
    # calculate charges
    if args.pcharge:
        print '\nCalculating charges..\n\n'
        flog.write('\nCalculating charges..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nCalculating charges..\n\n'+args.gui.mEd.toPlainText())
        if not os.path.isdir(pdir+'/Charge_files'):
            os.mkdir(pdir+'/Charge_files')
        getcharges(molf,pdir,args.gui,flog)
    # parse wavefunction
    if args.pwfninfo:
        print '\nCalculating wavefunction properties..\n\n'
        flog.write('\nCalculating wavefunction properties..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nCalculating wavefunction properties..\n\n'+args.gui.mEd.toPlainText())
        if not os.path.isdir(pdir+'/Wfn_files'):
            os.mkdir(pdir+'/Wfn_files')
        if not os.path.isdir(pdir+'/Cube_files'):
            os.mkdir(pdir+'/Cube_files')
        getcubes(molf,pdir,args.gui,flog)
        getwfnprops(molf,pdir,args.gui,flog)
        if not args.pgencubes and os.path.isdir(pdir+'/Cube_files'):
            shutil.rmtree(pdir+'/Cube_files')
    # generate cube files
    if args.pgencubes:
        print '\nGenerating cube files..\n\n'
        flog.write('\nGenerating cube files..\n\n')
        if args.gui:
            args.gui.mEd.setText('\nGenerating cube files..\n\n'+args.gui.mEd.toPlainText())
        if not os.path.isdir(pdir+'/Cube_files'):
            os.mkdir(pdir+'/Cube_files')
        getcubes(molf,pdir,args.gui,flog)
    flog.close()
