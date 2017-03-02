#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from PIL import Image


inFile = 'tests/pcb.Outline.bmp'
modelFile = 'blank.brd'
outFile = 'out.brd'

#Internal units are 0.1um, or 1/10000
#So 1 pixel =
#1 mm:  10000
#1 mil: 254
scale = 423


class BmpToBrd(object):

    def __init__(self, inFile, modelFile, outFile, scalingFactor = 1):
        img = Image.open(inFile)
        self.scalingFactor = scalingFactor / 10000.0
        self.componentElement = []
        
        self.Read_Lines(img)
        self.Update_Brd(modelFile)

    def Read_Lines(self, img):
        print "Image dimensions: ", img.size
        
        for y in xrange(img.size[1]):
            start = -1
            for x in xrange(img.size[0]):
                pixel = img.getpixel((x, y))
                if pixel == 1:
                    if start == -1:
                        start = x
                    end = x + 1
                elif start != -1:
                    self.Append_Square(start, end, y)
                    start = -1

    def Append_Square(self, start, end, y):
        x1 = "{}".format(start * self.scalingFactor)
        y1 = "{}".format(y * self.scalingFactor * -1)
        x2 = "{}".format(end * self.scalingFactor)
        y2 = "{}".format((y+1) * self.scalingFactor * -1)
        
        self.componentElement.append(ET.Element('rectangle', attrib = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'layer': '1'}))
        
    def Update_Brd(self, modelFile):
        tree = ET.parse(modelFile)
        root = tree.getroot()
        
        packages = root.find('drawing').find('board').find('libraries').find('library').find('packages').find('package')
        
        for element in self.componentElement:
            ET.SubElement(packages, 'rectangle', element.attrib)
        
        tree.write('out.brd')
                
    def Write_Brd(self, filename):
        f = open(filename, 'w+')
        
        for line in self.componentData:
            f.write(line)
            
        f.close()

if __name__ == "__main__":
    obj = BmpToBrd(inFile, modelFile, outFile, scale)
