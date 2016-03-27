# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

#####################################################
########## This script generates input  #############
##########  for TeraChem calculations   #############
#####################################################
import os
import shutil
from Classes.globalvars import *


### generate multiple runs if multiple methods requested ###
def multitcgen(args,strfiles):
    jobdirs = []
    method = False
    if args.method and len(args.method) > 1:
        methods = args.method
        for method in methods:
            jobdirs.append(tcgen(args,strfiles,method))
    else:
        jobdirs.append(tcgen(args,strfiles,method))
    # remove original files
    for xyzf in strfiles:
        os.remove(xyzf+'.xyz')
    return jobdirs

### generate terachem input files ###
def tcgen(args,strfiles,method):
    # global variables
    globs = globalvars()
    jobdirs = []
    coordfs = []
    # Initialize the jobparams dictionary with mandatory/useful keywords.
    jobparams={'run': 'minimize',
           'timings': 'yes',
           'min_coordinates':'cartesian',
           'maxit': '500',
           'scrdir': './scr',
           'method': 'b3lyp',
           'basis': 'lacvps_ecp',
           'spinmult': '1',
           'charge': '0',
           'gpus': '1',
            }
    # if multiple methods requested generate c directories
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
            if method[0]=='U' or method[0]=='u':
                mmd = '/'+method[1:]
            else:
                mmd = '/'+method
            mdir = rdir+'/'+nametrunc+mmd
            if not os.path.exists(mdir):
                os.mkdir(mdir)
        jobdirs.append(mdir)
        shutil.copy2(xyzf,mdir)
    # parse extra arguments
    # Method parsing, does not check if a garbage method is used here:
    unrestricted=False
    if method:
        jobparams['method'] = method
        if ('u' or 'U') in method[0]:
            # Unrestricted calculation
            unrestricted=True
        else:
            # Restricted calculation
            unrestricted=False
            if args.spin and int(args.spin) > 1:
                jobparams['method'] = 'u'+method
                unrestricted=True
    else:
        if args.spin and int(args.spin) > 1:
                jobparams['method'] = 'ub3lyp'
                unrestricted=True
        else:
            jobparams['method'] = 'b3lyp'
    if (args.gpus):
        jobparams['gpus'] = args.gpus
    if (args.dispersion):
        jobparams['dispersion']=args.dispersion
    # Just carry over spin and charge keywords if they're set. Could do checks, none for now.
    if args.spin:
        jobparams['spinmult']=args.spin
    if args.charge:
        if args.bcharge:
            args.charge = int(args.charge)+int(args.bcharge)
        jobparams['charge']=args.charge
    # Check for existence of basis and sanitize name
    if args.basis:
        ecp=False # Flag not currently used, for deciding gpus_ecp code or not later. Can always specify with 'extra' command
        if '*' in args.basis:
            jobparams['basis']=args.basis.replace('*','s')
        else:
            jobparams['basis']=args.basis
    # Overwrite plus add any new dictionary keys from commandline input.       
    if args.qoption:
        if len(args.qoption)%2!=0:
                print 'WARNING: wrong number of arguments in -qoption'
        else:
            for elem in range(0,int(0.5*len(args.qoption))):
                key,val=args.qoption[2*elem],args.qoption[2*elem+1]
                jobparams[key]=val
    # Extra keywords for unrestricted. 
    if unrestricted:
       # If running unrestricted, assume convergence will be more difficult for now.
       jobparams['scf']='diis+a' 
       if not jobparams.has_key('levelshift'):
          jobparams['levelshift']='yes'
       elif jobparams['levelshift'] != 'yes':
          print("Warning! You're doing an unrestricted calculation but have set levelshift = %s" %(jobparams['levelshift']))
       if not jobparams.has_key('levelshiftvala'):
          jobparams['levelshiftvala']='1.6'
       if not jobparams.has_key('levelshiftvalb'):
          jobparams['levelshiftvalb']='0.1'
    # Now we're ready to start building the input file
    for i,jobd in enumerate(jobdirs):
        output=open(jobd+'/terachem_input','w')
        output.write('# file created with %s\n' % globs.PROGRAM)
        jobparams['coordinates'] = coordfs[i]
        for keys in jobparams.keys():
            output.write('%s %s\n' %(keys,jobparams[keys]))
        output.close()
    return jobdirs
