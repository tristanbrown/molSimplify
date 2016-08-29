# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

#######################################################
########## This script parses molden files  ###########
####### and calculates various MO properties  #########
#######################################################

# import std modules
import os, sys, subprocess, time, re
# import local modules
from Scripts.postparse import *
from Classes.globalvars import *


class AtomClass:
  typ = '' # type
  ID = '0' # molden id
  nel = '0' # number of electrons
  xyz = ['0.0','0.0','0.0']
  # number of s,p,d primitives | number of s,p,d and total shells, primitives
  ns,np,nd,nf,nsc,npc,ndc,nfc,totc = (0,)*9

####################################
### get range for S,P,D orbitals ###
####################################
def getrange(idx,atoms):
    totc = 0 
    for i in range(0,idx):
        totc += (atoms[i].nsc+atoms[i].npc*3+atoms[i].ndc*6)
    totc += 1 # start index at 1 instead of 0 to compare with molden
    return [totc,totc+atoms[idx].nsc,totc+atoms[idx].nsc+atoms[idx].npc*3]

#####################################
### parse molden file and get MOs ###
#####################################
def parse(folder,molf):
    metals = ['Sc','SC','Ti','TI','V','Cr','CR','Mn','MN','Fe','FE','Co','CO','Ni','NI','Cu','CU','Zn','ZN']
    print "Parsing "+molf.split('.molden')[0]
    # get coordinates of metal
    f = open(molf,'r')
    sm = f.read().splitlines()
    f.close()
    resd = molf.rsplit('/',1)[0]
    moln = molf.rsplit('/',1)[-1]
    moln = moln.split('.molden')[0]
    if resd[0]=='.' and resd[1]=='/':
        resd = resd[2:]
    elif resd[0]=='.':
        resd == resd[1:]
    found = False
    for met in metals:
        if (found == False):
            ml = [line for line in sm if met in line]
            if len(ml)>0 and found == False :
                if 'Title' in ml[0] and len(ml)>1:
                    mlll = ml[1].split(None)
                else:
                    mlll = ml[0].split(None)
                if len(mlll) > 2:
                    found = True
                    fmet = met
    if len(ml)==0:
        print 'WARNING:No metal found, defaulting to 1st atom for relative properties..'
        skipm = True
        ml = [sm[4]]
        mlll = filter(None,ml[0].split(None))
    atidx = int(mlll[1])-1
    # INITIALIZE VARIABLES
    natoms = 0 
    # read molden file
    f=open(molf,'r')
    s=f.read()
    f.close()
    # check if TeraChem
    if 'TeraChem' in s:
        tera = True
    else:
        tera = False
    ###################################
    ####### PARSE MOLDEN FILE #########
    ###################################
    # Get atoms
    atoms = [] # Type, ID, num electrons, x, y, z
    satoms = find_between(s,'[Atoms]','[GTO]').splitlines()[1:]
    for line in satoms:
        natoms += 1
        ll = filter(None,line.split(None))
        atom = AtomClass()
        atom.typ = ll[0]
        atom.ID = ll[1]
        atom.nel = ll[2]
        atom.xyz = ll[3:]
        atoms.append(atom)
    # Parse basis set
    sgto = filter(None,find_between(s,'[GTO]','[MO]').splitlines())
    sgto.append('END') # for final termination
    cl = 1 
    ###################################
    ########### GET SHELLS  ###########
    ###################################
    totshells = 0 
    for noatom in range(0,natoms): # loop over atoms
        # skip first line
        while(True):
            l = filter(None,sgto[cl].split(None))
            if len(l) > 0:
                if (l[0]=='s' or l[0]=='S'): # get shell type
                    atoms[noatom].ns = int(l[1]) # number of primitives
                    atoms[noatom].nsc += 1 # total number of s-type shells
                    atoms[noatom].totc += 1  
                    cl += atoms[noatom].ns+1
                elif (l[0]=='p' or l[0]=='P'):
                    atoms[noatom].np = int(l[1])
                    atoms[noatom].npc += 1
                    atoms[noatom].totc += 3 # px,py,pz for each p shell
                    cl += atoms[noatom].np+1
                elif (l[0]=='d' or l[0]=='D'):
                    atoms[noatom].nd = int(l[1])
                    atoms[noatom].ndc += 1
                    cl += atoms[noatom].nd+1
                    atoms[noatom].totc += 6 # dxx,dyy,dzz,dxy,dyz,dzx for each d shell
                elif (l[0]=='f' or l[0]=='F'):
                    atoms[noatom].nf = int(l[1])
                    atoms[noatom].nfc += 1
                    cl += atoms[noatom].nf+1
                    atoms[noatom].totc += 10 # 10 orbitals f shell
                else:
                    cl += 1
                    break
            else:
                break
        totshells += atoms[noatom].totc
    ###################################
    ############ GET INFO  ############
    ###################################
    # get range of AO for atom of interest
    [sidx,pidx,didx] = getrange(atidx,atoms)
    S = [sidx,sidx+atoms[atidx].nsc-1] # range of S AOs
    P = [S[1]+1,S[1]+atoms[atidx].npc*3] # range of P AOs
    D = [P[1]+1,P[1]+atoms[atidx].ndc*6] # range of D AOs
    smos = filter(None,s.split('En')[1:])
    # loop over MOs
    txt=''
    header = 'MO   Energy  Spin Occup S-char  P-char  D-char Av-orb\n'
    eldic = {'Alpha':0,'Beta':0}
    totAocc = 0.0
    totBocc = 0.0
    coreel = 8.9 # 9 a and 9 b core electrons
    totscoeffs = 0.0
    totpcoeffs = 0.0
    totdcoeffs = 0.0
    scenter = 0.0
    pcenter = 0.0
    dcenter = 0.0
    ehomo = -999.0
    elumo = 10000.0
    e0 = 10000.0
    minoccup = [-10000.0,]*25
    minunoccup = [-10000.0,]*25
    totoccups = 0 
    avoccup = 0.0
    for i,ss in enumerate(smos) :
        lines = filter(None,ss.split('\n'))
        # remove extra MO from gamess
        if not tera:
            if '[MO]' in lines[0]:
                lines = lines[2:]
        AOs = filter(None,lines[3:])[:-1]
        occ = float(lines[2].split('=')[-1])
        en = float(lines[0].split('=')[-1])
        spin = lines[1].split('=')[-1]
        spin = spin.replace(' ','')
        eldic[spin] += 1
        coeffs = 0 
        scoeffs = 0 
        pcoeffs = 0 
        dcoeffs = 0
        if (occ > 0.0 and en > ehomo):
            ehomo = en 
        if (occ > 0.0 and en < e0):
            e0 = en 
        if (occ < 1.0 and en < elumo):
            elumo = en 
        # get min occup
        if (occ > 0.0):
            avoccup += occ
            totoccups +=1
        if (occ > 0.0 and en > minoccup[-1]):
            minoccup[0] = en
            minoccup = sorted(minoccup)
        elif (occ < 1.0 and en > minoccup[0]):
            minunoccup[-1] = en
            minunoccup = sorted(minoccup,reverse=True)
        if len(AOs) > 0 :
            if not tera:
                AOs = AOs[:-2]
            for AO in AOs:
                cof = [int(filter(None,AO.split(' '))[0]),float(filter(None,AO.split(' '))[1])]
                coeffs += cof[1]*cof[1]
                if S[0] <= cof[0] <= S[1]:
                    scoeffs += cof[1]*cof[1]
                elif P[0] <= cof[0] <= P[1]:
                    pcoeffs += cof[1]*cof[1]
                elif D[0] <= cof[0] <= D[1]:
                    dcoeffs += cof[1]*cof[1]
            if (coeffs > 0):
                scoeffs /= coeffs
                pcoeffs /= coeffs
                dcoeffs /= coeffs
            # total s coeffs in MOs
            if (scoeffs + pcoeffs + dcoeffs > 0.05 ):
                tstr = str(eldic[spin]).ljust(4)+"{0:.3f}".format(en).ljust(10)+ spin[0].lower().ljust(5) +str(int(occ)).ljust(4)
                tstr += ("{0:.1f}".format(100*scoeffs)+'%').ljust(8)+("{0:.1f}".format(100*pcoeffs)+'%').ljust(8)+("{0:.1f}".format(100*dcoeffs)+'%').ljust(8)
                tstr += ("{0:.1f}".format(avoccup/totoccups)).ljust(8)
                txt += tstr + '\n'
    outtxt = header+txt
    rsd = os.path.relpath(resd,folder)
    rsd = rsd.replace('/','_')
    f=open(folder+'/MO_files/'+rsd+'-'+moln+'_orbs.txt','w')
    f.write(outtxt)
    f.close()

