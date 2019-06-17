# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 09:17:37 2019

@author: Asus
"""


# Is there a way to convert an existing python file to CSV?

import csv

with open('mycsv.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['col1', 'col2', 'col3'])
    thewriter.writerow(['one', 'two', 'three'])
