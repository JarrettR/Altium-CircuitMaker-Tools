#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from svg.path import parse_path, Line

filename = 'pcb split.svg'
outfolder = 'out'

class SvgToPoly(object):

    def __init__(self, filename, outFolder = 'out', curveResolution = 1, scalingFactor = 1):
        tree = ET.parse(filename)
        self.root = tree.getroot()
        self.outFolder = outFolder
        self.curveResolution = curveResolution
        self.scalingFactor = scalingFactor

    def Parse(self):
        for g in self.root.findall('{http://www.w3.org/2000/svg}g'):
            for data in g.findall('{http://www.w3.org/2000/svg}path'):
                csvList = self.ConvertPath(data)
                self.WriteCsv(csvList, data.get('id'))
                #break
                
    def ConvertPath(self, data):
        name = data.get('id')
        print '-----', name
        path = data.get('d')
        #print path
        csvList = []
        
        pathSegments = parse_path(path)
        
        for segment in pathSegments:
            if not isinstance(segment, Line):
                segment = self.StraightenCurve(segment, self.curveResolution)
            csvList.append((segment.start.real * self.scalingFactor, -1 * segment.start.imag * self.scalingFactor))
        return csvList
        
                
    def StraightenCurve(self, data, samples):
        #todo: implement samples
        line = Line(data.point(0), data.point(1))
        return line
        
                
    def WriteCsv(self, data, filename):
        csvFile = [("Index","X (mil)","Y (mil)","Arc Angle (Neg = CW)")]
        i = 0
        
        f = open(self.outFolder + '/' + filename + '.csv', 'w+')
        
        for coordinate in data:
            csvFile.append((str(i), str(coordinate[0]), str(coordinate[1]), str()))
            
        for line in csvFile:
            firstEntry = True
            lineBuff = ''
            for entry in line:
                if firstEntry == False:
                    lineBuff = lineBuff + ','
                lineBuff = lineBuff + '"' + entry + '"'
                firstEntry = False
            f.write(lineBuff + '\n')
            
        f.close()
                

        

if __name__ == "__main__":
    obj = SvgToPoly(filename)
    obj.Parse()
