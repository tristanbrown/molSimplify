# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##########################################################
######## This script generates a collection  #############
#####  of randomly placed binding species around   #######
########   a functionalized ferrocene core   #############
######## and then creates the required input #############
######## and job files for running terachem  #############
########  calculations on these structures   #############
##########################################################

# import custom modules
from geometry import *
from io import *
from Classes.globalvars import *
# import standard modules
import os, sys
import pybel, openbabel, random, itertools
from numpy import log, arccos, cross, dot, pi

######################
### Euclidean norm ###
######################
def norm(u):
    # INPUT
    #   - u: n-element list
    # OUTPUT
    #   - d: Euclidean norm
    d = 0.0
    for u0 in u:
        d += (u0*u0)
    d = sqrt(d)
    return d
    
################################################
### gets the elements in a that are not in b ###
################################################
def setdiff(a,b):
    # INPUT
    #   - a: list with elements
    #   - b: list with elements
    # OUTPUT
    #   - aa: elements in a that are not in b
    b = set(b)
    return [aa for aa in a if aa not in b]

##########################################
#### gets all possible combinations   ####
#### for connection atoms in geometry ####
##########################################
def getbackbcombs():
    bbcombs = dict()
    bbcombs['one'] = [[1]]
    bbcombs['li'] = [[1],[2]]
    bbcombs['oct'] = [[1,2,3,4,5,6], # 6-dentate
                     [1,2,3,4,5],[1,2,3,4,6],[1,2,3,5,6],[1,2,4,5,6], # 5-dentate
                     [1,3,4,5,6],[2,3,4,5,6], # 5-dentate
                     [1,2,3,5],[2,4,5,6],[1,3,4,6], # 4-dentate
                     [1,2,3],[5,1,2],[1,4,3],[1,5,3],[1,6,3],[4,1,6], # 3-dentate
                     [2,3,5],[2,4,5],[4,2,6],[2,6,5],[4,3,6],[4,5,6], # 3-dentate
                     [1,2],[1,4],[1,5],[1,6],[2,3],[2,4], # 2-dentate
                     [2,6],[3,4],[3,5],[3,6],[4,5],[5,6], # 2-dentate
                     [1],[2],[3],[4],[5],[6]] # 1-dentate 
    bbcombs['pbp'] = [[1,2,3,4,5,6],[1,2,3,4,6], # 6/5-dentate
                      [1,2,3,5], # 4-dentate
                      [1,2,3],[1,2,4],[2,1,5],[3,1,6],[5,6,3],[2,6,5], # 3-dentate
                      [1,2],[2,3],[3,4],[4,5],[1,7],[2,6],[5,7],[3,6], # 2-dentate
                      [1],[2],[3],[4],[5],[6],[7]] # 1-dentate
    bbcombs['spy'] = [[1,2,3,4,5],[1,4,2,3],[1,4,2],[4,2,3],[2,3,1],[3,1,4],
                     [1,4],[4,2],[2,3],[3,1],[4,5],[2,5],[3,5],[1,5],[1],[2],[3],[4],[5]]
    bbcombs['sqp'] = [[1,4,2,3],[1,4,2],[4,2,3],[2,3,1],[3,1,4],[1,4],[4,2],[2,3],[3,1],
                      [1],[2],[3],[4]]
    bbcombs['tbp'] = [[1,2,3,4,5],[1,3,4,5],[3,2,4],[4,5,3],[5,1,3],[4,5],[5,3],[3,4],
                     [1,4],[1,5],[1,3],[2,4],[2,5],[2,3],[1],[2],[3],[4],[5]]
    bbcombs['thd'] = [[1,2,3,4],[3,2,4],[2,4,1],[4,1,3],[2,4],[4,3],[3,2],[1,3],[1,4],[2,4],[1],[2],[3],[4]]
    bbcombs['tpl'] = [[1,3,4],[1,2],[2,3],[1,3],[1],[2],[3]]
    bbcombs['tpr'] = [[1,2,3,4,5,6],[1,2,3,4,5],[1,2,5,4],[5,2,3,6],[1,4,6,3],[1,2,3],[3,6,5],
                     [2,3],[2,5],[5,6],[6,4],[4,1],[1],[2],[3],[4],[5],[6]]
    return bbcombs

#########################################
### gets a combination that satisfies ###
#### denticity and updates dictionary ###
#########################################
def getnupdateb(backbatoms,denticity):
    dlist = []
    batoms = []
    # find matching combination
    for b in backbatoms:
        if len(b)==denticity:
            batoms = b
            break
    # loop and find elements to delete
    for b in batoms:
        for i,bcomb in enumerate(backbatoms):
            if b in bcomb and i not in dlist:
                dlist.append(i)
    dlist.sort(reverse=True) # sort
    # delete used points
    for i in dlist:
        del backbatoms[i]
    if len(batoms) < 1:
        print 'No more connecting points available..'
    return batoms,backbatoms

##############################################
### gets connection atoms of smiles string ###
##############################################
def getsmilescat(args,indsmi):
    # INPUT
    #   - args: placeholder for input arguments
    #   - nosmiles: number of ligands defined via SMILES
    #   - indsmi: index of SMILES string ligand (like counter)
    # OUTPUT
    #   - tt: list of connection atoms
    tt= []  # initialize list of connection atoms
    if args.smicat and args.smident: # get connection atom(s)
        if len(args.smident) > indsmi: # check if smident entry exists
            # get starting index in smicat
            tsmiidx = 0
            for iloop in range(0,indsmi):
                tsmiidx += int(args.smident[iloop])
            # if smicat entry exists for smiles grab the numbers
            if len(args.smicat) >= tsmiidx+int(args.smident[indsmi]): 
                for iloop in range(0,int(args.smident[indsmi])):
                    tt.append(int(args.smicat[tsmiidx+iloop]))
            else:
            # lse just get sequential numbers 0,1,2.. until smident
                for iloop in range(0,int(args.smident[indsmi])): # default 0,1,2..
                    tt.append(iloop)
        else:
            tt = [0] # default value
    elif args.smident and len(args.smident) > indsmi: # if no smicat exists
        for iloop in range(0,int(args.smident[indsmi])): # default 0,1,2..
            tt.append(iloop)
    elif args.smicat: # in order of smicat if only 1 SMILES
        for t in args.smicat:
            tt.append(int(t))
    else:
        tt = [0] # default value 0 connection atom
    return tt

#######################################
### gets denticity of smiles string ###
#######################################
def getsmident(args,indsmi):
    # INPUT
    #   - args: placeholder for input arguments
    #   - nosmiles: number of ligands defined via SMILES
    #   - indsmi: index of SMILES string ligand (like counter)
    # OUTPUT
    #   - SMILES ligand denticity (int)
    ### check for denticity specification in input ###
    # if denticity is specified return this
    if args.smident and len(args.smident) > indsmi:
        return int(args.smident[indsmi])
    elif args.smicat:
        return int(len(args.smicat))
    # otherwise return default
    else:
        return 1

##############################################
### modifies backbone according to langles ###
##############################################
def modifybackbonel(backb, langles):
    # INPUT
    #   - backb: list with points comprising the backbone
    #   - langles: angles for distorting backbone points corresponding to ligands (pairs of theta/phi)
    # OUTPUT
    #   - backb: list with modified points comprising the backbone
    for i,ll in enumerate(langles):
        if ll:
            theta = float(ll.split('/')[0])/180.0
            phi = float(ll.split('/')[-1])/180.0
            backb[i+1] = PointTranslateSph(backb[0],backb[i+1],[distance(backb[0],backb[i+1]),theta,phi])
    return backb
    
##############################################
### modifies backbone according to pangles ###
##############################################
def modifybackbonep(backb, pangles):
    # INPUT
    #   - backb: list with points comprising the backbone
    #   - pangles: angles for distorting corresponding backbone points  (pairs of theta/phi)
    # OUTPUT
    #   - backb: list with modified points comprising the backbone
    for i,ll in enumerate(pangles):
        theta = float(ll.split('/')[0])/180.0
        phi = float(ll.split('/')[-1])/180.0
        backb[i+1] = PointTranslateSph(backb[0],backb[i+1],[distance(backb[0],backb[i+1]),theta,phi])
    return backb

##################################
### randomly distorts backbone ###
##################################
def distortbackbone(backb, distort):
    # INPUT
    #   - backb: list with points comprising the backbone
    #   - distort: % distortion of the backbone
    # OUTPUT
    #   - backb: list with modified points comprising the backbone
    for i in range(1,len(backb)):
            theta = random.uniform(0.0,0.01*int(distort)) # *0.5
            phi = random.uniform(0.0,0.01*int(distort)*0.5) # *0.5
            backb[i] = PointTranslateSph(backb[0],backb[i],[distance(backb[0],backb[i]),theta,phi])
    return backb

