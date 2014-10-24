# Project: TGIS 501 Lab 4 Chapter 7, Challenge 1
# Filename: tgis501_lab4_ch7-1.py
# Description: Create conditional buffers
# Author: Kris Symer
# Date: 2014-10-23

# Import system modules
import arcpy
from arcpy import env

# Set environment variables
env.workspace = "X:/msgt/tgis501/lab_4/Exercise07"

fc = "airports.shp"
unique_name = arcpy.CreateUniqueName("Results/seaplane_buffer.shp")

cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" = \'Seaplane Base\'')
for row in cursor:
    #populate feature class
del row
del cursor

arcpy.Buffer_analysis(fc, unique_name, "7500 METERS")


unique_name = arcpy.CreateUniqueName("Results/airport_buffer.shp")

cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" = \'Airport\'')
for row in cursor:
    #populate feature class
del row
del cursor

arcpy.Buffer_analysis(fc, unique_name, "15000 METERS")

