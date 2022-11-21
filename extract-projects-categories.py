#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

with open('okfn-network-projects.csv', mode = 'r') as file:

    categories = set()
    csvFile = csv.reader(file)

    for line in csvFile:
        line_cats = line[4].split(',')
        for l in line_cats:
            clean_l = l.strip()
            if clean_l != '?' and clean_l != '':
                categories.add(clean_l)


with open('data/project_categories.json', mode = 'w') as file:

    file_content = '{ "categories": ['

    for i, c in enumerate(categories):
        file_content += f'''{{
            "name": "{c}"
        }}'''

        if i < len(categories) - 1:
            file_content += ','


    file_content += "] }"
    file.write(file_content)
