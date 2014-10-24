# Project: TGIS 501 Lab 4 Chapter 5, Challenge 3
# Filename: tgis501_lab4_ch5-3.py
# Description: Dissolve parks by park_type
# Author: Kris Symer
# Date: 2014-10-23

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "X:/msgt/tgis501/lab_4/Exercise05"

# Set local variables
inFeatures = "parks.shp"
outFolder = "/Results/"
outFile = "parks_dissolve.shp"
outFeatureClass = env.workspace + outFolder + outFile
dissolveField = "PARK_TYPE"
 
# Execute Dissolve using PARK_TYPE as Dissolve Field
arcpy.Dissolve_management(inFeatures, outFeatureClass, dissolveField, "", "SINGLE_PART", "")
