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



files = []
for file in os.listdir("./"):
    if file.endswith(".ps") or file.endswith(".eps"):
        files.append(file)


latexFile = open("report.tex","w")
latex.BeginDocument(latexFile)
numFilesPerFigure = 3.0
numFigures = int(math.ceil(len(files) / numFilesPerFigure))
for i in range(0,numFigures):
    latex.BeginFigure(latexFile)
    for j in range(i*int(numFilesPerFigure),(i+1)*int(numFilesPerFigure)):
        if j < len(files):
           latex.BeginMiniPage(latexFile,numFilesPerFigure)
           latex.IncludeGraphics(latexFile,files[j],True)
           latex.EndMiniPage(latexFile)
    latex.EndFigure(latexFile)
latex.EndDocument(latexFile)
latexFile.close()