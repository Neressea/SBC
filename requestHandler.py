from query import query
import requests

USER = 'student'
PASS = '5hoPpeR4'
HEADER = 'application/sparql-results+json'
ADDRESS = 'https://pgxlod.loria.fr/bigdata/namespace/kb/sparql'

def requestSPARQL(gene, drug, verbose=True):
    """ Return result of query based on gene and drug in param """
    res = requests.post(
        ADDRESS,
        auth=(USER, PASS),
        headers={'Accept': HEADER},
        data={'query': query % {'gene': gene, 'drug': drug}},
        verify=False
    )
    return res
