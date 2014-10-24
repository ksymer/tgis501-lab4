# Project: TGIS 501 Lab 4 Chapter 6, Challenge 1
# Filename: tgis501_lab4_ch6-1.py
# Description: List workspace feature class names and geometry
# Author: Kris Symer
# Date: 2014-10-23

# Import system modules
import arcpy
from arcpy import env

# Set environment variables
env.workspace = "X:/msgt/tgis501/lab_4/Exercise06"

# Create list of all feature classes in workspace
fclist = arcpy.ListFeatureClasses()

# Get name and shape type for each feature class in list
for fc in fclist:
    desc = arcpy.Describe(fc)
    name = desc.baseName
    geo = desc.shapeType
    print name + " is a " + geo + " feature class"
