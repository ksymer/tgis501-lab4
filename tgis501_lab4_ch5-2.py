# Project: TGIS 501 Lab 4 Chapter 5, Challenge 2
# Filename: tgis501_lab4_ch5-2.py
# Description: Add XY coordinates to hospitals
# Author: Kris Symer
# Date: 2014-10-23


# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "X:/msgt/tgis501/lab_4/Exercise05"

# Set local variables
in_data = "hospitals.shp"
in_features = "Results/hospitals_xy.shp"

# Set spatial reference
prj_file = "facilities.prj"
prj_file = env.workspace + "/" + prj_file
print prj_file
spatial_ref = arcpy.SpatialReference(prj_file)
arcpy.DefineProjection_management(in_data, spatial_ref)
print in_data + "defined as: " + spatial_ref.name
env.overwriteOutput = True
env.outputCoordinateSystem = spatial_ref

# Copying data to preserve original dataset
# Execute Copy
arcpy.Copy_management(in_data, in_features)

# Execute AddXY
arcpy.AddXY_management(in_features)
print in_features + "complete"
