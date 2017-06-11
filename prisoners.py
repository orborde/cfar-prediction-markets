def compute_outcomes(c):
    d = 1 - c
    dd = d * d
    cc = c * c
    dc = c * d * 2
    return dd, cc, dc

print "{:3} {:4} {:6} {:6} {:6}".format("i", "c", "cc", "dc", "dd")
for i in range(0, 100+1, 5):
    c = float(i) / 100
    dd, cc, dc = compute_outcomes(c)
    print "{:3} {:4} {:6} {:6} {:6}".format(i, c, cc, dc, dd)

