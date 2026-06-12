from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # A row is unchanged by a left rotation of k iff it is unchanged by a
        # right rotation of k, so one check covers both even and odd rows.
        k %= len(mat[0])
        return all(row == row[k:] + row[:k] for row in mat)
