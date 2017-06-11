import itertools

nom = 0
denom = 0
for months in itertools.product(range(12), repeat=3):
    denom += 1
    #print months, len(months) - len(set(months)) + 1,
    if len(set(months)) != len(months):
        nom += 1
        #print '*',
    #print

print nom, denom, (nom * 100) / denom
