#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
n = 0
'''
for n in range (0, len(dna), 3) :
    codon = dna[n:n+3]
    print (codon)
'''
k=0
for k in range (1, 6, 1) :
    print ('kmer =', k)
    for n in range (0, len(dna)-k+1, k) :
        kmer = dna[n:n+k]
        print (kmer)

"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