###########################################
### loads M-L bond length from database ###
###########################################
def getbondlength(args,metal,m3D,lig3D,matom,atom0,ligand,MLbonds):
    # INPUT
    #   - args: palceholder for input arguments
    #   - metal: name for metallic element
    #   - m3D: mol3D with main complex
    #   - lig3D: mol3D with ligand
    #   - matom: index of metal atom in m3D
    #   - atom0: index of connecting atom in lig3D
    #   - ligand: name of ligand
    #   - MLbonds: data from database
    # OUTPUT
    #   - bondl: bond length in A
    ### check for roman letters in oxstate
    romans={'I':'1','II':'2','III':'3','IV':'4','V':'5','VI':'6'}
    if args.oxstate: # if defined put oxstate in keys
        if args.oxstate in romans.keys():
            oxs = romans[args.oxstate]
        else:
            oxs = args.oxstate
    else:
        oxs = '-'
    # check for spin multiplicity
    spin = args.spin if args.spin else '-'
    key = []
    key.append((metal,oxs,spin,lig3D.getAtom(atom0).sym,ligand))
    key.append((metal,oxs,spin,lig3D.getAtom(atom0).sym,'-')) # disregard exact ligand
    key.append((metal,'-','-',lig3D.getAtom(atom0).sym,ligand)) # disregard oxstate/spin
    key.append((metal,'-','-',lig3D.getAtom(atom0).sym,'-')) # else just consider bonding atom
    found = False
    # search for data
    for kk in key:
        if (kk in MLbonds.keys()): # if exact key in dictionary
            bondl = float(MLbonds[kk])
            found = True
            break
    if not found: # last resort covalent radii
        bondl = m3D.getAtom(matom).rad + lig3D.getAtom(atom0).rad
    return bondl

###############################
### FORCE FIELD OPTIMIZATION ##
###############################
def ffopt(ff,mol,connected,constopt,frozenats):
    # INPUT
    #   - ff: force field to use, available MMFF94, UFF< Ghemical, GAFF
    #   - mol: mol3D to be ff optimized
    #   - connected: indices of connection atoms to metal
    #   - constopt: flag for constrained optimization
    # OUTPUT
    #   - mol: force field optimized mol3D
    ''' options
    B: ff before addition
    A: ff whole structure after addition (each step)
    BA: 0 and 1 together
    '''
    metals = range(21,31)+range(39,49)+range(72,81)
    ### check requested force field
    ffav = 'mmff94, uff, ghemical, gaff, mmff94s' # force fields
    if ff not in ffav:
        print 'Requested force field not available. Defaulting to MMFF94'
        ff = 'mmff94'
    # perform constrained ff optimization if requested after #
    if (constopt > 0):
        ### get metal
        midx = mol.findMetal()
        ### convert mol3D to OBmol via xyz file, because AFTER/END option have coordinates
        mol.writexyz('tmp.xyz')
        mol.OBmol = mol.getOBmol('tmp.xyz','xyzf')
        os.remove('tmp.xyz')
        ### initialize constraints
        constr = openbabel.OBFFConstraints()
        ### openbabel indexing starts at 1 ### !!!
        # convert metals to carbons for FF
        indmtls = []
        mtlsnums = []
        for iiat,atom in enumerate(mol.OBmol.atoms):
            if atom.atomicnum in metals:
                indmtls.append(iiat)
                mtlsnums.append(atom.atomicnum)
                atom.OBAtom.SetAtomicNum(6)
        ### add distance constraints
        for catom in connected:
            dma = mol.getAtom(midx[0]).distance(mol.getAtom(catom))
            if constopt==1:
                constr.AddAtomConstraint(catom+1) # indexing babel
            else:
                constr.AddDistanceConstraint(midx[0]+1,catom+1,dma) # indexing babel
        ### freeze metal
        constr.AddAtomConstraint(midx[0]+1) # indexing babel
        ### freeze small ligands
        for cat in frozenats:
            constr.AddAtomConstraint(cat+1) # indexing babel
        ### set up forcefield
        forcefield = openbabel.OBForceField.FindForceField(ff)
        obmol = mol.OBmol.OBMol
        forcefield.Setup(obmol,constr)
        ### force field optimize structure
        forcefield.ConjugateGradients(1000)
        forcefield.GetCoordinates(obmol)
        mol.OBmol = pybel.Molecule(obmol)
        # reset atomic number to metal
        for i,iiat in enumerate(indmtls):
            mol.OBmol.atoms[iiat].OBAtom.SetAtomicNum(mtlsnums[i])
        mol.convert2mol3D()
        del forcefield, constr, obmol
    else:
        ### initialize constraints
        constr = openbabel.OBFFConstraints()
        ### add atom constraints
        for catom in connected:
            constr.AddAtomConstraint(catom+1) # indexing babel
        ### set up forcefield
        forcefield = openbabel.OBForceField.FindForceField(ff)
        obmol = mol.OBmol.OBMol # we don't have coordinates yet, but we have OBmol
        forcefield.Setup(obmol,constr)
        ### force field optimize structure
        forcefield.ConjugateGradients(1000)
        forcefield.GetCoordinates(obmol)
        mol.OBmol = pybel.Molecule(obmol)
        mol.convert2mol3D()
        del forcefield, constr, obmol
    return mol
    
################################################
### FORCE FIELD OPTIMIZATION for custom cores ##
################################################
def ffoptd(ff,mol,connected,ccatoms,frozenats):
    # INPUT
    #   - ff: force field to use, available MMFF94, UFF< Ghemical, GAFF
    #   - mol: mol3D to be ff optimized
    #   - connected: indices of connection atoms to metal
    #   - constopt: flag for constrained optimization
    # OUTPUT
    #   - mol: force field optimized mol3D
    metals = range(21,31)+range(39,49)+range(72,81)
    ### convert mol3D to OBmol via xyz file, because AFTER/END option have coordinates
    mol.writexyz('tmp.xyz')
    mol.OBmol = mol.getOBmol('tmp.xyz','xyzf')
    os.remove('tmp.xyz')
    ### initialize constraints
    constr = openbabel.OBFFConstraints()
    ### openbabel indexing starts at 1 ### !!!
    # convert metals to carbons for FF
    indmtls = []
    mtlsnums = []
    for iiat,atom in enumerate(mol.OBmol.atoms):
        if atom.atomicnum in metals:
            indmtls.append(iiat)
            mtlsnums.append(atom.atomicnum)
            atom.OBAtom.SetAtomicNum(6)
    ### add distance constraints
    for ict,catom in enumerate(connected):
        dma = mol.getAtom(ccatoms[ict]).distance(mol.getAtom(catom))
        constr.AddDistanceConstraint(ccatoms[ict]+1,catom+1,dma) # indexing babel
    ### freeze metals
    for indm in indmtls:
        constr.AddAtomConstraint(indm+1) # indexing babel
    ### freeze small ligands
    for cat in frozenats:
        constr.AddAtomConstraint(cat+1) # indexing babel
    ### set up forcefield
    forcefield = openbabel.OBForceField.FindForceField(ff)
    obmol = mol.OBmol.OBMol
    forcefield.Setup(obmol,constr)
    ### force field optimize structure
    forcefield.ConjugateGradients(2000)
    forcefield.GetCoordinates(obmol)
    mol.OBmol = pybel.Molecule(obmol)
    # reset atomic number to metal
    for i,iiat in enumerate(indmtls):
        mol.OBmol.atoms[iiat].OBAtom.SetAtomicNum(mtlsnums[i])
    mol.convert2mol3D()
    del forcefield, constr, obmol
    return mol

#####################################################
####### Uses force field to estimate optimum ########
############ backbone positioning ###################
#################################################
def getconnection(core,cm,catom,toconnect):
    ff = 'UFF'
    metals = range(21,31)+range(39,49)+range(72,81)
    ### get hydrogens
    Hlist = core.getHs()
    ### add fake atoms for catoms
    ncore = core.natoms
    # add fake atom in local centermass axis
    coords = core.getAtom(catom).coords()
    dd = distance(coords,core.centermass())
    backbcoords = alignPtoaxis(coords,coords,vecdiff(coords,core.centermass()),1.5)
    bopt = backbcoords
    # manually find best positioning
    am = mol3D()
    am.addatom(atom3D('C',backbcoords))
    for ii in range(0,toconnect-1):
        P = PointTranslateSph(coords,am.atoms[ii].coords(),[1.5,45,30])
        am.addatom(atom3D('C',P))
    setopt = []
    mdist = -1
    for ii in range(0,toconnect):
        for itheta in range(0,360,3):
            for iphi in range(0,180,2):
                P = PointTranslateSph(coords,backbcoords,[1.5,itheta,iphi])
                am.atoms[ii].setcoords(P)
                dd = 0 
                for idx in range(0,toconnect):
                    dd += distance(cm,am.atoms[idx].coords())
                if (am.mindistmol() > 0.0):
                    d0 = dd+0.5*(log(core.mindist(am)*am.mindistmol()))
                if d0 > mdist:
                    mdist = d0
                    setopt = am.coordsvect()
    for ii in range(0,toconnect):
        core.addatom(atom3D('C',setopt[ii]))
    ffoptc = False
    if ffoptc:
        ### convert mol3D to OBmol via xyz file
        core.writexyz('tmp.xyz')
        core.OBmol = core.getOBmol('tmp.xyz','xyzf')
        os.remove('tmp.xyz')
        ### openbabel indexing starts at 1 ### 
        # convert metals to carbons for FF
        [indmtls,mtlsnums] = [[],[]]
        for iiat,atom in enumerate(core.OBmol.atoms):
            if atom.atomicnum in metals:
                indmtls.append(iiat)
                mtlsnums.append(atom.atomicnum)
                core.OBmol.atoms[iiat].OBAtom.SetAtomicNum(6)
        ### initialize constraints
        constr = openbabel.OBFFConstraints()
        ### freeze molecule
        for atom in range(ncore):
            constr.AddAtomConstraint(atom+1) # indexing babel
        ### add distance constraints
        constr.AddDistanceConstraint(catom+1,ncore,1.5)
        ### ignore Hydrogens
        for ii in Hlist:
            constr.AddIgnore(ii+1)
        ### set up forcefield
        forcefield = openbabel.OBForceField.FindForceField(ff)
        obmol = core.OBmol.OBMol
        forcefield.Setup(obmol,constr)
        ### force field optimize structure
        forcefield.ConjugateGradients(500)
        forcefield.GetCoordinates(obmol)
        core.OBmol = pybel.Molecule(obmol)
        # reset atomic number to metal
        for i,iiat in enumerate(indmtls):
            core.OBmol.atoms[iiat].OBAtom.SetAtomicNum(mtlsnums[i])
        core.convert2mol3D()
        del forcefield, constr, obmol
    connPts = []
    for ii in range(0,toconnect):
        connPts.append(core.getAtom(ncore+ii).coords())
    return connPts
    
