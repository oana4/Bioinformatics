# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 16:28:26 2025

@author: Lascu Oana
"""

#application which is able to compute the 
#relative frequencies for each symbol found in the alphabet of sequence s

from collections import Counter

def relative_frequencies(seq):
    total = len(seq)
    freq = Counter(seq)  #occurrences of each symbol
    
    
    rel_freq = {ch: count / total for ch, count in freq.items()}
    return rel_freq


s = "dfbdklfai 25782 0u8w'/[dsmkDFSJI@@@#$^*gh"
frequencies = relative_frequencies(s)

print("Relative frequencies:")
for ch, f in sorted(frequencies.items()):
    printable = ch if ch != " " else "<space>"
    print(f"{printable!r}: {f:.3f}")
