# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

#####################################################
########## This script generates input  #############
##########    for QChem calculations    #############
#####################################################

import glob
import sys
import os
import shutil
from Classes.mol3D import mol3D
from Classes.atom3D import atom3D
from Classes.globalvars import *

### generate multiple runs if multiple methods requested ###
def multiqgen(args,strfiles):
    method = False
    jobdirs=[]
    if args.method and len(args.method) > 1:
        methods = args.exchange
        for method in methods:
            jobdirs.append(qen(args,strfiles,method))
    else:
        jobdirs.append(qgen(args,strfiles,method))
    # remove original files
    for xyzf in strfiles:
        os.remove(xyzf+'.xyz')
    return jobdirs

### generate input files ###
def qgen(args,strfiles,method):
    # get global variables
    globs = globalvars()
    jobdirs = []
    coordfs = []
    # Initialize the jobparams dictionary with mandatory/useful keywords.
    jobparams={'UNRESTRICTED': 'true',
           'BASIS': 'lanl2dz',
           'JOBTYPE': 'opt',
            'EXCHANGE': 'b3lyp',
           'CORRELATION': 'none',
           'MAX_SCF_CYCLES': '500',
           'GEOM_OPT_MAX_CYCLES': '1000',
           'SYMMETRY': 'off',
           'PRINT_ORBITALS': 'true',
           'CHARGE':'1',
           'SPIN':'1',
            }
    # Overwrite plus add any new dictionary keys from commandline input.       
    for xyzf in strfiles:
        rdir = xyzf.rsplit('/',1)[0]
        xyzft = xyzf.rsplit('/',1)[-1]
        xyzf += '.xyz'
        coordfs.append(xyzf.rsplit('/',1)[-1])
        coordname = xyzft
        # Setting jobname for files + truncated name for queue.
        if len(coordname) > 10:
            nametrunc=coordname[0:6]+coordname[-4:]
        else:
            nametrunc=coordname
        if not os.path.exists(rdir+'/'+nametrunc):
            os.mkdir(rdir+'/'+nametrunc) 
        mdir = rdir+'/'+nametrunc
        if method:
            mmd = '/'+method
            mdir = rdir+'/'+nametrunc+mmd
            if not os.path.exists(mdir):
                os.mkdir(mdir)
        jobdirs.append(mdir)
        shutil.copy2(xyzf,mdir)
    # Check for existence of basis and sanitize name
    if args.basis and len(args.basis) > 1:
        jobparams['BASIS']=args.basis
    if args.correlation and len(args.correlation) > 1:
        jobparams['CORRELATION']=args.correlation
    if method and len(method) > 1:
        jobparams['EXCHANGE']=method
    if not args.unrestricted:
        jobparams['UNRESTRICTED']='false'
    # Just carry over spin and charge keywords if they're set. Could do checks, none for now.
    if args.spin:
       jobparams['SPIN']=args.spin
    if args.charge:
       jobparams['CHARGE']=args.charge
    # Now we're ready to start building the input file and the job script
    for i,jobd in enumerate(jobdirs):
        output=open(jobd+'/qch.inp','w')
        f=open(jobd+'/'+coordfs[i])
        s = f.readlines()[2:] # read coordinates
        f.close()
        # write rem block
        output.write('$rem\nUNRESTRICTED\t\t' + jobparams['UNRESTRICTED'])
        output.write('\nBASIS\t\t'+jobparams['BASIS']+'\nJOBTYPE\t\t'+jobparams['JOBTYPE'])
        output.write('\nEXCHANGE\t\t'+jobparams['EXCHANGE']+'\nCORRELATION\t\t')
        output.write(jobparams['CORRELATION']+'\nMAX_SCF_CYCLES\t\t')
        output.write(jobparams['MAX_SCF_CYCLES']+'\nGEOM_OPT_MAX_CYCLES\t\t')
        output.write(jobparams['GEOM_OPT_MAX_CYCLES']+'\nSYMMETRY\t\t'+jobparams['SYMMETRY'])
        output.write('\nPRINT_ORBITALS\t\t'+jobparams['PRINT_ORBITALS']+'\n')
        # write additional options
        if (args.remoption):
            if len(args.remoption)%2 > 0:
                print 'WARNING: wrong number of arguments in -remoption'
            else:
                for elem in range(0,int(0.5*len(args.remoption))):
                    key,val=args.remoption[2*elem],args.remoption[2*elem+1]
                    output.write(key+'\t\t'+val+'\n')
        output.write('$end\n\n')
        # write $molecule block
        output.write('$molecule\n'+jobparams['CHARGE']+' '+jobparams['SPIN']+'\n')
        output.write(''.join(s)+'$end')
        output.close()
    return jobdirs