#################################################
####### functionalizes core with ligands ########
############## for metal complexes ##############
#################################################
def mcomplex(args,core,ligs,ligoc,installdir,licores,globs):
    # INPUT
    #   - args: placeholder for input arguments
    #   - core: mol3D structure with core
    #   - ligs: list of ligands
    #   - ligoc: list of ligand occupations
    #   - installdir: top installation directory
    #   - licores: dictionary with ligands
    #   - globs: class with global variables
    # OUTPUT
    #   - core3D: built complex
    #   - complex3D: list of all mol3D ligands and core
    #   - emsg: error messages
    if globs.debug:
        print '\nGenerating complex with ligands and occupations:',ligs,ligoc
    if args.gui:
        args.gui.iWtxt.setText('\n----------------------------------------------------------------------------------\n'+
                                      '\nGenerating complex with ligands: '+ ' '.join(ligs)+'\n'+args.gui.iWtxt.toPlainText())
        args.gui.app.processEvents()
    # import gui options
    if args.gui:
        from Classes.qBox import qBoxWarning
    ### initialize variables ###
    emsg, complex3D = False, []
    coordbasef=[['one'],['li'],['tpl'],['thd','sqp'],['tbp','spy'], # list of coordinations
                ['oct','tpr'],['pbp']] 
    cclist=['one','li','tpl','thd','sqp','tbp','spy','oct','tpr','pbp'] # list of coordinations
    # get list of possible combinations for connectino atoms
    bbcombsdict = getbackbcombs()
    metal = core.getAtom(0).sym # metal symbol
    occs0 = []      # occurrences of each ligand
    dentl = []      # denticity of ligands
    toccs = 0       # total occurrence count (number of ligands)
    octa = False    # flag for forced octahedral structures like porphyrines
    catsmi = []     # SMILES ligands connection atoms
    smilesligs = 0  # count how many smiles strings
    issmiles = []   # index of SMILES ligands
    connected = []  # indices in core3D of ligand atoms connected to metal
    frozenats = []  # atoms to be frozen in optimization
    ### load bond data ###
    MLbonds = loaddata(installdir+'/Data/ML.dat')
    ### calculate occurrences, denticities etc for all ligands ###
    for i,ligname in enumerate(ligs):
        # if not in cores -> smiles
        if ligname not in licores.keys():
            dent_i = getsmident(args,smilesligs)
            issmiles.append(smilesligs)
            smilesligs += 1
        else:
            issmiles.append('-')
        # otherwise get denticity from ligands dictionary
            dent_i = int(len(licores[ligname][2:]))
        # get occurrence for each ligand if specified (default 1)
        oc_i = int(ligoc[i]) if i < len(ligoc) else 1
        occs0.append(0)         # initialize occurrences list
        dentl.append(dent_i)    # append denticity to list
        # loop over occurrence of ligand i to check for max coordination
        for j in range(0,oc_i):
            if (toccs+dent_i <= 7):
                occs0[i] += 1
            toccs += dent_i
            if dent_i == 4: # if we have 4-coordinate ligand force octahedral
                octa = True
    ### sort by descending denticity (needed for adjacent connection atoms) ###
    indcs = [i[0] for i in sorted(enumerate(dentl), key=lambda x:x[1],reverse=True)]    
    ligands = [ligs[i] for i in indcs]  # sort ligands list
    occs = [occs0[i] for i in indcs]    # sort occurrences list
    dents = [dentl[i] for i in indcs]   # sort denticities list
    issmi = [issmiles[i] for i in indcs]# sort issmiles list
    # sort keepHs list ###
    keepHs = False
    if args.keepHs:
        keepHs = [k for k in args.keepHs]
        for j in range(len(args.keepHs),len(ligs)):
            keepHs.append(False)
        keepHs = [keepHs[i] for i in indcs] # sort keepHs list
    ### sort M-L bond list ###
    MLb = False
    if args.MLbonds:
        MLb = [k for k in args.MLbonds]
        for j in range(len(args.MLbonds),len(ligs)):
            MLb.append(False)
        MLb = [MLb[i] for i in indcs] # sort MLbonds list
    ### sort ligands custom angles ###
    langles = False
    if args.langles:
        langles = []
        for j in range(len(args.langles),len(ligs)):
            langles.append(False)
        langles = [args.langles[i] for i in indcs] # sort custom langles list
    ### geometry information ###
    coord = min(toccs,7) # complex coordination
    coord = 6 if octa else coord # check if forced octahedral
    # check for coordination
    if args.coord and int(args.coord)!=coord:
        print "WARNING: Number of ligands doesn't agree with coordination/geometry. Will use geometry indicated by ligands."
        if args.gui:
            qqb = qBoxWarning(args.gui.mainWindow,'Warning',"Number of ligands doesn't agree with coordination/geometry. Will use geometry indicated by ligand frequency.")
        geom = coordbasef[coord-1][0]
    elif args.coord:
        geom = coordbasef[int(args.coord)-1][0] # geometry specified by user coordination
    else:
        geom = coordbasef[coord-1][0] # total number of ligands define coordination
    # check if geometry is defined and overwrite
    if args.geometry and args.geometry in cclist:
        geom = args.geometry
    elif args.geometry:
        if args.gui:
            qqb = qBoxWarning(args.gui.mainWindow,'Warning',"Requested geometry not available."+"Defaulting to "+coordbasef[coord-1][0])
        print "WARNING: requested geometry not available. Select one from: "
        getgeoms()
        print "Defaulting to "+coordbasef[coord-1][0]
    else:
        geom = coordbasef[coord-1][0]
    if toccs > 7:
        if args.gui:
            qqb = qBoxWarning(args.gui.mainWindow,'Warning',"Requested coordination greater than 7, 6-coordinate complex will be generated")
        print "WARNING: requested coordination greater than 7, 6-coordinate complex will be generated"
    ### load backbone and combinations ###
    # load backbone for coordination
    corexyz = loadcoord(installdir,geom)
    # get combinations possible for specified geometry
    backbatoms = bbcombsdict[geom] 
    # distort if requested
    if args.pangles:
        corexyz = modifybackbonep(corexyz,args.pangles) # point distortion
    elif args.langles:
        corexyz = modifybackbonel(corexyz,langles) # ligand distortion
    if args.distort:
        corexyz = distortbackbone(corexyz,args.distort) # random distortion
    coord = len(corexyz)-1 # get coordination
    ### initialize molecules ###
    # create molecule and add metal and base
    m3D = mol3D() 
    m3D.addatom(atom3D(metal,corexyz[0])) # add metal
    core3D = mol3D() # create backup
    core3D.addatom(atom3D(metal,corexyz[0])) # add metal
    if args.calccharge and 'y' in args.calccharge.lower():
        if args.oxstate:
            romans={'0':'0','I':'1','II':'2','III':'3','IV':'4','V':'5','VI':'6'}
            core3D.charge = int(romans[args.oxstate])
    mcoords = core3D.getAtom(0).coords() # metal coordinates in backbone
    ### initialize complex list of ligands/core
    auxm = mol3D()
    auxm.copymol3D(core3D)
    complex3D.append(auxm)
    # add terminal atoms in backbone given their coordinates
    for m in range(1,coord+1):
        m3D.addatom(atom3D('X',corexyz[m])) ## add termination atoms
    ###############################
    #### loop over ligands and ####
    ### begin functionalization ###
    ###############################
    # loop over ligands
    totlig = 0  # total number of ligands added
    for i,ligand in enumerate(ligands):
        smiles = False
        for j in range(0,occs[i]):
            denticity = dents[i]
            if not(ligand=='x' or ligand =='X') and (totlig-1+denticity < coord):
                # load ligand
                lig,emsg = lig_load(installdir,ligand,licores) # load ligand
                if emsg:
                    return False,emsg
                # if SMILES string
                if ligand not in licores.keys():
                    lig.cat = getsmilescat(args,issmi[i])
                    smiles = True
                # perform FF optimization if requested
                if args.ff and 'b' in args.ffoption:
                    if len(lig.OBmol.atoms) > 3:
                        lig = ffopt(args.ff,lig,lig.cat,0,frozenats)
                ###############################
                lig3D = lig # change name
                # convert to mol3D
                lig3D.convert2mol3D() # convert to mol3D
                if not keepHs or (len(keepHs) <= i or not keepHs[i]):
                    # remove one hydrogen
                    Hs = lig3D.getHsbyIndex(lig.cat[0])
                    if len(Hs) > 0:
                        lig3D.deleteatom(Hs[0])
                ### add atoms to connected atoms list
                catoms = lig.cat # connection atoms
                initatoms = core3D.natoms # initial number of atoms in core3D
                for at in catoms:
                    connected.append(initatoms+at)
                ### initialize variables
                atom0, r0, r1, r2, r3 = 0, mcoords, 0, 0, 0 # initialize variables
                ####################################################
                ##    attach ligand depending on the denticity    ##
                ## optimize geometry by minimizing steric effects ##
                ####################################################
                if (denticity == 1):
                    # connection atom in backbone
                    batoms,backbatoms = getnupdateb(backbatoms,denticity)
                    if len(batoms) < 1 :
                        emsg = 'Connecting all ligands is not possible. Check your input!'
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        break
                    # connection atom in lig3D
                    atom0 = catoms[0]
                    # align molecule according to connection atom and shadow atom
                    lig3D.alignmol(lig3D.getAtom(atom0),m3D.getAtom(batoms[0]))
                    r1 = lig3D.getAtom(atom0).coords()
                    r2 = lig3D.centermass() # center of mass
                    if not r2:
                        emsg = 'Center of mass calculation for ligand failed. Check input.'
                        print emsg
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        break
                    rrot = r1
                    theta,u = rotation_params(r0,r1,r2)
                    # for most ligands align center of mass of local environment
                    if (lig3D.natoms > 1):
                        lig3Db = mol3D()
                        lig3Db.copymol3D(lig3D)
                        ####################################
                        # center of mass of local environment (to avoid bad placement of bulky ligands)
                        auxmol = mol3D()
                        for at in lig3D.getBondedAtoms(atom0):
                            auxmol.addatom(lig3D.getAtom(at))
                        r2 = auxmol.centermass() # overwrite global with local centermass
                        theta,u = rotation_params(r0,r1,r2)
                        ####################################
                        # rotate around axis and get both images
                        lig3D = rotate_around_axis(lig3D,rrot,u,theta)
                        lig3Db = rotate_around_axis(lig3Db,rrot,u,theta-180)
                        d2 = distance(mcoords,lig3D.centermass())
                        d1 = distance(mcoords,lig3Db.centermass())
                        lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    if lig3D.natoms > 2:
                        #####################################
                        # check for linear molecule
                        auxm = mol3D()
                        for at in lig3D.getBondedAtoms(atom0):
                            auxm.addatom(lig3D.getAtom(at))
                        if auxm.natoms > 1:
                            r0 = lig3D.getAtom(atom0).coords()
                            r1 = auxm.getAtom(0).coords()
                            r2 = auxm.getAtom(1).coords()
                            if checkcolinear(r1,r0,r2):
                                # we will rotate so that angle is right
                                theta,urot = rotation_params(r1,mcoords,r2)
                                theta = vecangle(vecdiff(r0,mcoords),urot)
                                lig3D = rotate_around_axis(lig3D,r0,urot,theta)
                        #####################################
                        # check for symmetric molecule
                        if distance(lig3D.getAtom(atom0).coords(),lig3D.centersym()) < 8.0e-2:
                            atsc = lig3D.getBondedAtoms(atom0)
                            r0a = lig3D.getAtom(atom0).coords()
                            r1a = lig3D.getAtom(atsc[0]).coords()
                            r2a = lig3D.getAtom(atsc[1]).coords()
                            theta,u = rotation_params(r0a,r1a,r2a)
                            theta = vecangle(u,vecdiff(r0a,mcoords))
                            urot = cross(u,vecdiff(r0a,mcoords))
                            ####################################
                            # rotate around axis and get both images
                            lig3Db = mol3D()
                            lig3Db.copymol3D(lig3D)
                            lig3D = rotate_around_axis(lig3D,r0a,urot,theta)
                            lig3Db = rotate_around_axis(lig3Db,r0a,urot,-theta)
                            d2 = lig3D.mindist(core3D)
                            d1 = lig3Db.mindist(core3D)
                            lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                        # rotate around axis of symmetry and get best orientation
                        r1 = lig3D.getAtom(atom0).coords()
                        u = vecdiff(r1,mcoords)
                        dtheta = 2
                        optmax = -9999
                        totiters = 0
                        lig3Db = mol3D()
                        lig3Db.copymol3D(lig3D)
                        # check for minimum distance between atoms and center of mass distance
                        while totiters < 180:
                            lig3D = rotate_around_axis(lig3D,r1,u,dtheta)
                            d0 = lig3D.mindist(core3D) # try to maximize minimum atoms distance
                            d0cm = lig3D.distance(core3D) # try to maximize center of mass distance
                            iteropt = d0cm+10*log(d0) # optimization function
                            if (iteropt > optmax): # if better conformation, keep
                                lig3Db = mol3D()
                                lig3Db.copymol3D(lig3D)
                                optmax = iteropt
                            totiters += 1
                        lig3D = lig3Db
                    # get distance from bonds table or vdw radii
                    if MLb and MLb[i]:
                        if 'c' in MLb[i].lower():
                            bondl = m3D.getAtom(0).rad + lig3D.getAtom(atom0).rad
                        else:
                            bondl = float(MLb[i]) # check for custom
                    else:
                        bondl = getbondlength(args,metal,core3D,lig3D,0,atom0,ligand,MLbonds)
                    # get correct distance for center of mass
                    cmdist = bondl - distance(r1,mcoords)+distance(lig3D.centermass(),mcoords)
                    lig3D=setcmdistance(lig3D, mcoords, cmdist)
                elif (denticity == 2):
                    # connection atom in backbone
                    batoms,backbatoms = getnupdateb(backbatoms,denticity)
                    if len(batoms) < 1 :
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        emsg = 'Connecting all ligands is not possible. Check your input!'
                        break
                    # connection atom
                    atom0 = catoms[0]
                    # align molecule according to connection atom and shadow atom
                    lig3D.alignmol(lig3D.getAtom(atom0),m3D.getAtom(batoms[0]))
                    r1 = lig3D.getAtom(atom0).coords()
                    # align center of mass to the middle
                    r21 = [a-b for a,b in zip(lig3D.getAtom(catoms[1]).coords(),r1)]
                    r21n = [a-b for a,b in zip(m3D.getAtom(batoms[1]).coords(),r1)]
                    theta = 180*arccos(dot(r21,r21n)/(norm(r21)*norm(r21n)))/pi
                    u = cross(r21,r21n)
                    rrot = r1
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    # rotate around axis and get both images
                    lig3D = rotate_around_axis(lig3D,rrot,u,theta)
                    lig3Db = rotate_around_axis(lig3Db,rrot,u,theta-180)
                    d1 = distance(lig3D.getAtom(catoms[1]).coords(),m3D.getAtom(batoms[1]).coords())
                    d2 = distance(lig3Db.getAtom(catoms[1]).coords(),m3D.getAtom(batoms[1]).coords())
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    # align center of mass
                    rm = [0.5*(a+b) for a,b in zip(lig3D.getAtom(catoms[1]).coords(),r1)]
                    theta,u = rotation_params(r0,rm,lig3D.centermass())
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    # rotate around axis and get both images
                    lig3D = rotate_around_axis(lig3D,rm,u,theta)
                    lig3Db = rotate_around_axis(lig3Db,rm,u,theta-180)
                    d1 = lig3D.mindist(core3D)
                    d2 = lig3Db.mindist(core3D)
                    lig3D = lig3D if (d1 > d2)  else lig3Db # pick best one
                    r21 = vecdiff(r1,mcoords)
                    r21n = vecdiff(rm,mcoords)
                    costhb = dot(r21,r21n)/(norm(r21)*norm(r21n))+0.026
                    # get distance from bonds table or vdw radii
                    if MLb and MLb[i]:
                        if 'c' in MLb[i].lower():
                            bondl = m3D.getAtom(0).rad + lig3D.getAtom(atom0).rad
                        else:
                            bondl = float(MLb[i]) # check for custom
                    else:
                        bondl = getbondlength(args,metal,core3D,lig3D,0,atom0,ligand,MLbonds)
                    dbtotranslate = bondl*costhb + distance(rm,lig3D.centermass())
                    lig3D=setcmdistance(lig3D, mcoords, dbtotranslate)
                elif (denticity == 3):
                    # connection atom in backbone
                    batoms,backbatoms = getnupdateb(backbatoms,denticity)
                    if len(batoms) < 1 :
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        emsg = 'Connecting all ligands is not possible. Check your input!'
                        break
                    # connection atom
                    atom0 = catoms[1]
                    # align molecule according to connection atom and shadow atom
                    lig3D.alignmol(lig3D.getAtom(atom0),m3D.getAtom(batoms[1]))
                    # align with correct plane
                    rl0,rl1,rl2 = lig3D.getAtom(catoms[0]).coords(),lig3D.getAtom(catoms[1]).coords(),lig3D.getAtom(catoms[2]).coords()
                    rc0,rc1,rc2 = m3D.getAtom(batoms[0]).coords(),m3D.getAtom(batoms[1]).coords(),m3D.getAtom(batoms[2]).coords()
                    theta,ul = rotation_params(rl0,rl1,rl2)
                    theta,uc = rotation_params(rc0,rc1,rc2)
                    urot = vecdiff(rl1,mcoords)
                    theta = vecangle(ul,uc)
                    # rotate around primary axis
                    r1 = lig3D.getAtom(atom0).coords() # connection atomn
                    r2 = lig3D.centermass() # center of mass
                    rrot = rl1
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    lig3D = rotate_around_axis(lig3D,rrot,urot,theta)
                    lig3Db = rotate_around_axis(lig3Db,rrot,urot,180-theta)
                    rl0,rl1,rl2 = lig3D.getAtom(catoms[0]).coords(),lig3D.getAtom(catoms[1]).coords(),lig3D.getAtom(catoms[2]).coords()
                    rl0b,rl1b,rl2b = lig3Db.getAtom(catoms[0]).coords(),lig3Db.getAtom(catoms[1]).coords(),lig3Db.getAtom(catoms[2]).coords()
                    rc0,rc1,rc2 = m3D.getAtom(batoms[0]).coords(),m3D.getAtom(batoms[1]).coords(),m3D.getAtom(batoms[2]).coords()
                    theta,ul = rotation_params(rl0,rl1,rl2)
                    theta,ulb = rotation_params(rl0b,rl1b,rl2b)
                    theta,uc = rotation_params(rc0,rc1,rc2)
                    d1 = norm(cross(ul,uc))
                    d2 = norm(cross(ulb,uc))
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    # rotate around secondary axis
                    urot = uc
                    rdl = vecdiff(lig3D.getAtom(catoms[0]).coords(),rc1)
                    rdc = vecdiff(m3D.getAtom(batoms[0]).coords(),rc1)
                    theta = vecangle(rdc,rdl)
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    lig3D = rotate_around_axis(lig3D,rc1,urot,theta)
                    lig3Db = rotate_around_axis(lig3Db,rc1,urot,-theta)
                    d1 = distance(lig3D.getAtom(catoms[0]).coords(),m3D.getAtom(batoms[0]).coords())
                    d2 = distance(lig3Db.getAtom(catoms[0]).coords(),m3D.getAtom(batoms[0]).coords())
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one                    
                    # flip to align 3rd atom if wrong
                    urot = vecdiff(lig3D.getAtom(catoms[0]).coords(),lig3D.getAtom(catoms[1]).coords())
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    lig3Db = rotate_around_axis(lig3Db,rc1,urot,180)
                    d1 = distance(lig3D.getAtom(catoms[2]).coords(),m3D.getAtom(batoms[2]).coords())
                    d2 = distance(lig3Db.getAtom(catoms[2]).coords(),m3D.getAtom(batoms[2]).coords())
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    # if overlap flip
                    overlap = lig3D.overlapcheck(core3D,True)
                    if overlap:
                        lig3D = rotate_around_axis(lig3D,rc1,uc,180)
                    # translate to right distance
                    auxm = mol3D()
                    for ic,cat in enumerate(catoms):
                        auxm.addatom(lig3D.getAtom(cat))
                    cml = auxm.centermass()
                    cmc = [(rc0[ij]+rc1[ij]+rc2[ij])/3 for ij in range(0,3)]
                    lig3D.translate(vecdiff(cmc,cml))
                elif (denticity == 4):
                    # connection atom in backbone
                    batoms,backbatoms = getnupdateb(backbatoms,denticity)
                    if len(batoms) < 1 :
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        emsg = 'Connecting all ligands is not possible. Check your input!'
                        break
                    # connection atom
                    atom0 = catoms[0]
                    # align molecule according to connection atom and shadow atom
                    lig3D.alignmol(lig3D.getAtom(atom0),m3D.getAtom(batoms[0]))
                    r0c = m3D.getAtom(1).coords()
                    r1c = m3D.getAtom(2).coords()
                    r2c = m3D.getAtom(3).coords()
                    r0l = lig3D.getAtom(catoms[0]).coords()
                    r1l = lig3D.getAtom(catoms[1]).coords()
                    r2l = lig3D.getAtom(catoms[2]).coords()
                    theta,uc = rotation_params(r0c,r1c,r2c) # normal vector to backbone plane
                    theta,ul = rotation_params(r0l,r1l,r2l) # normal vector to ligand plane
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    theta = 180*arccos(dot(uc,ul)/(norm(uc)*norm(ul)))/pi
                    u = cross(uc,ul)
                    # rotate around axis to match planes
                    lig3D = rotate_around_axis(lig3D,r0l,u,theta)
                    lig3Db = rotate_around_axis(lig3Db,r0l,u,theta-180)
                    d1 = distance(lig3D.centermass(),mcoords)
                    d2 = distance(lig3Db.centermass(),mcoords)
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    # rotate around secondary axis to match atoms
                    r0l = lig3D.getAtom(catoms[0]).coords()
                    r1l = lig3D.getAtom(catoms[1]).coords()
                    r2l = lig3D.getAtom(catoms[2]).coords()
                    theta,ul = rotation_params(r0l,r1l,r2l) # normal vector to ligand plane
                    rm = lig3D.centermass()
                    r1 = vecdiff(lig3D.centermass(),r0l)
                    r2 = vecdiff(mcoords,r0l)
                    theta = 180*arccos(dot(r1,r2)/(norm(r1)*norm(r2)))/pi
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    # rotate around axis and get both images
                    lig3D = rotate_around_axis(lig3D,r0l,ul,theta)
                    lig3Db = rotate_around_axis(lig3Db,r0l,ul,theta-90)
                    d1 = distance(lig3D.centermass(),mcoords)
                    d2 = distance(lig3Db.centermass(),mcoords)      
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    # translate to center of mass
                    dcm = vecdiff(mcoords,lig3D.centermass())
                    lig3D.translate(dcm)
                elif (denticity == 5):
                    # connection atom in backbone
                    batoms,backbatoms = getnupdateb(backbatoms,denticity)
                    if len(batoms) < 1 :
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        emsg = 'Connecting all ligands is not possible. Check your input!'
                        break
                    # get center of mass 
                    ligc = mol3D()
                    for i in range(0,4): #5 is the non-planar atom
                        ligc.addatom(lig3D.getAtom(catoms[i]))
                    # translate ligand to the middle of octahedral
                    lig3D.translate(vecdiff(mcoords,ligc.centermass()))
                    # get plane
                    r0c = m3D.getAtom(batoms[0]).coords()
                    r2c = m3D.getAtom(batoms[1]).coords()
                    r1c = mcoords
                    r0l = lig3D.getAtom(catoms[0]).coords()
                    r2l = lig3D.getAtom(catoms[1]).coords()
                    r1l = mcoords
                    theta,uc = rotation_params(r0c,r1c,r2c) # normal vector to backbone plane
                    theta,ul = rotation_params(r0l,r1l,r2l) # normal vector to ligand plane
                    theta = 180*arccos(dot(uc,ul)/(norm(uc)*norm(ul)))/pi
                    u = cross(uc,ul)
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    # rotate around axis to match planes
                    lig3D = rotate_around_axis(lig3D,mcoords,u,theta)
                    lig3Db = rotate_around_axis(lig3Db,mcoords,u,180+theta)
                    d1 = distance(lig3D.getAtom(catoms[4]).coords(),m3D.getAtom(batoms[-1]).coords())
                    d2 = distance(lig3Db.getAtom(catoms[4]).coords(),m3D.getAtom(batoms[-1]).coords())
                    lig3D = lig3D if (d2 < d1)  else lig3Db # pick best one
                    # rotate around center axis to match backbone atoms
                    r0l = vecdiff(lig3D.getAtom(catoms[0]).coords(),mcoords)
                    r1l = vecdiff(m3D.getAtom(totlig+1).coords(),mcoords)
                    u = cross(r0l,r1l)
                    theta = 180*arccos(dot(r0l,r1l)/(norm(r0l)*norm(r1l)))/pi
                    lig3Db = mol3D()
                    lig3Db.copymol3D(lig3D)
                    lig3D = rotate_around_axis(lig3D,mcoords,u,theta)
                    lig3Db = rotate_around_axis(lig3Db,mcoords,u,theta-90)
                    d1 = distance(lig3D.getAtom(catoms[0]).coords(),m3D.getAtom(batoms[0]).coords())
                    d2 = distance(lig3Db.getAtom(catoms[0]).coords(),m3D.getAtom(batoms[0]).coords())
                    lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                elif (denticity == 6):
                    # connection atom in backbone
                    batoms,backbatoms = getnupdateb(backbatoms,denticity)
                    if len(batoms) < 1 :
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        emsg = 'Connecting all ligands is not possible. Check your input!'
                        break
                    # get center of mass 
                    ligc = mol3D()
                    for i in range(0,6):
                        ligc.addatom(lig3D.getAtom(catoms[i]))
                    # translate metal to the middle of octahedral
                    core3D.translate(vecdiff(ligc.centermass(),mcoords))
                auxm = mol3D()
                auxm.copymol3D(lig3D)
                complex3D.append(auxm)
                if lig3D.natoms < 4:
                    for latdix in range(0,lig3D.natoms):
                        frozenats.append(latdix+core3D.natoms)
                # combine molecules
                core3D = core3D.combine(lig3D)
                if args.calccharge and 'y' in args.calccharge.lower():
                    core3D.charge += lig3D.charge
                # perform FF optimization if requested
                if args.ff and 'a' in args.ffoption:
                    core3D = ffopt(args.ff,core3D,connected,1,frozenats)
            totlig += denticity
    # perform FF optimization if requested
    if args.ff and 'a' in args.ffoption:
        core3D = ffopt(args.ff,core3D,connected,2,frozenats)
    ###############################
    return core3D,complex3D,emsg

