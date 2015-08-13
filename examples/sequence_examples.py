from uqbinfpy.sequence import *
import sys


def example(aln_file):
    aln = readClustalFile(aln_file, Protein_Alphabet)
    aln.displayConsensus(theta1 = 0.1, theta2 = 0.01)

if (len(sys.argv) > 1):
    example(sys.argv[1])
