# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##############################################################
########## This script processes the input file  #############
##############################################################

# import std modules
import glob, os, re, argparse, sys
from io import *


#####################################################
########## write options to input file  #############
#####################################################
def writeinputc(args,fname):
    f = open(fname,'w')
    f.write("# Input file generated from GUI options\n")
    for key, val in args.iteritems():
        if len(val) > 0:
            vals = val.splitlines()
            for v in vals:
                f.write(key+' '+v+'\n')
    f.close()

###########################################################
########## write options to postp input file  #############
###########################################################
def writeinputp(args,fname):
    f = open(fname,'w')
    f.write("# Input file generated from GUI options\n")
    for key, val in args.iteritems():
            f.write(key+' '+val+'\n')
    f.close()
    
#####################################################
########## write options to input file  #############
#####################################################
def writeinputf(args):
    f = open(args['-rundir']+'/geninput.inp','w')
    f.write("# Input file generated from GUI options\n")
    for key, val in args.iteritems():
        if len(val) > 0:
            vals = val.splitlines()
            for v in vals:
                f.write(key+' '+v+'\n')
    f.close()

#########################################################
########## grabs GUI options to input file  #############
#########################################################
def grabguivars(gui):
    # list with arguments
    args = dict()
    ### general structure generation options ###
    args['-core'] = gui.etcore.text()
    args['-lig'] = gui.etlig.text()
    args['-ligocc'] = gui.etligocc.text()
    args['-ccatoms'] = gui.etccat.text()
    if gui.replig.getState():
        args['-replig'] = '1'
    args['-coord'] = gui.dcoord.currentText()
    args['-geometry'] = gui.dcoordg.currentText()
    args['-lignum'] = gui.etlignum.text()
    args['-MLbonds'] = gui.etMLb.text()
    args['-pangles'] = gui.etLang.text()
    args['-distort'] = str(gui.sdist.value())
    args['-rgen'] = gui.etrgen.text()
    args['-keepHs'] = gui.etkeepHs.text()
    args['-smicat'] = gui.etsmicat.text()
    args['-smident'] = gui.etsmident.text()
    args['-sminame'] = gui.etsminame.text()
    args['-oxstate'] = gui.doxs.currentText()
    args['-spin'] = gui.dspin.currentText()
    args['-rundir'] = gui.etrdir.text()
    rdir = args['-rundir']
    if rdir[1] == '/':
         args['-rundir'] = rdir[:-1]
    args['-suff'] = gui.etsuff.text()
    ### binding molecule options ###
    if gui.chkM.getState():
        args['-bind'] = gui.etbind.text()
        args['-bcharge'] = gui.etchbind.text()
        args['-nbind'] = gui.etnbind.text()
        if gui.chsep.getState():
            args['-bsep'] = 'yes'
        args['-nambsmi'] = gui.etbsmi.text()
        args['-maxd'] = gui.etplacemax.text()
        args['-mind'] = gui.etplacemin.text()
        args['-place'] = gui.dmolp.currentText()
        args['-bphi'] = gui.etplacephi.text()
        args['-btheta'] = gui.etplacetheta.text()
        args['-bref'] = gui.etmaskbind.text()
    ### force field optimization ###
    if gui.chkFF.getState():
        args['-ff'] = gui.dff.currentText()
        args['-ffoption'] = gui.dffba.currentText()
    ### Quantum Chemistry options ###
    if gui.chkI.getState():
        args['-qccode'] = gui.qcode.currentText()
        if args['-qccode'].lower() in 'terachem':
            args['-charge'] = gui.etqctch.text()
            if gui.chch.getState():
                args['-calccharge'] = 'yes'
            args['-spin'] = gui.etqctspin.text()
            args['-runtyp'] = gui.qctcalc.currentText()
            args['-method'] = gui.etqctmethod.text()
            args['-basis'] = gui.etqctbasis.text()
            args['-dispersion'] = gui.qctsel.currentText()
            args['-qoption'] = gui.qceditor.toPlainText()
        elif args['-qccode'].lower() in 'gamess':
            args['-charge'] = gui.etqcgch.text()
            if gui.chch.getState():
                args['-calccharge'] = 'yes'
            args['-spin'] = gui.etqcgspin.text()
            args['-runtyp'] = gui.qcgcalc.currentText()
            args['-method'] = gui.etqcgmethod.text()
            args['-gbasis'] = gui.etqcgbasis.text()
            args['-ngauss'] = gui.etqcngauss.text()
            args['-npfunc'] = gui.etqcnpfunc.text()
            args['-ndfunc'] = gui.etqcndfunc.text()
            args['-sysoption'] = gui.qcgedsys.toPlainText()
            args['-ctrloption'] = gui.qcgedctrl.toPlainText()
            args['-scfoption'] = gui.qcgedscf.toPlainText()
            args['-statoption'] = gui.qcgedstat.toPlainText()
        elif args['-qccode'].lower() in 'qchem':
            args['-charge'] = gui.etqcQch.text()
            if gui.chch.getState():
                args['-calccharge'] = 'yes'
            args['-spin'] = gui.etqcQspin.text()
            args['-runtyp'] = gui.qcQcalc.currentText()
            args['-basis'] = gui.etqcQbasis.text()
            args['-remoption'] = gui.qcQeditor.toPlainText()
            args['-exchange'] = gui.etqcQex.text()
            args['-correlation'] = gui.etqcQcor.text()
            if gui.chQun:
                args['-unrestricted'] = '1'
    ### jobscript options ###
    if gui.chkJ.getState():
        args['-jsched'] = gui.scheduler.currentText()
        args['-jname'] = gui.etjname.text()
        args['-memory'] = gui.etjmem.text()
        args['-wtime'] = gui.etjwallt.text()
        args['-queue'] = gui.etjqueue.text()
        args['-gpus'] = gui.etjgpus.text()
        args['-cpus'] = gui.etjcpus.text()
        args['-modules'] = gui.etjmod.text()
        args['-joption'] = gui.etjopt.toPlainText()
        args['-jcommand'] = gui.jcomm.toPlainText()
    writeinputf(args)
    return args

