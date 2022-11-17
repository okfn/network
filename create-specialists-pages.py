#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import shutil

with open('okfn-network-experts.csv', mode = 'r') as file:

    csvFile = csv.reader(file)
    next(csvFile)

    for line in csvFile:
        source = 'content/specialist.md'
        destination = f'content/specialist/{line[10]}.md'
        shutil.copy(source, destination)
 
