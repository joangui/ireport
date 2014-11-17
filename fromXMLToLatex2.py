#!/usr/bin/env python                                                          

import os
import glob
import  subprocess
import datetime
import sys

from xml.dom.minidom import parse
import xml.dom.minidom


class Query:
    input=""
    context=""
    inputTokens=""
    contextTokens=""
    plainEntityCommunities=""
    plainEntityCommunitiesCategoryFiltered=""
    selectedPaths=""


queryList =[]

xmlFile = sys.argv[1]

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse(xmlFile)
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print "Root element : %s" % collection.getAttribute("shelf")

# Get all the movies in the collection
queries = collection.getElementsByTagName("query")

# Print detail of each movie.
for query in queries:

    query_python = Query()

    print "*****Query*****"
    id = query.getElementsByTagName('id')[0]
    # print "Id: %s" % id.childNodes[0].data
    query_python.id = id.childNodes[0].data

    input = query.getElementsByTagName('input')[0]
    # print "Input: %s" % input.childNodes[0].data
    query_python.input = input.childNodes[0].data

    context = query.getElementsByTagName('context')[0]
    # print "Context: %s" % context.childNodes[0].data
    query_python.context = context.childNodes[0].data

    inputTokens = query.getElementsByTagName('inputTokens')[0]
    # print "Input tokens: %s" % inputTokens.childNodes[0].data
    query_python.inputTokens = inputTokens.childNodes[0].data

    contextTokens = query.getElementsByTagName('contextTokens')[0]
    # print "Context tokens: %s" % inputTokens.childNodes[0].data
    query_python.contextTokens= inputTokens.childNodes[0].data

    plainEntityCommunities = query.getElementsByTagName('plainEntityCommunities')[0]
    # print "Community per entity: %s" % plainEntityCommunities.childNodes[0].data
    query_python.plainEntityCommunities= plainEntityCommunities.childNodes[0].data

    plainEntityCommunitiesCategoryFiltered = query.getElementsByTagName('plainEntityCommunitiesCategoryFiltered')[0]
    # print "Community per entity category filtered: %s" % plainEntityCommunitiesCategoryFiltered.childNodes[0].data
    query_python.plainEntityCommunitiesCategoryFiltered=plainEntityCommunitiesCategoryFiltered.childNodes[0].data

    selectedPaths = query.getElementsByTagName('selectedPaths')[0]
    # print "Selected Paths: %s" % selectedPaths.childNodes[0].data
    query_python.selectedPaths = selectedPaths.childNodes[0].data

    queryList.append(query_python)
    # break

for query in queryList:
    print "Query id: " + query.id




    
