import collections
from collections import defaultdict
import operator

def non_repeating(samplestr):
    '''
    Finds and returns the FIRST NON-REPEATING character in a given string
    '''

    seendict = {}

    answer = 'no answer'

    for item in samplestr:
        if item in seendict:
            seendict[item] += 1
        else:
            seendict[item] = 1
  
    for key, value in seendict.items():
        if value == 1:
            answer = key
            return answer
        
    return answer
        

samplestr = "HHelllo"

answer = non_repeating(samplestr)
print(answer)
answer = non_repeating("abcab") # should return 'c'
print(answer)
answer = non_repeating("abab") # should return None
print(answer)
answer = non_repeating("aabbbc") # should return 'c'
print(answer)
answer = non_repeating("aabbdbc") # should return 'd'
print(answer)
