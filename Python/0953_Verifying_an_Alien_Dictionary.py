# In an alien language words are sorted according to a custom order.
# Verify that the given list of words is sorted in this alien order.

# Author: Kaustav Ghosh

class Solution(object):
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j >= len(w2): return False
                if rank[w1[j]] < rank[w2[j]]: break
                if rank[w1[j]] > rank[w2[j]]: return False
        return True