'''
#################################################
####### functionalizes core with ligands ########
############## for custom cores #################
#################################################
def ligadd(args,core,ligands,ligoc,installdir,licores,globs):
    # INPUT
    #   - args: placeholder for input arguments
    #   - core: mol3D structure with core
    #   - ligands: list of ligands
    #   - ligoc: list of ligand occupations
    #   - installdir: top installation directory
    #   - licores: dictionary with ligands
    #   - globs: class with global variables
    # OUTPUT
    #   - core3D: built complex
    #   - emsg: error messages
    emsg = False 
    # load base core for coordination
    catoms = core.cat # get connection atoms
    core3D = core # change name
    smilesligs = 0 # counter for smiles
    totlig = 0 # counter for total ligands
    Hlist = [] # list of hydrogens to be removed
    maxcoord = len(catoms) # maximum connected ligands
    mcoords = core3D.centermass()
    nats = core3D.natoms
    # load bond data
    MLbonds = loaddata(installdir+'/Data/ML.dat')
    for i,ligand in enumerate(ligands):
        lig,emsg = lig_load(installdir,ligand,licores) 
        if emsg:
            return False,emsg
        if ligand not in licores.keys():
            lig.denticity = getsmident(args,globs.nosmiles,smilesligs)
            smilesligs += 1
        if lig.denticity > 1:
            print 'For custom cores only monodentate ligands are supported..'
            exit(0)
        else:
            # get occupancy
            occ = ligoc[i] if i < len(ligoc) else 1
            for j in range(0,int(occ)):
                if not(ligand=='x' or ligand =='X') and (totlig < maxcoord):
                    # load ligand
                    lig,emsg = lig_load(installdir,ligand,licores) 
                    ###############################
                    ### FORCE FIELD OPTIMIZATION ##
                    ###############################
                    if (args.ff):
                        ### check requested force field
                        ffav = 'mmff94, gchemical, uff, gaff, mmff94s' # force fields
                        if args.ff not in ffav:
                            print 'Requested force field not available. Defaulting to MMFF94'
                            args.ff = 'mmff94'
                        ### force field optimize ligand
                        lig.OBmol.localopt(args.ff,1000)
                    ################################
                    lig3D = lig # change name
                    lig3D.convert2mol3D() # convert to mol3D
                    # remove one hydrogen
                    Hs = lig3D.getHsbyIndex(lig.cat[0])
                    if not keepHs or (len(keepHs) <= i or not keepHs[i]):
                        if len(Hs) > 0:
                            lig3D.deleteatom(Hs[0])
                    # get connection atom(s)
                    catom = catoms[totlig]
                    lcatom = lig.cat[0] # connecting atom for ligand
                    lcatom3D = lig3D.getAtom(lcatom)
                    catom3D = core3D.getAtom(catom)
                    # get right distance
                    db = distance(mcoords,catom3D.coords())+catom3D.rad+lcatom3D.rad
                    # if metal is the connecting point get best image by various tries
                    if catom3D.ismetal():
                        # find current coordination of metal
                        ccoord = core3D.getBondedAtoms(catom)
                        # assume octahedral coordination
                        if len(ccoord) == 4:
                            # get plane spanned by the 4 connection atoms
                            r0 = core3D.getAtom(ccoord[0]).coords()
                            r1 = core3D.getAtom(ccoord[1]).coords()
                            r2 = core3D.getAtom(ccoord[2]).coords()
                            th,uc =  rotation_params(r0,r1,r2)
                        elif len(ccoord) == 5:
                            # get center of mass between connected atoms to metal
                            auxm = mol3D()
                            for iaux in ccoord:
                                auxm.addatom(core3D.getAtom(iaux))
                            uc = vecdiff(mcoords,auxm.centermass())
                        else:
                            # try with center of mass
                            uc = vecdiff(core3D.centermass(),mcoords)
                        # get bond length
                        bondl = getbondlength(args,catom3D.sym,core3D,lig3D,0,lcatom,ligand,MLbonds)
                        # align to right axis
                        lig3D = aligntoaxis2(lig3D,lcatom3D.coords(),mcoords,uc,bondl)
                    else:
                        # align to right axis
                        uc = vecdiff(catom3D.coords(),mcoords)
                        lig3D = aligntoaxis2(lig3D,lcatom3D.coords(),mcoords,uc,db)
                    # align center of mass
                    r0 = lig3D.getAtom(lcatom).coords()
                    u0 = vecdiff(lig3D.centermass(),r0)
                    if (la.norm(u0)*la.norm(uc) > 1e-10):
                        theta = 180*np.arccos(np.dot(u0,uc)/(la.norm(u0)*la.norm(uc)))/np.pi
                        u = np.cross(u0,uc)
                        # rotate around axis
                        lig3D = rotate_around_axis(lig3D,r0,u,theta)
                    # combine molecules
                    core3D = core3D.combine(lig3D)
                    if args.calccharge and 'y' in args.calccharge.lower():
                        core3D.charge += lig3D.charge
                    # hydrogen to be removed
                    hhs = core3D.getHsbyIndex(catom)
                    if len(hhs) > 0 :
                        Hlist.append(core3D.getHsbyIndex(catom)[0])
                    totlig += 1
                else:
                    totlig += 1
    # remove extra hydrogens
    core3D.deleteatoms(Hlist)
    return core3D,emsg
'''

