#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import shutil

with open('okfn-network-projects.csv', mode = 'r') as file:

    csvFile = csv.reader(file)
    next(csvFile)

    for line in csvFile:
        source = 'content/project.md'
        destination = f'content/project/{line[9]}.md'
        shutil.copy(source, destination)

        # Update metadata for project page
        project_file = open(destination, 'r')
        project_lines = project_file.readlines()
        project_file = open(destination, 'w')

        for i, l in enumerate(project_lines):
            if 'og_url' in l:
                project_lines[i] = l.replace('project', f'project/{line[9]}') 
                continue

            if 'og_image_tw' in l:
                project_lines[i] = f'og_image_tw: "https://network.okfn.org/images/logos/{line[8]}"\n' 
                continue
                
            if 'og_image' in l:
                project_lines[i] = f'og_image: "https://network.okfn.org/images/logos/{line[8]}"\n' 
                continue

            if 'og_title' in l:
                title = f'"Discover {line[1]} at the Open Knowledge Repository"'
                project_lines[i] = re.sub(r'([\w]*:?) "(.*)".*', r'\1 ' + title, l) 
                continue

            if 'og_description' in l: 
                description = '"Learn more about this and other projects about open data, data literacies, and more."'
                project_lines[i] = re.sub(r'([\w]*:?) "(.*)".*', r'\1 ' + description, l) 
                continue

        project_file.write(''.join(project_lines))
        project_file.close()
