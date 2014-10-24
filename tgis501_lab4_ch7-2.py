# Project: TGIS 501 Lab 4 Chapter 7, Challenge 2
# Filename: tgis501_lab4_ch7-2.py
# Description: Add text field to feature class and conditionally populate values
# Author: Kris Symer
# Date: 2014-10-23

import arcpy
from arcpy import env
env.workspace = "X:/msgt/tgis501/lab_4/Exercise07"
fc = "roads.shp"
fieldName = "FERRY"
fieldType = "TEXT"
fieldLength = 3
fields = ('FEATURE', 'FERRY') #evaluate a, then update b

#Add new text field
arcpy.AddField_management(fc, fieldName, fieldType, "", "", fieldLength)

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    # For each row, evaluate the FEATURE value (index position 
    #  of 0), and update FERRY (index position of 1)
    #
    for row in cursor:
        if (row[0] == "Ferry Crossing"):
            row[1] = "Yes"
        else:
            row[1] = "No"

        # Update the cursor with the updated list
        #
        cursor.updateRow(row)

