
from pymantic import sparql
from query import query

ADDRESS = 'http://localhost:3000/bigdata/namespace/kb/sparql'

def requestSPARQL(gene, drug, verbose=True):
    """ Return result of query based on gene and drug in param """
    server = sparql.SPARQLServer(ADDRESS)
    q = query % {'gene': gene, 'drug': drug}
    print q
    res = server.query(q)
    print res


# Loading data to Blazegraph
# server.update('load <file:///tmp/data.n3>')

# Executing query

# for b in result['results']['bindings']:
#     print "%s %s" (b['p']['value'], b['o']['value']