from parser import parseFile
from query import query
import requests
import time

USER = 'student'
PASS = '5hoPpeR4'
HEADER = 'application/sparql-results+json, application/json '
ADDRESS = 'https://pgxlod.loria.fr/bigdata/namespace/kb/sparql'

def requestSPARQL(gene, drug):
    print "Request for (%s, %s)" % (gene, drug),
    r = requests.post(
        ADDRESS,
        auth=(USER, PASS),
        headers={'Accept': HEADER},
        data={'query': query % {'gene': gene, 'drug': drug}},
        verify=False
    )
    print "\t[OK]"
    return r.content

values = parseFile('./data/training_set_91_91.tsv')

# for value in values:
#     request(gene=value[0], drug=value[1])

start_time = time.time()
res = requestSPARQL(gene=values[0][0], drug=values[0][1])
print("\t(%s seconds)" % (time.time() - start_time))
