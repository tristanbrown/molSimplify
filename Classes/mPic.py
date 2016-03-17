# Written by Tim Ioannidis for HJK Group
# Dpt of Chemical Engineering, MIT

##################################################
########### Defines class of window  #############
##################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import struct
import imghdr
import os
import sys

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height


class mPic(QLabel):
    # constructor needs window, picture path, marginW, marginH and scale
    # margins and scale are fractional 
    def __init__(self,window,picpath,mW,mH,sc):
        super(mPic,self).__init__()
        self = QLabel(window)
        # get picture size
        [pw,ph] = get_image_size(picpath)
        wgeom = window.getGeometry()
        # rescale image        
        initR = float(ph)/float(pw)
        pw = wgeom[2]*sc
        ph = int(initR*pw)
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        pixmap = QPixmap(picpath)
        pixmap = pixmap.scaledToHeight(ph)
        self.setGeometry(marginW,marginH,pw,ph)
        self.setPixmap(pixmap)
        self.show()

class mPic2(QLabel):
    # constructor needs window, picture path, marginW, marginH and scale
    # margins and scale are fractional 
    def __init__(self,window,picpath,mW,mH,W,H):
        super(mPic2,self).__init__()
        self = QLabel(window)
        # get picture size
        [pw,ph] = get_image_size(picpath)
        wgeom = window.getGeometry()
        # rescale image        
        initR = float(ph)/float(pw)
        wgR = float(wgeom[3])/float(wgeom[2])
        if wgR < initR : 
            rsc = float(wgeom[3])/float(ph)
        else:
            rsc = float(wgeom[2])/float(pw)
        [pw,ph] = [rsc*pw,rsc*ph]
        # check for fractional coords
        marginW =  mW*wgeom[2]
        marginH =  mH*wgeom[3]
        pixmap = QPixmap(picpath)
        pixmap = pixmap.scaled(pw,ph)
        self.setGeometry(marginW,marginH,pw,ph)
        self.setPixmap(pixmap)
        self.show()
        
        
        
        
        
        
        
        
        
        
