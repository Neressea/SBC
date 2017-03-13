query = """
PREFIX atc: <http://bio2rdf.org/atc:>
PREFIX bio2rdfv: <http://bio2rdf.org/bio2rdf_vocabulary:>
PREFIX clinvar: <http://bio2rdf.org/clinvar:>
PREFIX clinvarv: <http://bio2rdf.org/clinvar_vocabulary:>
PREFIX dbv: <http://bio2rdf.org/drugbank_vocabulary:>
PREFIX disgenet: <http://rdf.disgenet.org/resource/gda/>
PREFIX drugbank: <http://bio2rdf.org/drugbank:>
PREFIX mapping: <http://biodb.jp/mappings/>
PREFIX medispan: <http://orpailleur.fr/medispan/>
PREFIX ncbigene: <http://bio2rdf.org/ncbigene:>
PREFIX pharmgkb: <http://bio2rdf.org/pharmgkb:>
PREFIX pharmgkbv: <http://bio2rdf.org/pharmgkb_vocabulary:>
PREFIX pubchemcompound: <http://bio2rdf.org/pubchem.compound:>
PREFIX sider: <http://bio2rdf.org/sider:>
PREFIX siderv: <http://bio2rdf.org/sider_vocabulary:>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX so: <http://bio2rdf.org/sequence_ontology:>
PREFIX umls: <http://bio2rdf.org/umls:>
PREFIX uniprot: <http://bio2rdf.org/uniprot:>

SELECT DISTINCT ?relation ?action
WHERE {
  pharmgkb:PA449053   pharmgkbv:x-drugbank  ?drugbank.
  pharmgkb:PA107      pharmgkbv:x-uniprot   ?uniprot.
  ?relation           dbv:drug              ?drugbank.
  ?drugbankGene       dbv:x-uniprot         ?uniprot.
  { ?relation         dbv:target            ?drugbankGene }
  UNION { ?relation   dbv:carrier     ?drugbankGene }
  UNION { ?relation   dbv:enzyme      ?drugbankGene }
  UNION { ?relation   dbv:transporter ?drugbankGene }
  ?relation           dbv:action            ?action.
}
"""
#A la place du ?relation tu peux mettre un count(?action) as ?numberAction par exemple
