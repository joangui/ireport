#This software is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This software is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import math
import latex
import argparse


parser = argparse.ArgumentParser(description='Creates a report from *.ps and *.eps images')
parser.add_argument('-d', '--dir', dest='dir', type=str, default='./', required=False,
                   help='The input directory to look for the images.')
parser.add_argument('-o', '--output', dest='output', type=str, default='ireport.tex', required=False,
                   help='The name of the ouput report file.')
parser.add_argument('-n', '--num', dest='num', type=int, default='3', required=False,
                   help='The number of images per row.')
parser.add_argument('-t', '--title', dest='title', type=str, default='report', required=False,
                   help='The title of the report.')
args = parser.parse_args()


inputDir	= args.dir	# The directory to look for images.
outputFileName	= args.output	# The name of the ouput report.
numImagesPerRow = args.num	# The number of images per row.
title 		= args.title	# The title of the report.

# Look for the files in the input directory.
files = []
for file in os.listdir(inputDir):
    if file.endswith(".ps") or file.endswith(".eps"):
        files.append(file)


# Create the report
latexFile = open(outputFileName,"w")
latex.BeginDocument(latexFile,title)
numFigures = int(math.ceil(len(files) / numImagesPerRow))
for i in range(0,numFigures):
    latex.BeginFigure(latexFile)
    for j in range(i*int(numImagesPerRow),(i+1)*int(numImagesPerRow)):
        if j < len(files):
           latex.BeginMiniPage(latexFile,numImagesPerRow)
           latex.IncludeGraphics(latexFile,files[j],True)
           latex.EndMiniPage(latexFile)
    latex.EndFigure(latexFile)
latex.EndDocument(latexFile)
latexFile.close()