#########################################################
##########  grabs GUI options for terachem  #############
#########################################################
def grabguivarstc(gui):
    globs = globalvars()
    # list with arguments
    args = dict()
    args['-charge'] = gui.etqctch.text()
    args['-spin'] = gui.etqctspin.text()
    args['-runtyp'] = gui.qctcalc.currentText()
    args['-method'] = gui.etqctmethod.text()
    args['-basis'] = gui.etqctbasis.text()
    args['-dispersion'] = gui.qctsel.currentText()
    args['-qoption'] = gui.qceditor.toPlainText()
    ### write input file ###
    writeinputc(args,globs.homedir+'/.tcdefinput.inp')
    return args

######################################################
##########  grabs GUI options for GAMESS #############
######################################################
def grabguivarsgam(gui):
    globs = globalvars()
    # list with arguments
    args = dict()
    args['-charge'] = gui.etqcgch.text()
    args['-spin'] = gui.etqcgspin.text()
    args['-runtyp'] = gui.qcgcalc.currentText()
    args['-method'] = gui.etqcgmethod.text()
    args['-gbasis'] = gui.etqcgbasis.text()
    args['-ngauss'] = gui.etqcngauss.text()
    args['-npfunc'] = gui.etqcnpfunc.text()
    args['-ndfunc'] = gui.etqcndfunc.text()
    args['-sysoption'] = gui.qcgedsys.toPlainText()
    args['-ctrloption'] = gui.qcgedctrl.toPlainText()
    args['-scfoption'] = gui.qcgedscf.toPlainText()
    args['-statoption'] = gui.qcgedstat.toPlainText()
    ### write input file ###
    writeinputc(args,globs.homedir+'/.gamdefinput.inp')
    return args

#####################################################
##########  grabs GUI options for QChem #############
#####################################################
def grabguivarsqch(gui):
    globs = globalvars()
    # list with arguments
    args = dict()
    args['-charge'] = gui.etqcQch.text()
    args['-spin'] = gui.etqcQspin.text()
    args['-runtyp'] = gui.qcQcalc.currentText()
    args['-basis'] = gui.etqcQbasis.text()
    args['-remoption'] = gui.qcQeditor.toPlainText()
    args['-exchange'] = gui.etqcQex.text()
    args['-correlation'] = gui.etqcQcor.text()
    if gui.chQun:
        args['-unrestricted'] = '1'
    ### write input file ###
    writeinputc(args,globs.homedir+'/.qchdefinput.inp')
    return args

