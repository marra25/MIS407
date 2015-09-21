# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:08:54 2015

@author: Bryce Marra
"""

import csv

with open('myData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    prices = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        price = row[4]

        dates.append(date)
        colors.append(color)
        prices.append(price)

    print(dates)
    print(colors)
    print(prices)
