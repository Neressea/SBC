from parser import parseFile
from requestHandler import requestSPARQL
from fileManager import save

values = parseFile('./data/training_set_91_91.tsv')

data = []

l = len(values)
i = 1
for value in values:
    ind = '{0:03}'.format(i)
    print "[%s/%d] Request for (%s, %s)" % (ind, l, value[0], value[1]),
    res = requestSPARQL(gene=value[0], drug=value[1])
    if res.status_code == 200:
        print "\t[OK]",
        print res.content
        data.append({'gene': value[0], 'drug': value[1], 'asso': value[2], 'json': res.content})
    else:
        print "\t\t[FAIL]",
    i += 1
    print "\n",

save(data, FILE)
