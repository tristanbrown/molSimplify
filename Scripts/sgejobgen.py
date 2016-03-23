# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

#####################################################
######## This script generates jobscripts  ##########
########       for submission to SGE       ##########
#####################################################
import argparse, glob, sys, os, subprocess

### generates jobscripts for SGE queueing system ###
def sgejobgen(args,jobdirs):
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
        output.write('#$ -S /bin/bash\n')
        output.write('#$ -N %s\n' %(jobname))
        output.write('#$ -R y\n')
        if not args.wtime:
            output.write('#$ -l h_rt=168:00:00\n')
        else:
            wtime = args.wtime.split(':')[0]
            wtime = wtime.split('h')[0]
            output.write('#$ -l h_rt='+wtime+':00:00\n')
        if not args.memory:
            output.write('#$ -l h_rss=8G\n')
        else:
            mem = args.memory.split('G')[0]
            output.write('#$ -l h_rss='+mem+'G\n')
        if not args.queue:
            if args.qccode and args.qccode in 'terachem TeraChem TERACHEM tc TC Terachem':
                output.write('#$ -q gpus\n')
                if args.gpus:
                    output.write('#$ -l gpus='+args.gpus+'\n')
                    gpus = args.gpus
                else:
                    output.write('#$ -l gpus=1\n')
            else:
                output.write('#$ -q cpus\n')
                if args.cpus:
                    output.write('#$ -l cpus='+args.cpus+'\n')
                    cpus = args.cpus
                else:
                    output.write('#$ -l cpus=1\n')
        else:
            output.write('#$ -q '+args.queue+'\n')
            if args.cpus:
                    output.write('#$ -l cpus='+args.cpus+'\n')
                    cpus = args.cpus
            elif args.gpus:
                output.write('#$ -l gpus='+args.gpus+'\n')
                gpus = args.gpus
            else:
                output.write('#$ -l gpus=1\n')
        if args.gpus:
            output.write('#$ -pe smp '+args.gpus+'\n')
        elif args.cpus:
            output.write('#$ -pe smp '+args.cpus+'\n')
        else:
            output.write('#$ -pe smp 1\n')
        if args.joption:
            for jopt in args.joption:
                output.write('# '+jopt+'\n')
        if args.modules:
            for mod in args.modules:
                output.write('module load '+mod+'\n')
        if args.gpus:
            output.write('export OMP_NUM_THREADS='+args.gpus+'\n')
        elif args.cpus:
            output.write('export OMP_NUM_THREADS='+args.cpus+'\n')
        else:
            output.write('export OMP_NUM_THREADS=1\n')
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
        elif args.qccode and ('gam' in args.qccode.lower() or 'qch' in args.qccode.lower()):
            gm = False
            qch = False
            if args.jcommand:
                for jc in args.jcommand:
                    if 'rungms' in jc:
                        gm = True
                    if 'qchem' in jc:
                        qch = True
            if not gm and 'gam' in args.qccode.lower():
                output.write('rungms gam.inp '+cpus +' > gam.out')
            elif not qch and 'qch' in args.qccode.lower():
                output.write('qchem qch.inp '+cpus +' > qch.out')
        else:
            print 'Not supported QC code requested. Please input execution command manually'
        output.close()
