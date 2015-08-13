from uqbinfpy.stats import *


print "Fisher's Exact Test:"
print "The one-tailed p-value (p-value=0.998 : 0.004)"
p = getFETpval(838, 159, 78, 29)
print p
print "The two-tailed p-value (0.006)"
p2 = getFET2tail(838, 159, 78, 29)
print p2
print 80*'-'

print "Wilcoxon Ranksum: (should result in a p-value around 0.0455)"
p = getRSpval([4.6,5.1,5.8,6.5,4.7,5.2,6.1,7.2,4.9,5.5,6.5], [5.2,5.6,6.8,8.1,5.3,6.2,7.7,5.4,6.3,8.0])
print p
print 80*'-'

print "The Z-score: (should result in a z-score of around -1.78 [number of SDs from the mean] and a p-value of 0.037)"
z = getZScore([12.1, 11.2, 12.3, 11.8, 11.2, 12.3, 11.1, 13.2, 12.3, 11.6, 10.8], 10.6)
print z
p = f(z)
print p
print 80*'-'

print "A test of Pearson correlation: the example should give r = 0.988"
r = getPearson([1, 2, 3.3, 1, 2, 3.3], [0.1, 0.2, 0.33, 0.13, 0.21, 0.3])
print r
print 80*'-'
