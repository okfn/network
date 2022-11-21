#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import shutil

with open('okfn-network-experts.csv', mode = 'r') as file:

    csvFile = csv.reader(file)
    next(csvFile)

    for line in csvFile:
        source = 'content/specialist.md'
        destination = f'content/specialist/{line[10]}.md'
        shutil.copy(source, destination)

        # Update metadata from specialist page
        specialist_file = open(destination, 'r')
        specialist_lines = specialist_file.readlines()
        specialist_file = open(destination, 'w')

        for i, l in enumerate(specialist_lines):
            if 'og_url' in l:
                specialist_lines[i] = l.replace('specialist', f'specialist/{line[10]}') 

            if 'og_image' in l:
                specialist_lines[i] = f'og_image: "https://network.okfn.org/images/directory/{line[8]}"\n' 
                
            if 'og_title' in l:
                title = f'"{line[1]} is part of the Open Knowledge Network"'
                specialist_lines[i] = re.sub(r'([\w]*:?) "(.*)".*', r'\1 ' + title, l) 
 
            if 'og_description' in l: 
                description = '"Get in touch with our pool of experts in open data, data literacies, and more."'
                specialist_lines[i] = re.sub(r'([\w]*:?) "(.*)".*', r'\1 ' + title, l) 
 

        specialist_file.write(''.join(specialist_lines))
        specialist_file.close()


 