#################################################
####### functionalizes core with ligands ########
############## for metal complexes ##############
#################################################
def customcore(args,core,ligs,ligoc,installdir,licores,globs):
    # INPUT
    #   - args: placeholder for input arguments
    #   - core: mol3D structure with core
    #   - ligs: list of ligands
    #   - ligoc: list of ligand occupations
    #   - installdir: top installation directory
    #   - licores: dictionary with ligands
    #   - globs: class with global variables
    # OUTPUT
    #   - core3D: built complex
    #   - complex3D: list of all mol3D ligands and core
    #   - emsg: error messages
    if globs.debug:
        print '\nGenerating complex with ligands and occupations:',ligs,ligoc
    if args.gui:
        args.gui.iWtxt.setText('\nGenerating complex with core:'+args.core+' and ligands: '+ ' '.join(ligs)+'\n'+args.gui.iWtxt.toPlainText())
        args.gui.app.processEvents()
    # import gui options
    if args.gui:
        from Classes.qBox import qBoxWarning
    ### initialize variables ###
    emsg, complex3D = False, []
    occs0 = []      # occurrences of each ligand
    toccs = 0       # total occurrence count (number of ligands)
    catsmi = []     # SMILES ligands connection atoms
    smilesligs = 0  # count how many smiles strings
    issmiles = []   # index of SMILES ligands
    dentl = []      # denticity of ligands
    connected = []  # indices in core3D of ligand atoms connected to metal
    frozenats = []  # list of frozen atoms for optimization
    ### load bond data ###
    MLbonds = loaddata(installdir+'/Data/ML.dat')
    ### calculate occurrences, denticities etc for all ligands ###
    for i,ligname in enumerate(ligs):
        # if not in cores -> smiles
        if ligname not in licores.keys():
            dent_i = getsmident(args,smilesligs)
            issmiles.append(smilesligs)
            smilesligs += 1
        else:
            issmiles.append('-')
        # otherwise get denticity from ligands dictionary
            dent_i = int(len(licores[ligname][2:]))
        # get occurrence for each ligand if specified (default 1)
        oc_i = int(ligoc[i]) if i < len(ligoc) else 1
        occs0.append(0)         # initialize occurrences list
        dentl.append(dent_i)    # append denticity to list
        # loop over occurrence of ligand i to check for max coordination
        for j in range(0,oc_i):
            if (toccs+dent_i <= 7):
                occs0[i] += 1
            toccs += dent_i
    # remove ligands with denticity > 1
    todel = []
    for ii,ddent in enumerate(dentl):
        if ddent > 1:
            todel.append(ii)
    for ii in sorted(todel,reverse=True):
        del dentl[ii]
        del ligands[ii]
        del occs[ii]
        del issmi[ii]
    ### sort by descending denticity (needed for adjacent connection atoms) ###
    indcs = [i[0] for i in sorted(enumerate(dentl), key=lambda x:x[1],reverse=True)]
    ligands = [ligs[i] for i in indcs]  # sort ligands list
    occs = [occs0[i] for i in indcs]    # sort occurrences list
    issmi = [issmiles[i] for i in indcs]# sort issmiles list
    # sort keepHs list ###
    keepHs = False
    if args.keepHs:
        keepHs = [k for k in args.keepHs]
        for j in range(len(args.keepHs),len(ligs)):
            keepHs.append(False)
        keepHs = [keepHs[i] for i in indcs] # sort keepHs list
    ### sort M-L bond list ###
    MLb = False
    if args.MLbonds:
        MLb = [k for k in args.MLbonds]
        for j in range(len(args.MLbonds),len(ligs)):
            MLb.append(False)
        MLb = [MLb[i] for i in indcs] # sort MLbonds list
    if not args.ccatoms:
        emsg = 'Connection atoms for custom core not specified. Defaulting to 1!\n'
        print emsg
        if args.gui:
            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
    ccatoms = args.ccatoms if args.ccatoms else [0]
    core3D = mol3D()
    core3D.copymol3D(core)
    cmcore = core3D.centermass()
    if args.calccharge and 'y' in args.calccharge.lower():
        if args.oxstate:
            romans={'0':'0','I':'1','II':'2','III':'3','IV':'4','V':'5','VI':'6'}
            core3D.charge = int(romans[args.oxstate])
    ###############################
    #### loop over ligands and ####
    ### begin functionalization ###
    ###############################
    # flags of connection points already calculated
    setccatoms = list(set(ccatoms)) # set of connection points
    conflags = [False for ii in enumerate(setccatoms)]
    confcount = 0 
    # loop over ligands
    totlig = 0  # total number of ligands added
    for i,ligand in enumerate(ligands):
        if len(ccatoms) < i:
            ccatoms.append(0)
        smiles = False
        for j in range(0,occs[i]):
            if not(ligand=='x' or ligand =='X'):
                if totlig >= len(ccatoms):
                    emsg = 'Number of ligands greater than connection points. Please specify enough connection atoms in custom core.\n'
                    print emsg
                    if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                    return False,emsg
                core = mol3D()
                core.copymol3D(core3D)
                if not args.replig:
                    cidxconn = setccatoms.index(ccatoms[totlig]) # get current index in set of connection atoms
                    if not conflags[cidxconn]:
                        totconn = ccatoms.count(ccatoms[totlig]) # total connection points
                        alconn = ccatoms[:totlig].count(ccatoms[totlig]) # already connected
                        cpoints = getconnection(core,cmcore,ccatoms[totlig],totconn)
                        conflags[cidxconn] = True
                        confcount = 0 
                    else:
                        confcount += 1
                    cpoint = cpoints[confcount]
                    mcoords = core3D.getAtom(ccatoms[totlig]).coords() # metal coordinates in backbone
                    # connection atom save
                    conatom3D = atom3D(core3D.getAtom(ccatoms[totlig]).sym,core3D.getAtom(ccatoms[totlig]).coords())
                else:
                    cpoint = core3D.getAtom(ccatoms[totlig]).coords()
                    conatoms = core3D.getBondedAtoms(ccatoms[totlig])
                    # find real connection atom
                    metclose = core3D.findcloseMetal(core3D.getAtom(ccatoms[totlig]))
                    mindist = 1000
                    for cat in conatoms:
                        if core3D.getAtom(cat).distance(core3D.getAtom(metclose)) < mindist:
                            atclose = cat
                            mindist = core3D.getAtom(cat).distance(core3D.getAtom(ccatoms[totlig]))
                    mcoords = core3D.getAtom(atclose).coords() # connection coordinates in backbone
                    # connection atom save
                    conatom3D = atom3D(core3D.getAtom(atclose).sym,core3D.getAtom(atclose).coords())
                    delatoms = core3D.findsubMol(ccatoms[totlig],atclose) # find old ligand
                    # find shifting if needed
                    if len(ccatoms) > totlig+1:
                        lshift = len([a for a in delatoms if a < ccatoms[totlig+1]])
                        ccatoms[totlig+1] -= lshift
                    core3D.deleteatoms(delatoms)
                # load ligand
                lig,emsg = lig_load(installdir,ligand,licores) # load ligand
                if emsg:
                    return False,emsg
                # if SMILES string
                if ligand not in licores.keys():
                    lig.cat = getsmilescat(args,issmi[i])
                    smiles = True
                # perform FF optimization if requested
                if args.ff and 'b' in args.ffoption:
                    if len(lig.OBmol.atoms) > 3:
                        lig = ffopt(args.ff,lig,lig.cat,0,frozenats)
                ###############################
                lig3D = lig # change name
                # convert to mol3D
                lig3D.convert2mol3D() # convert to mol3D
                if not keepHs or (len(keepHs) <= i or not keepHs[i]):
                    # remove one hydrogen
                    Hs = lig3D.getHsbyIndex(lig.cat[0])
                    if len(Hs) > 0:
                        lig3D.deleteatom(Hs[0])
                ### add atoms to connected atoms list
                catoms = lig.cat # connection atoms
                initatoms = core3D.natoms # initial number of atoms in core3D
                ### initialize variables
                atom0, r0, r1, r2, r3 = 0, mcoords, 0, 0, 0 # initialize variables
                ####################################################
                ##    attach ligand depending on the denticity    ##
                ## optimize geometry by minimizing steric effects ##
                ####################################################
                denticity = 1
                if (denticity == 1):
                    # connection atom in lig3D
                    atom0 = catoms[0]
                    # align molecule according to connection atom and shadow atom
                    lig3D.alignmol(lig3D.getAtom(atom0),atom3D('C',cpoint))
                    r1 = lig3D.getAtom(atom0).coords()
                    r2 = lig3D.centermass() # center of mass
                    if not r2:
                        emsg = 'Center of mass calculation for ligand failed. Check input.'
                        print emsg
                        if args.gui:
                            qqb = qBoxWarning(args.gui.mainWindow,'Warning',emsg)
                        break
                    rrot = r1
                    theta,u = rotation_params(r0,r1,r2)
                    # for most ligands align center of mass of local environment
                    if (lig3D.natoms > 1):
                        lig3Db = mol3D()
                        lig3Db.copymol3D(lig3D)
                        ####################################
                        # center of mass of local environment (to avoid bad placement of bulky ligands)
                        auxmol = mol3D()
                        for at in lig3D.getBondedAtoms(atom0):
                            auxmol.addatom(lig3D.getAtom(at))
                        r2 = auxmol.centermass() # overwrite global with local centermass
                        theta,u = rotation_params(r0,r1,r2)
                        ####################################
                        # rotate around axis and get both images
                        lig3D = rotate_around_axis(lig3D,rrot,u,theta)
                        lig3Db = rotate_around_axis(lig3Db,rrot,u,theta-180)
                        d2 = distance(mcoords,lig3D.centermass())
                        d1 = distance(mcoords,lig3Db.centermass())
                        lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                    if lig3D.natoms > 2:
                        #####################################
                        # check for linear molecule
                        auxm = mol3D()
                        for at in lig3D.getBondedAtoms(atom0):
                            auxm.addatom(lig3D.getAtom(at))
                        if auxm.natoms > 1:
                            r0 = lig3D.getAtom(atom0).coords()
                            r1 = auxm.getAtom(0).coords()
                            r2 = auxm.getAtom(1).coords()
                            if checkcolinear(r1,r0,r2):
                                # we will rotate so that angle is right
                                theta,urot = rotation_params(r1,mcoords,r2)
                                theta = vecangle(vecdiff(r0,mcoords),urot)
                                lig3D = rotate_around_axis(lig3D,r0,urot,theta)
                        #####################################
                        # check for symmetric molecule
                        if distance(lig3D.getAtom(atom0).coords(),lig3D.centersym()) < 8.0e-2:
                            atsc = lig3D.getBondedAtoms(atom0)
                            r0a = lig3D.getAtom(atom0).coords()
                            r1a = lig3D.getAtom(atsc[0]).coords()
                            r2a = lig3D.getAtom(atsc[1]).coords()
                            theta,u = rotation_params(r0a,r1a,r2a)
                            theta = vecangle(u,vecdiff(r0a,mcoords))
                            urot = cross(u,vecdiff(r0a,mcoords))
                            ####################################
                            # rotate around axis and get both images
                            lig3Db = mol3D()
                            lig3Db.copymol3D(lig3D)
                            lig3D = rotate_around_axis(lig3D,r0a,urot,theta)
                            lig3Db = rotate_around_axis(lig3Db,r0a,urot,-theta)
                            d2 = lig3D.mindist(core3D)
                            d1 = lig3Db.mindist(core3D)
                            lig3D = lig3D if (d1 < d2)  else lig3Db # pick best one
                        # rotate around axis of symmetry and get best orientation
                        r1 = lig3D.getAtom(atom0).coords()
                        u = vecdiff(r1,mcoords)
                        dtheta = 2
                        optmax = -9999
                        totiters = 0
                        lig3Db = mol3D()
                        lig3Db.copymol3D(lig3D)
                        # check for minimum distance between atoms and center of mass distance
                        while totiters < 180:
                            lig3D = rotate_around_axis(lig3D,r1,u,dtheta)
                            d0 = lig3D.mindist(core3D) # try to maximize minimum atoms distance
                            d0cm = lig3D.distance(core3D) # try to maximize center of mass distance
                            iteropt = d0cm+10*log(d0) # optimization function
                            if (iteropt > optmax): # if better conformation, keep
                                lig3Db = mol3D()
                                lig3Db.copymol3D(lig3D)
                                optmax = iteropt
                            totiters += 1
                        lig3D = lig3Db
                    # get distance from bonds table or vdw radii
                    if MLb and MLb[i]:
                        if 'c' in MLb[i].lower():
                            bondl = conatom3D.rad + lig3D.getAtom(atom0).rad
                        else:
                            bondl = float(MLb[i]) # check for custom
                    else:
                        mm3D = mol3D()
                        mm3D.addatom(conatom3D)
                        bondl = getbondlength(args,conatom3D.sym,mm3D,lig3D,0,atom0,ligand,MLbonds)
                    # get correct distance for center of mass
                    u = vecdiff(cpoint,mcoords)
                    lig3D = aligntoaxis2(lig3D, cpoint, mcoords, u, bondl)
                    connected.append(core3D.natoms+atom0)
                    # list of frozen atoms (small ligands)
                    if lig3D.natoms < 4:
                        for latdix in range(0,lig3D.natoms):
                            frozenats.append(latdix+core3D.natoms)
                    # combine molecules
                    core3D = core3D.combine(lig3D)
                else:
                    emsg = 'Multidentate ligands not supported for custom cores. Skipping.\n' 
                    print emsg
                if args.calccharge and 'y' in args.calccharge.lower():
                    core3D.charge += lig3D.charge
                # perform FF optimization if requested
                if args.ff and 'a' in args.ffoption:
                    core3D = ffoptd(args.ff,core3D,connected,ccatoms,frozenats)
            totlig += 1
    # perform FF optimization if requested
    if args.ff and 'a' in args.ffoption:
        core3D = ffoptd(args.ff,core3D,connected,ccatoms,frozenats)
    return core3D,emsg

