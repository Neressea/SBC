from fileManager import load, FILE

data = load(FILE)

for d in data:
    print "(%s, %s) -> %s" % (d['gene'], d['drug'], d['asso'])
    print "%s" % (d['json'])
