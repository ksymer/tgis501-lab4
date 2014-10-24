# Project: TGIS 501 Lab 4 Chapter 5, Challenge 4
# Filename: tgis501_lab4_ch5-4.py
# Description: Check extension status
# Author: Kris Symer
# Date: 2014-10-23

# Import system modules
import arcpy
#from arcpy import env

#Create dictionary of key/value pairs for extensions to check
extensions = {'3D': '3D Analyst', 'Network': 'Network Analyst', 'Spatial': 'Spatial Analyst'}

if arcpy.CheckProduct("ArcInfo") == "Available":
    #check for extensions

    print "The following extensions are available:"
    #Create dictionary of key/value pairs for extensions to check
    extensions = {'3D': '3D Analyst', 'Network': 'Network Analyst', 'Spatial': 'Spatial Analyst'}
    for code, label in extensions.iteritems():
        if arcpy.CheckExtension(code) == "Available":
            print label
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)
