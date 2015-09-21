# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:05:18 2015

@author: Bryce Marra
"""

import csv

with open('myData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