#########################################################
##########  grabs GUI options for jobscript #############
#########################################################
def grabguivarsjob(gui):
    globs = globalvars()
    # list with arguments
    args = dict()
    args['-jname'] = gui.etjname.text()
    args['-memory'] = gui.etjmem.text()
    args['-wtime'] = gui.etjwallt.text()
    args['-queue'] = gui.etjqueue.text()
    args['-gpus'] = gui.etjgpus.text()
    args['-cpus'] = gui.etjcpus.text()
    args['-modules'] = gui.etjmod.text()
    args['-joption'] = gui.etjopt.toPlainText()
    args['-jcommand'] = gui.jcomm.toPlainText()
    ### write input file ###
    writeinputc(args,globs.homedir+'/.jobdefinput.inp')
    return args

############################################################
########## grabs GUI db options to input file  #############
############################################################
def grabdbguivars(gui):
    args = dict()
    ### database search options ###
    args['-dbsim'] = gui.etcDBsmi.text()
    args['-dbcatoms'] = gui.etcDBcatoms.text()
    args['-dbresults'] = gui.etcDBnres.text()
    args['-dboutputf'] = gui.etcDBoutf.text()+gui.cDBdent.currentText()
    args['-dbbase'] = gui.cDBsel.currentText()
    args['-dbsmarts'] = gui.etcDBsmarts.text()
    args['-dbfinger'] = gui.cDBsf.currentText()
    args['-dbatoms'] = gui.etcDBsatoms0.text()+'<'+gui.etcDBsatoms1.text()
    args['-dbbonds'] = gui.etcDBsbonds0.text()+'<'+gui.etcDBsbonds1.text()
    args['-dbarbonds'] = gui.etcDBsabonds0.text()+'<'+gui.etcDBsabonds1.text()
    args['-dbsbonds'] = gui.etcDBsbondss0.text()+'<'+gui.etcDBsbondss1.text()
    args['-dbmw'] = gui.etcDBmw0.text()+'<'+gui.etcDBmw1.text()
    if len(args['-dboutputf'].replace(' ',''))==4:
        args['-dboutputf'] = ''
    ### check input
    if args['-dbatoms']=='<':
        args['-dbatoms'] = ''
    if args['-dbbonds']=='<':
        args['-dbbonds'] = ''
    if args['-dbarbonds']=='<':
        args['-dbarbonds'] = ''
    if args['-dbsbonds']=='<':
        args['-dbsbonds'] = ''
    if args['-dbmw']=='<':
        args['-dbmw'] = ''
    rdir = gui.etrdir.text()
    if rdir[-1]=='/':
        rdir = rdir[:-1]
    args['-rundir'] = rdir
    ### write input file ###
    writeinputc(args,rdir+'/dbinput.inp')
    return args
    
    
###################################################################
########## grabs GUI options to input file for postp  #############
###################################################################
def grabguivarsP(gui):
    args = dict()
    ### post-processing options ###
    args['-postp'] = ''
    args['-postdir'] = gui.etpdir.text()
    args['-postqc'] = gui.pqcode.currentText()
    rdir = args['-postdir']
    if rdir[-1]=='/':
        rdir = rdir[:-1]
    if gui.psum.getState()==1:
        args['-pres'] = ''
    if gui.pwfnav.getState()==1:
        args['-pwfninfo'] = ''
    if gui.pch.getState()==1: 
        args['-pcharge'] = ''
    if gui.pcub.getState()==1:
        args['-pgencubes'] = ''
    if gui.porbs.getState()==1: 
        args['-porbinfo'] = ''
    if gui.pdeloc.getState()==1:
        args['-pdeloc'] = ''
    if gui.pnbo.getState()==1:
        args['-pnbo'] = ''
    ### write input file ###
    writeinputp(args,rdir+'/postproc.inp')
#################################################
########### loads input file to tc  #############
#################################################
def loadfrominputtc(gui,fname):
    f = open(fname,'r')
    s = f.read()
    s = filter(None,s.splitlines())
    f.close()
    db = False
    ### general structure generation options ###
    for ss in s:
        st = ss.split(None,1)
        if '-charge'==st[0]:
            gui.etqctch.setText(st[-1])
        if 'spin'==st[0]:
            gui.etqctspin.setText(st[-1])
        if '-runtyp'==st[0]:
            gui.qctcalc.setCurrentText(st[-1])
        if '-method'==st[0]:
            gui.etqctmethod.setText(st[-1])
        if '-basis'==st[0]:
            gui.etqctbasis.setText(st[-1])
        if '-dispersion'==st[0]:
            gui.qctsel.setCurrentText(st[-1])
        if '-qoption'==st[0]:
            gui.qceditor.setText(gui.qceditor.toPlainText()+'\n'+st[-1])
        if '-charge'==st[0]:
            gui.etqctch.setText(st[-1])
        if '-spin'==st[0]:
            gui.etqctspin.setText(st[-1])
        if '-runtyp'==st[0]:
            gui.qctcalc.setCurrentText(st[-1])