##########################################
### main structure generation function ###
##########################################
def structgen(installdir,args,rootdir,ligands,ligoc,globs):
    # INPUT
    #   - installdir: top installation directory
    #   - args: placeholder for input arguments
    #   - rootdir: directory of current run
    #   - ligands: list of ligands
    #   - ligoc: list of ligand occupations
    #   - globs: class with global variables
    # OUTPUT
    #   - strfiles: list of xyz files generated
    #   - emsg: error messages
    emsg = False
    # import gui options
    if args.gui:
        from Classes.qBox import qBoxWarning
    # get global variables class
    ############ LOAD DICTIONARIES ############
    mcores = readdict(installdir+'/Cores/cores.dict')
    licores = readdict(installdir+'/Ligands/ligands.dict')
    bindcores = readdict(installdir+'/Bind/bind.dict')
    ########## END LOAD DICTIONARIES ##########
    strfiles = []
    ########## START FUNCTIONALIZING ##########
    # load molecule core
    core,emsg = core_load(installdir,args.core,mcores)
    if emsg:
        return False,emsg
    core.convert2mol3D() # convert to mol3D
    # copy initial core for backup
    initcore3D = mol3D()
    initcore3D.copymol3D(core)
    sanity = False
    # check if ligands specified for functionalization
    if (ligands):
        # check if simple coordination complex or not
        if core.natoms == 1:
            core3D,complex3D,emsg = mcomplex(args,core,ligands,ligoc,installdir,licores,globs)
        else:
            # functionalize custom core
            core3D,emsg = customcore(args,core,ligands,ligoc,installdir,licores,globs)
        if emsg:
            return False,emsg
    else:
        core3D = initcore3D
    ############ END FUNCTIONALIZING ###########
    # generate multiple geometric arrangements
    Nogeom = int(args.bindnum) if args.bindnum and args.bind else 1 # number of different combinations
    ligname = '' # name of folder
    nosmiles = 0 
    # generate name of the folder
    for l in ligands:
        if l not in licores.keys():
            if args.sminame:
                if globs.nosmiles > 1:
                    ismidx = nosmiles
                else:
                    ismidx = 0 
                if len(args.sminame) > ismidx:
                    l = args.sminame[ismidx][0:2]
                else:
                    l = l = 'smi'+str(nosmiles)
            else:
                l = 'smi'+str(nosmiles)
            nosmiles += 1
        ligname += ''.join("%s" % l[0:2])
    if args.bind:
        # load bind, add hydrogens and convert to mol3D
        bind,bsmi,emsg = bind_load(installdir,args.bind,bindcores)
        if emsg:
            return False,emsg
        bind.convert2mol3D()
        an3D = bind # change name
        # get core size
        mindist = core3D.size
        #mindist = core3D.size
        # assign reference point
        Rp = initcore3D.centermass()
        # Generate base case (separated structures)
        an3Db = mol3D()
        an3Db.copymol3D(an3D)
        base3D = protate(an3Db,Rp,[20*mindist,0.0,0.0])
        mols = []
        maxdist = mindist+float(args.maxd) # Angstrom, distance of non-interaction    
        mindist = mindist+float(args.mind) # Angstrom, distance of non-interaction
        if args.bcharge:
            core3D.charge += int(args.bcharge)
        elif args.calccharge and 'y' in args.calccharge.lower():
            core3D.charge += int(an3D.charge)
        ### check if smiles string in binding species
        if bsmi:
            if args.nambsmi: # if name specified use it in file
                fname = rootdir+'/'+args.core[0:3]+ligname+args.nambsmi[0:2]
            else: # else use default
                fname = rootdir+'/'+args.core[0:3]+ligname+'bsm' 
        else: # else use name from binding in dictionary
            fname = rootdir+'/'+args.core[0:3]+ligname+args.bind[0:2]
        for i in range(0,Nogeom+1):        
            # generate random sequence of parameters for rotate()
            totits = 0 
            while True:
                R = random.uniform(mindist,maxdist) # get random distance, separated for i=0
                phi = random.uniform(0.0,360.0)
                theta = random.uniform(-180.0,180.0)
                if args.bphi:
                    phi = float(args.bphi)
                if args.btheta:
                    theta = float(args.btheta)
                # if specific angle is requested force angle
                if (args.place and not args.bphi and not args.btheta):
                    if ('ax' in args.place):
                        theta = 90.0
                        theta1 = -90.0
                    elif ('s' in args.place):
                        theta = 0.0
                        theta1 = 180.0
                    else:
                        theta = float(args.place)
                thetax = random.uniform(0.0,360.0)
                thetay = random.uniform(0.0,360.0)
                thetaz = random.uniform(0.0,360.0)
                # translate
                an3Db = mol3D()
                an3Db.copymol3D(an3D)
                tr3D = protate(an3Db, Rp,[R,theta,phi])
                # rotate center of mass
                newmol = cmrotate(tr3D,[thetax,thetay,thetaz])
                if ('theta1' in locals()):
                    an3Db = mol3D()
                    an3Db.copymol3D(an3D)
                    tr3D2 = protate(an3Db, Rp,[R,theta1,phi])
                    newmol2 = cmrotate(tr3D2,[thetax,thetay,thetaz])
                    d1 = tr3D.distance(core3D)
                    d2 = tr3D2.distance(core3D)
                    if (d2 > d1):
                        newmol = newmol2
                # check for overlapping
                if not(newmol.overlapcheck(core3D,1)):
                    break
                if totits > 200:
                    print "WARNING: Overlapping in molecules for file "+fname+str(i)
                    break 
                totits += 1
            if (i > 0):
                # write new xyz file
                newmol.writemxyz(core3D,fname+str(i))
                # append filename
                strfiles.append(fname+str(i))
            else:
                # write new xyz file
                core3D.writexyz(fname+'R')
                # append filename
                strfiles.append(fname+'R')
                # write binding molecule file
                an3Db.writexyz(fname+'B')
                strfiles.append(fname+'B')
                del an3Db
    else:
        fname = rootdir+'/'+args.core[0:3]+ligname
        core3D.writexyz(fname)
        strfiles.append(fname)
    pfold = rootdir.split('/',1)[-1]
    if args.calccharge and 'y' in args.calccharge.lower():
        args.charge = core3D.charge
    # check for molecule sanity
    sanity = core3D.sanitycheck(True)
    del core3D
    if sanity:
        print 'WARNING: Generated complex is not good!\n'
        if args.gui:
            qqb = qBoxWarning(args.gui.mainWindow,'Warning','Generated complex in folder '+rootdir+' is no good!')
    if args.gui:
        args.gui.iWtxt.setText('In folder '+pfold+' generated '+str(Nogeom)+' structures!\n'+args.gui.iWtxt.toPlainText())
        args.gui.app.processEvents()
    print '\nIn folder '+pfold+' generated ',Nogeom,' structures!'
    return strfiles, emsg