#########################
### parse _orbs files ###
#########################
def parsed(orbf):
    # read results file
    f=open(orbf,'r')
    s=f.read()
    f.close()
    ############################
    ####### PARSE FILE #########
    ############################
    s = s.splitlines()[4:]
    totcoefs = 0.0
    dbandc = 0.0
    ehomo = -10000.0
    elumo = 10000.0
    ens0 = 0.0
    for line in s:
        l = filter(None, line.split(None))
        occ = int(l[3])
        en = float(l[1])
        sc = float(l[-4].split('%')[0])
        dc = float(l[-2].split('%')[0])
        avocc = float(l[-1])
        dbandc += occ*dc*en
        totcoefs += dc
        if (sc > 99.5):
            ens0 = en
        if ((occ==1 or occ==2) and en > ehomo):
            ehomo = en
        elif (occ==0 and en < elumo):
            elumo = en
    efermi = 0.5*(elumo+ehomo)
    dbandc /= totcoefs
    egap = ehomo - elumo
    return [ens0,dbandc,ehomo,elumo,efermi,egap,avocc]

##################################
### get MOs average properties ###
##################################
def getresd(dirf):
    # get results files
    resfiles=mybash("find '"+dirf+"' -name *_orbs.txt")
    resfiles=filter(None,re.split('\n',resfiles))
    txt = 'Filename                                                              e0(base)   d-band      e-homo      e-lumo      e-fermi     e-gap     [Hartree]  Av-Occup\n'
    txt += '--------------------------------------------------------------------------------------------------------------------------------------------------------------\n'
    text = []
    for resf in resfiles:
        rrfs = resf.split('_orbs')[0]
        rrfs = rrfs.replace('/MO_files','')
        rrfs = rrfs.rsplit('/',1)[-1]
        rrfs = rrfs.replace('_','/')
        rr = parsed(resf)
        text.append(rrfs.ljust(70)+"{0:.3f}".format(rr[0]).ljust(10)+"{0:.3f}".format(rr[1]).ljust(13)+
        "{0:.3f}".format(rr[2]).ljust(12)+"{0:.3f}".format(rr[3]).ljust(13)+"{0:.3f}".format(rr[4]).ljust(10)+
        "{0:.3f}".format(rr[5]).ljust(23)+"{0:.3f}".format(rr[6]).ljust(10)+'\n')
    text = sorted(text)
    f = open(dirf+'/avorbs.txt','w')
    f.write(txt+''.join(text))
    f.close()

###################################
#### Post process molden files ####
###################################
def moldpost(molf,folder,gui,flog):
    # parse each file and get MO information
    for f in molf:
        if gui:
            gui.iWtxt.setText('Processing '+f+'\n'+gui.iWtxt.toPlainText())
            gui.app.processEvents()
        flog.write('Processing '+f+'\n')
        parse(folder,f)
    # parse generated _orbs files and get summary
    getresd(folder)