#####################################################
########### loads input file to GAMESS  #############
#####################################################
def loadfrominputgam(gui,fname):
    f = open(fname,'r')
    s = f.read()
    s = filter(None,s.splitlines())
    f.close()
    db = False
    ### general structure generation options ###
    for ss in s:
        st = ss.split(None,1)
      ### Quantum Chemistry options ###
        if '-charge'==st[0]:
            gui.etqcgch.setText(st[-1])
        if '-spin'==st[0]:
            gui.etqcgspin.setText(st[-1])
        if '-runtyp'==st[0]:
            gui.qcgcalc.setCurrentText(st[-1])
        if '-method'==st[0]:
            gui.etqcgmethod.setText(st[-1])
        if '-gbasis'==st[0]:
            gui.etqcgbasis.setText(st[-1])
        if '-ngauss'==st[0]:
            gui.etqcngauss.setText(st[-1])
        if '-npfunc'==st[0]:
            gui.etqcnpfunc.setText(st[-1])
        if '-ndfunc'==st[0]:
            gui.etqcndfunc.setText(st[-1])
        if '-sysoption'==st[0]:
            gui.qcgedsys.setText(gui.qcgedsys.toPlainText()+'\n'+st[-1])
        if '-ctrloption'==st[0]:
            gui.qcgedctrl.setText(gui.qcgedctrl.toPlainText()+'\n'+st[-1])
        if '-scfoption'==st[0]:
            gui.qcgedscf.setText(gui.qcgedscf.toPlainText()+'\n'+st[-1])
        if '-statoption'==st[0]:
            gui.qcgedstat.setText(gui.qcgedstat.toPlainText()+'\n'+st[-1])
####################################################
########### loads input file to QChem  #############
####################################################
def loadfrominputqch(gui,fname):
    f = open(fname,'r')
    s = f.read()
    s = filter(None,s.splitlines())
    f.close()
    db = False
    ### general structure generation options ###
    for ss in s:
        st = ss.split(None,1)
      ### Quantum Chemistry options ###
        if '-basis'==st[0]:
            gui.etqcQbasis.setText(st[-1])
        if '-charge'==st[0]:
            gui.etqcQch.setText(st[-1])
        if '-spin'==st[0]:
            gui.etqcQspin.setText(st[-1])
        if '-runtyp'==st[0]:
            gui.qcQcalc.setCurrentText(st[-1])
        if '-remoption'==st[0]:
            gui.qcQeditor.setText(gui.qcQeditor.toPlainText()+'\n'+st[-1])
        if '-exchange'==st[0]:
            gui.etqcQex.setText(st[-1])
        if '-correlation'==st[0]:
            gui.etqcQcor.setText(st[-1])
        if '-unrestricted'==st[0]:
            gui.chQun.setChecked(True)
#########################################################
########### loads input file to jobscripts  #############
#########################################################
def loadfrominputjob(gui,fname):
    f = open(fname,'r')
    s = f.read()
    s = filter(None,s.splitlines())
    f.close()
    db = False
    ### general structure generation options ###
    for ss in s:
        st = ss.split(None,1)
        ### jobscript options ###
        if '-jname'==st[0]:
            gui.etjname.setText(st[-1])
        if '-memory'==st[0]:
            gui.etjmem.setText(st[-1])
        if '-wtime'==st[0]:
            gui.etjwallt.setText(st[-1])
        if '-queue'==st[0]:
            gui.etjqueue.setText(st[-1])
        if '-gpus'==st[0]:
            gui.etjgpus.setText(st[-1])
        if '-cpus'==st[0]:
            gui.etjcpus.setText(st[-1])
        if '-modules'==st[0]:
            gui.etjmod.setText(st[-1])
        if '-joption'==st[0]:
            gui.etjopt.setText(gui.etjopt.toPlainText()+'\n'+st[-1])
        if '-jcommand'==st[0]:
            gui.jcomm.setText(gui.jcomm.toPlainText()+'\n'+st[-1])
