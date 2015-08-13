##################################################################################################################
#      Example applications of ML methods including NNs and Naive Bayes for secondary structure prediction.      #
##################################################################################################################

import os, time
import sys

from uqbinfpy import sequence
from uqbinfpy import ml
from uqbinfpy import prob
from uqbinfpy.spred import *
from uqbinfpy import sym


def example(datadir):
    os.chdir(datadir)  # Note you will need to change this to find your directory of choice
    prot = sequence.readFastaFile('prot2.fa', sym.Protein_Alphabet)  # proteins
    sstr = sequence.readFastaFile('sstr3.fa', sym.DSSP3_Alphabet)    # secondary structure of prot
    # separate training and test data
    prot_trn = prot[0::2] # even-numbered indices
    prot_tst = prot[1::2] # odd-numbered indices
    sstr_trn = sstr[0::2] # even-numbered indices
    sstr_tst = sstr[1::2] # odd-numbered indices
    W = 15
    nHid = 30
    nn = SeqNN(W, sym.Protein_Alphabet, sym.DSSP3_Alphabet, nHid, cascade = W)
    #nn.nn = ml.readNNFile('sstr3.nn')
    #print "Successfully loaded network"
    start = time.time()
    print nn.observeAll(prot_trn, sstr_trn, eta = 0.01, niter = 20)
    print "It took", time.time() - start, "seconds to train NN."
    cm = nn.testAll(prot_tst, sstr_tst)
    print cm
    Qk, Q = ml.Qk(cm, sym.DSSP3_Alphabet)
    print Q
    print Qk
    nn.nn1.writeFile('sstr3.nn1')
    nn.nn2.writeFile('sstr3.nn2')
    print "Successfully saved network/s"


    nb = prob.NaiveBayes([ sym.Protein_Alphabet for _ in range(W) ], sym.DSSP3_Alphabet)
    start = time.time()
    for i in range(len(prot_trn)):
        subseqs = slidewin(prot_trn[i], W)
        # Note how we remove the targets at the ends of the sequence
        subtarg = sstr_trn[i][W/2:-W/2+1]
        for j in range(len(subseqs)):
            nb.observe(subseqs[j], subtarg[j])
    print "It took", time.time() - start, "seconds to train NB."
    cm = numpy.zeros((len(sym.DSSP3_Alphabet), len(sym.DSSP3_Alphabet)))
    for i in range(len(prot_tst)):
        subseqs = slidewin(prot_tst[i], W)
        # Note how we remove the targets at the ends of the sequence
        subtarg = sstr_tst[i][W/2:-W/2+1]
        for j in range(len(subseqs)):
            out = nb[subseqs[j]]
            c_targ = sym.DSSP3_Alphabet.index(subtarg[j])
            c_pred = out.prob().index(max(out.prob()))
            cm[c_targ, c_pred] += 1
    print cm
    Qk, Q = ml.Qk(cm, sym.DSSP3_Alphabet)
    print Q
    print Qk

if (len(sys.argv) > 1):
    example1()
