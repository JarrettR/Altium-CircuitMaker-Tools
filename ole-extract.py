#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import olefile
import oletools.oleid

filename = "PCB-sl13nw6fpl4rim5mrg3x-1.PcbLib"
outFolder = "ole"

class DumpOle(object):

    def __init__(self, filename, outFolder):
        
        ole = olefile.OleFileIO(filename)
        listdir = ole.listdir()
        streams = []
        for direntry in listdir:
            #print direntry
            streams.append('/'.join(direntry))
        
        self.CreateDirs(streams)
        self.WriteFiles(ole, streams, outFolder)
        
    def CreateDirs(self, streams):
        for stream in streams:
            filePath = outFolder + '/' + str(stream)
            if not os.path.exists(os.path.dirname(filePath)):
                os.makedirs(os.path.dirname(filePath))
        #browse_stream(ole, stream)
                
    def WriteFiles(self, ole, streams, outFolder):
        for stream in streams:
            f = open(outFolder + '/' + stream, 'wb')
            file = ole.openstream(stream)
            print type(stream)
            while True:
                s = file.read(8192)
                if not s:
                    break
                f.write(s)
            f.close()
            
class PackageOle(object):

    def __init__(self, filename, outFolder):
        
        ole = olefile.OleFileIO()
        file = ole.open(filename, True)
        listdir = ole.listdir()
        streams = []
        for direntry in listdir:
            #print direntry
            streams.append('/'.join(direntry))
        
        
    def CreateDirs(self, streams):
        for stream in streams:
            filePath = outFolder + '/' + str(stream)
            if not os.path.exists(os.path.dirname(filePath)):
                os.makedirs(os.path.dirname(filePath))
        #browse_stream(ole, stream)
                
    def WriteFiles(self, ole, streams, outFolder):
        for stream in streams:
            f = open(outFolder + '/' + stream, 'wb')
            file = ole.openstream(stream)
            while True:
                s = file.read(8192)
                if not s:
                    break
                f.write(s)
            f.close()
            
                

        

if __name__ == "__main__":
    obj = DumpOle(filename, outFolder)
    #obj = PackageOle(filename, outFolder)
