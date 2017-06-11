import csv
import itertools
import random

MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

data = csv.DictReader(open('months.csv'))

LOOKUP = {}
for e in data:
    name, month = e['Name'], e['Month']
    if month != '':
        assert month in MONTHS
    LOOKUP[name] = month

assert len(LOOKUP) == 18

def count_collisions(assignment):
    count = 0
    hits = 0
    for names in itertools.combinations(assignment.keys(), r=3):
        count += 1
        months = [assignment[name] for name in names]
        #print names, months,
        hit = (len(set(months)) != len(months))
        if hit:
            hits += 1
            #print '*',
        #print
    return count, hits

def generate_assignment():
    assignment = {}
    for name, month in LOOKUP.iteritems():
        if month == '':
            month = random.choice(MONTHS)
        assignment[name] = month
    return assignment

import tqdm
count = 0
hits = 0
for i in tqdm.tqdm(range(100000)):
    a = generate_assignment()
    c, h = count_collisions(a)
    count += c
    hits += h
print hits, count, float(hits)/count * 100
