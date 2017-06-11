import collections
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

def load_distribution():
    dist = collections.defaultdict(int)
    fn = open('bdata.txt')
    header = fn.readline().strip()
    print repr(header)
    assert header == 'date count'
    for line in fn:
        line = line.strip()
        date, count = line.split()
        if date == 'total':
            continue
        count = int(count)
        month_num = int(date[:2])
        month = MONTHS[month_num - 1]
        #print line, ':', month, count
        dist[month] += count
    return dict(dist)

MONTH_DIST = load_distribution()
MONTHS_EXPANDED = []
for m, ct in MONTH_DIST.iteritems():
    MONTHS_EXPANDED += [m] * ct
print len(MONTHS_EXPANDED)
assert len(MONTHS_EXPANDED) == sum(MONTH_DIST.values())

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
            month = random.choice(MONTHS_EXPANDED)
        assignment[name] = month
    return assignment

for month in MONTHS:
    print month, MONTH_DIST[month],
    print MONTH_DIST[month]*100 / sum(MONTH_DIST.values())

import tqdm
count = 0
hits = 0
for i in tqdm.tqdm(range(100000)):
    a = generate_assignment()
    c, h = count_collisions(a)
    count += c
    hits += h
print hits, count, float(hits)/count * 100
