# Altium-CircuitMaker-Tools
A collection of scripts and tools to make my life easier while using Altium Designer or CircuitMaker.

There's more information [here](http://jrainimo.com/build/?p=1248), but the most useful script here is `brd-builder.py`, which can convert images to native EAGLE components, to be imported into CircuitMaker.

## brd-builder.py


### Description
Converts a 1-bit bitmap image into an EAGLE component on the specified layer. This was written because CircuitMaker's importer (via File->Import) for EAGLE files is great.

Conveniently this script is also great for importing images into EAGLE, too.

To use, open `brd-builder.py` and set the desired variable in the top portion, then run the script.

The input image *must* be a 1-bit bitmap. In Photoshop this is done by converting to grayscale in `Image->Mode->Greyscale` and then converting to bitmap in `Image->Mode->Bitmap`.
In GIMP, this is done through the menu in `Image->Mode->Indexed`. Then save as BMP.

### Pre-reqs

`pip install image`

## svg-parse.py


### Description
Grabs `test/pcb split.svg` and converts all objects to CircuitMaker-formatted CSV files for importing into shape objects.

### Pre-reqs

`pip install svg.path`

## ole-extract.py


### Description
Grabs `PCB-sl13nw6fpl4rim5mrg3x-1.PcbLib` (a CircuitMaker Library) as an OLE document extracts all binary blobs to the `ole` folder.

### Pre-reqs

`pip install olefile`

`pip install oletools`

## read-clipboard.py


### Description
This doesn't really work, was intended to read binary data in the clipboard.
