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
scale = 254


class BmpToBrd(object):

    def __init__(self, inFile, outFile, scalingFactor = 1):
        img = Image.open(inFile)
        self.scalingFactor = scalingFactor / 10000.0
        self.componentData = []
        self.componentElement = []
        
        #self.Read_Lines(img)
        #self.Write_Brd(outFile)

    def Read_Lines(self, img):
        print img.getpixel((5,3))
        
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
        #print start, end, y
        #outStr = '<rectangle x1="0.007621875" y1="0.00761875" x2="0.053340625" y2="0.02285625" layer="1"/>'
        outStr = '<rectangle x1="{}" y1="{}" x2="{}" y2="{}" layer="1"/>'
        x1 = start * self.scalingFactor
        y1 = y * self.scalingFactor * -1
        x2 = end * self.scalingFactor
        y2 = (y+1) * self.scalingFactor * -1
        self.componentData.append(outStr.format(x1, y1, x2, y2) + '\n')
        
        #self.componentElement.append(ET.Element('rectangle', attrib = {'x1' = x1, 'y1' = y1}))
        
        
    def Parse(self, modelFile):
        tree = ET.parse(modelFile)
        root = tree.getroot()
        
        x1 = 'hhhh'
        y1 = 'gggg'
        
        root.SubElement(root.find('drawing').find('board').find('libraries').find('library').find('packages').find('package'), 'rectangle', attrib = {'x1': x1, 'y1': y1})
        #for child in root.find('drawing').find('board').find('libraries').find('library').find('packages'):
        for rectangle in root.find('drawing').find('board').find('libraries').find('library').find('packages').find('package'):
            print rectangle.tag
            print rectangle.attrib
            print rectangle.text
            #root.remove(rectangle)
            
        # add self.componentData 
        
        tree.write('out.brd')

                
    def Write_Brd(self, filename):
        f = open(filename, 'w+')
        
        for line in self.componentData:
            f.write(line)
            
        f.close()
                

        

if __name__ == "__main__":
    obj = BmpToBrd(inFile, outFile, scale)
    obj.Parse(modelFile)
