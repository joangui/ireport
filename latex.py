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

def BeginDocument(fileObject,title):
    fileObject.write("\documentclass{article}\n")
    fileObject.write("\\usepackage{fullpage}\n")
    fileObject.write("\\usepackage{array}\n")
    fileObject.write("\\usepackage{amssymb}\n")
    fileObject.write("\\usepackage{amsmath}\n")
    fileObject.write("\\usepackage{url}\n")
    fileObject.write("\\usepackage{cite}\n")
    fileObject.write("\\usepackage{rotating}\n")
    fileObject.write("\\usepackage{enumitem}\n")
    fileObject.write("\\usepackage{xfrac}\n")
    fileObject.write("\\usepackage{multicol}\n")
    fileObject.write("\\usepackage{booktabs}\n")
    fileObject.write("\\usepackage{tabulary}\n")
    fileObject.write("\\usepackage{float}\n")
    fileObject.write("\\usepackage[utf8]{inputenc}\n")
    fileObject.write("\\title{"+title+"}\n")
    fileObject.write("\\begin{document}\n")
    fileObject.write("\\maketitle\n")
    return

def EndDocument(fileObject):
    fileObject.write("\end{document}")
    return

def BeginMiniPage(fileObject,numFiguresPerMinipage):
    fileObject.write("\\begin{minipage}{"+str(0.98/float(numFiguresPerMinipage))+"\linewidth}\n")
    fileObject.write("\\centering\n")
    return
def EndMiniPage(fileObject):
    fileObject.write("\end{minipage}\n")
    return

def BeginFigure(fileObject):
    fileObject.write("\\begin{figure}[H]\n")
    return
def EndFigure(fileObject):
    fileObject.write("\end{figure}\n")
    return


def IncludeGraphics(fileObject,imageFileName,rotate):
    if rotate:
        fileObject.write("\includegraphics[width=0.7\linewidth,angle=-90]{"+imageFileName+"}\n")
    else: 
        fileObject.write("\includegraphics[width=0.7\linewidth]{"+imageFileName+"}\n")
    return


