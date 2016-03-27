#!/usr/bin/env python
# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT


import os, sys, subprocess
from distutils.spawn import find_executable

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

# check command exists
def checkexist(cmd):
    exist = True
    try:
        subprocess.call(cmd)
    except OSError as e:
        exist = False
    return exist


if __name__ == '__main__':
    # check if brew is installed
    brew = checkexist('brew')
    # install brew
    if not brew:
        t = mybash('./brew')
    # check if openbabel is installed
    babel = checkexist('babel')
    # check if imagemagick is installed
    immag = checkexist('convert')
    # check if openbabel module is installed
    imbabel = True
    # try many times because of stochastic pybel error
    try:
        import openbabel
        #import pybel
    except:
        imbabel = False
    if not babel and not imbabel:
        t = mybash('./brew')
    elif not imbabel:
        t = mybash('./babel')
    if not immag:
        t = mybash('./imagemagick')




