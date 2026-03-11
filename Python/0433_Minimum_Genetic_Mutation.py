# A gene string can be represented by an 8-character long string, with choices from 'A','C','G','T'.
# Given the two gene strings startGene and endGene and the gene bank, return the minimum number
# of mutations needed to mutate from startGene to endGene. Return -1 if not possible.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue = deque([(startGene, 0)])
        visited = {startGene}
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for i in range(8):
                for ch in 'ACGT':
                    mut = gene[:i] + ch + gene[i+1:]
                    if mut in bank_set and mut not in visited:
                        visited.add(mut)
                        queue.append((mut, steps + 1))
        return -1
