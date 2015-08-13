from uqbinfpy.webservice import *

# Examples
seq = fetch('NC_004952', 'refseqn', 'fasta')
print seq
print 80*'-'
rows = search('organism:10090+AND+Sumo', 'uniprot', format = 'list') # find proteins in mouse (taxonomic id 10090) that match Sumo
print rows
print 80*'-'
rows = search('CYP1A1[Gene]+AND+Cavia+Cobaya+[Organism]', 'refseq:protein', format = 'fasta') # find proteins in NCBI's refseq (note different query syntax)
print rows
print idmap(rows[1:10])
print 80*'-'
mygo = getGOTerms(['Q9SJN0','P63166'])
mygo = getGOReport(['P20719','P63166','Q9SJN0',])
#print mygo['P63166']    # all terms associated with one of the genes
print mygo    # all terms associated with one of the genes
print getGODef('GO:0002080')['name']
print getGenes(['GO:0002080'], taxo=9606)
