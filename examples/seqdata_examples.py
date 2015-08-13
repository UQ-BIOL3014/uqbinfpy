import uqbinfpy.seqdata as sqd
import sys

def example(bitfile, bedfile):
    hg19 = sqd.TwoBitFile(bitfile)
    mybed1 = sqd.BedFile(bedfile, format = 'Peaks')
    print mybed1[0]
    #('chr1', 540640, 540790)
    for e in mybed1[0:5]:
        print e.getloc(hg19)
        #ggcgttttcctgtaaagttgggcacacgcttcccacatgactcagcaattgcacttctgggtatgtacccgagagaaacaaaagcttatgttcacacaaaaacctacaacgcaaatgcacaaacagctctatccaacaaccctggaagca
        #ATATAGTAAAACCCAGCCCATGGCCCCTAACAGGGGCCCTCTCAGCCCTCCTAATGACCTCCGGCCTAGCCATGTGATTTCACTTCCACTCCACAACCCTCCTCATACTAGGCCTACTAACCAACACACTAACCATATACCAATGATGGC
        #...

    for key in hg19:
        print key
    #chr19_gl000208_random
    #chr8_gl000197_random
    #chr6_apd_hap1
    #chr13
    #...

    print hg19['chrX']
    #<seqdata.TwoBitSequence at 0x10cde7d90>
    print len(hg19['chrX'])
    #155270560
    print hg19['chrX'][1000000:1000060]
    #'AAAcagctacttggaaggctgaagcaggaggattgtttgagtctaggagtttgaggctgc'


if len(sys.argv) == 3:
    example(sys.argv[1], sys.argv[2])
