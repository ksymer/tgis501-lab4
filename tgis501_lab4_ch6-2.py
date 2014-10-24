# Project: TGIS 501 Lab 4 Chapter 6, Challenge 2
# Filename: tgis501_lab4_ch6-2.py
# Description: Copy desired feature classes to a new file geodatabase
# Author: Kris Symer
# Date: 2014-10-23

# Import system modules
import arcpy
from arcpy import env

# Set environment variables
env.overwriteOutput = True
env.workspace = "X:/SOS2012/data/SoS2012.gdb"

# Set local destination variables
target_folder = "X:/msgt/tgis501/lab_4/Exercise06/Results"
target_dbname = "myOtherDB.gdb"
target_path = target_folder + "/" + target_dbname + "/"
this_shape = "polygon"

# Create list of desired feature classes in workspace
fclist = arcpy.ListFeatureClasses("", this_shape)

# If at least one desired shape exists, make a new db in target folder
if len(fclist) > 0:
    print this_shape + " count in " + env.workspace + " is: " + str(len(fclist))
    arcpy.CreateFileGDB_management(target_folder, target_dbname)

# Get name and shape type for each feature class in list
for fc in fclist:
    desc = arcpy.Describe(fc)
    name = desc.baseName
    geo = desc.shapeType
    print desc.baseName + " will be copied to: " + target_path + desc.baseName
    arcpy.CopyFeatures_management(fc, target_path + desc.baseName)

    