#################################################
########## loads input file to GUI  #############
#################################################
def loadfrominputfile(gui,fname):
    f = open(fname,'r')
    s = f.read()
    s = filter(None,s.splitlines())
    f.close()
    db = False
    ### general structure generation options ###
    for ss in s:
        st = ss.split(None,1)
        if '-lig' not in st[0]:
            st[-1] = st[-1].split('#')[0]
        if '-core'==st[0]:
            gui.etcore.setText(st[-1])
        if '-lig'==st[0]:
            gui.etlig.setText(st[-1])
        if '-ligocc'==st[0]:
            gui.etligocc.setText(st[-1])
        if '-replig'==st[0]:
            gui.replig.setChecked(True)
        if '-MLbonds'==st[0]:
            gui.etMLb.setText(st[-1])
        if '-distort'==st[0]:
            gui.sdist.setValue(int(st[-1]))
        if '-pangles'==st[0]:
            gui.etLang.setText(st[-1])
        if '-ccatoms'==st[0]:
            gui.etccat.setText(st[-1])
        if '-coord'==st[0]:
            gui.dcoord.setCurrentText(st[-1])
        if '-geometry'==st[0]:
            gui.dcoordg.setCurrentText(st[-1])
        if '-lignum'==st[0]:
                gui.etlignum.setText(st[-1])
        if '-rgen'==st[0]:
            gui.etrgen.setText(st[-1])
        if '-keepHs'==st[0]:
            gui.etkeepHs.setText(st[-1])
        if '-smicat'==st[0]:
            gui.etsmicat.setText(st[-1])
        if '-smident'==st[0]:
            gui.etsmident.setText(st[-1])
        if '-sminame'==st[0]:
            gui.etsminame.setText(st[-1])
        if '-oxstate'==st[0]:
            gui.doxs.setCurrentText(st[-1])
        if '-rundir'==st[0]:
            gui.etrdir.setText(st[-1])
        if '-suff'==st[0]:
            gui.etsuff.setText(st[-1])
        ### binding molecule options ###
        if '-bind'==st[0]:
            gui.chkM.setChecked(True)
            gui.enableemol()
            gui.etbind.setText(st[-1])
        if '-bsep'==st[0]:
            gui.chsep.setChecked(True)
        if '-bcharge'==st[0]:
            gui.etchbind.setText(st[-1])
        if '-nbind'==st[0]:
            gui.etnbind.setText(st[-1])
        if '-nambsmi'==st[0]:
            gui.etbsmi.setText(st[-1])
        if '-maxd'==st[0]:
            gui.etplacemax.setText(st[-1])
        if '-mind'==st[0]:
            gui.etplacemin.setText(st[-1])
        if '-place'==st[0]:
            gui.dmolp.setCurrentText(st[-1])
        if '-bphi'==st[0]:
            gui.etplacephi.setText(st[-1])
        if '-btheta'==st[0]:
            gui.etplacetheta.setText(st[-1])
        if '-bref'==st[0]:
            gui.etmaskbind.setText(st[-1])
        ### force field optimization ###
        ff = False
        if '-ff'==st[0]:
            gui.chkFF.setChecked(True)
            gui.enableffinput()
            gui.dff.setCurrentText(st[-1])
            ff = True
        if '-ffoption'==st[0]:
            sopt = st[-1].split('&')
            b,a,e = False,False,False
            for sopts in sopt:
                ssopt = sopts.replace(' ','')
                if ssopt[0].lower()=='b':
                    b = True
                elif ssopt[0].lower()=='a':
                    a = True
            if b and not a:
                idx = 0
            elif not b and a:
                idx = 1
            elif b and a:
                idx = 2
            else:
                idx = 2
            gui.dffba.setCurrentIndex(idx)
        ### Quantum Chemistry options ###
        if '-qccode'==st[0]:
            gui.chkI.setChecked(True)
            gui.enableqeinput()
            gui.qcode.setCurrentText(st[-1])
        if '-calccharge'==st[0]:
            gui.chch.setChecked(True)
        if '-basis'==st[0]:
            gui.etqctbasis.setText(st[-1])
            gui.etqcQbasis.setText(st[-1])
        if '-dispersion'==st[0]:
            gui.qctsel.setCurrentText(st[-1])
        if '-qoption'==st[0]:
            gui.qceditor.setText(gui.qceditor.toPlainText()+'\n'+st[-1])
        if '-charge'==st[0]:
            gui.etqcgch.setText(st[-1])
            gui.etqctch.setText(st[-1])
            gui.etqcQch.setText(st[-1])
        if '-spin'==st[0]:
            gui.etqcgspin.setText(st[-1])
            gui.etqctspin.setText(st[-1])
            gui.etqcQspin.setText(st[-1])
        if '-runtyp'==st[0]:
            gui.qcgcalc.setCurrentText(st[-1])
            gui.qctcalc.setCurrentText(st[-1])
            gui.qcQcalc.setCurrentText(st[-1])
        if '-method'==st[0]:
            gui.etqctmethod.setText(st[-1])
            gui.etqcgmethod.setText(st[-1])
        if '-gbasis'==st[0]:
            gui.etqcgbasis.setText(st[-1])
        if '-ngauss'==st[0]:
            gui.etqcngauss.setText(st[-1])
        if '-npfunc'==st[0]:
            gui.etqcnpfunc.setText(st[-1])
        if '-ndfunc'==st[0]:
            gui.etqcndfunc.setText(st[-1])
        if '-sysoption'==st[0]:
            gui.qcgedsys.setText(gui.qcgedsys.toPlainText()+'\n'+st[-1])
        if '-ctrloption'==st[0]:
            gui.qcgedctrl.setText(gui.qcgedctrl.toPlainText()+'\n'+st[-1])
        if '-scfoption'==st[0]:
            gui.qcgedscf.setText(gui.qcgedscf.toPlainText()+'\n'+st[-1])
        if '-statoption'==st[0]:
            gui.qcgedstat.setText(gui.qcgedstat.toPlainText()+'\n'+st[-1])
        if '-remoption'==st[0]:
            gui.qcQeditor.setText(gui.qcQeditor.toPlainText()+'\n'+st[-1])
        if '-exchange'==st[0]:
            gui.etqcQex.setText(st[-1])
        if '-correlation'==st[0]:
            gui.etqcQcor.setText(st[-1])
        if '-unrestricted'==st[0]:
            gui.chQun.setChecked(True)
        ### jobscript options ###
        if '-jsched'==st[0]:
            gui.chkJ.setChecked(True)
            gui.enableqeinput()
            gui.scheduler.setCurrentText(st[-1])
        if '-jname'==st[0]:
            gui.etjname.setText(st[-1])
        if '-memory'==st[0]:
            gui.etjmem.setText(st[-1])
        if '-wtime'==st[0]:
            gui.etjwallt.setText(st[-1])
        if '-queue'==st[0]:
            gui.etjqueue.setText(st[-1])
        if '-gpus'==st[0]:
            gui.etjgpus.setText(st[-1])
        if '-cpus'==st[0]:
            gui.etjcpus.setText(st[-1])
        if '-modules'==st[0]:
            gui.etjmod.setText(st[-1])
        if '-joption'==st[0]:
            gui.etjopt.setText(gui.etjopt.toPlainText()+'\n'+st[-1])
        if '-jcommand'==st[0]:
            gui.jcomm.setText(gui.jcomm.toPlainText()+'\n'+st[-1])
        ### database search options ###
        if '-dbsim'==st[0]:
            gui.etcDBsmi.setText(st[-1])
            db = True
        if '-dbcatoms'==st[0]:
            gui.etcDBcatoms.setText(st[-1])
        if '-dbresults'==st[0]:
            gui.etcDBnres.setText(st[-1])
            db = True
        if '-dboutputf'==st[0]:
            ssp = st[-1].split('.')
            gui.etcDBoutf.setText(ssp[0])
            gui.cDBdent.setCurrentText('.'+ssp[-1])
        if '-dbbase'==st[0]:
            gui.cDBsel.setCurrentText(st[-1])
            db = True
        if '-dbsmarts'==st[0]:
            gui.etcDBsmarts.setText(st[-1])
        if '-dbfinger'==st[0]:
            gui.cDBsf.setCurrentText(st[-1])
        if '-dbatoms'==st[0]:
            ssp = st[-1].split('<')
            gui.etcDBsatoms0.setText(ssp[0])
            gui.etcDBsatoms1.setText(ssp[-1])
        if '-dbbonds'==st[0]:
            ssp = st[-1].split('<')
            gui.etcDBsbonds0.setText(ssp[0])
            gui.etcDBsbonds1.setText(ssp[-1])
        if '-dbarbonds'==st[0]:
            ssp = st[-1].split('<')
            gui.etcDBsabonds0.setText(ssp[0])
            gui.etcDBsabonds1.setText(ssp[-1])
        if '-dbsbonds'==st[0]:
            ssp = st[-1].split('<')
            gui.etcDBsbondss0.setText(ssp[0])
            gui.etcDBsbondss1.setText(ssp[-1])
        if '-dbmw'==st[0]:
            ssp = st[-1].split('<')
            gui.etcDBmw0.setText(ssp[0])
            gui.etcDBmw1.setText(ssp[-1])
    if db:
        gui.searchDBW()
