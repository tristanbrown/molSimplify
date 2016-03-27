# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

#####################################################
######## This script generates jobscripts  ##########
########     for submission to SLURM       ##########
#####################################################

import argparse, glob, sys, os, subprocess

### generates jobscripts for SGE queueing system ###
def slurmjobgen(args,jobdirs):
    # consolidate lists
    jd = []
    for i,s in enumerate(jobdirs):
        if isinstance(s,list):
            for ss in s:
                jd.append(ss)
        else:
            jd.append(s)
    jobdirs = jd
    gpus = '1' # initialize gpus
    cpus = '1' # initialize cpus
    ### loop over job directories
    for job in jobdirs:
        # form jobscript identifier
        if args.jname:
            jobname = args.jname+str(args.jid)
            jobname = jobname[:8]
        else:
            jobname = 'job'+str(args.jid)
        args.jid += 1
        output=open(job+'/'+'jobscript','w')
        output.write('#!/bin/bash\n')
        output.write('#SBATCH --job-name=%s\n' %(jobname))
        output.write('#SBATCH --output=batch.log\n')
        output.write('#SBATCH --export=ALL\n')
        if not args.wtime:
            output.write('#SBATCH -t 168:00:00\n')
        else:
            wtime = args.wtime.split(':')[0]
            wtime = wtime.split('h')[0]
            output.write('#SBATCH -t '+wtime+':00:00\n')
        if not args.memory:
            output.write('#SBATCH --mem==8G\n')
        else:
            mem = args.memory.split('G')[0]
            output.write('#SBATCH --mem='+mem+'G\n')
        if not args.queue:
            if args.qccode and args.qccode in 'terachem TeraChem TERACHEM tc TC Terachem':
                output.write('#SBATCH --partition=gpus\n')
            else:
                output.write('#SBATCH --partition=cpus\n')
        else:
            output.write('#SBATCH --partition='+args.queue+'\n')
        nod = False
        nnod = False
        if args.joption:
            for jopt in args.joption:
                output.write('#SBATCH '+jopt+'\n')
                if 'nodes' in jopt:
                    nod = True
                if 'ntasks' in jopt:
                    nnod = True
        if not nod:
            output.write('#SBATCH --nodes=1\n')
        if not nnod:
            output.write('#SBATCH --ntasks-per-node=1\n')
        if args.modules:
            for mod in args.modules:
                output.write('module load '+mod+'\n')
        if args.jcommand:
            for com in args.jcommand:
                output.write(com+'\n')
        if args.qccode and args.qccode in 'terachem TeraChem TERACHEM tc TC Terachem':
            tc = False
            if args.jcommand: 
                for jc in args.jcommand:
                    if 'terachem' in jc:
                        tc = True
            if not tc:
                output.write('terachem terachem_input > tc.out')
        elif args.qccode and args.qccode in 'GAMESS gamess gam Gamess':
            gm = False
            if args.jcommand:
                for jc in args.jcommand:
                    if 'rungms' in jc:
                        gm = True
            if not gm:
                output.write('rungms gam.inp '+cpus +' > gam.out')
        else:
            print 'No supported QC code requested. Please input execution command manually'
        output.close()
