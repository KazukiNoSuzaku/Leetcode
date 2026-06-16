from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diag = -1
        best_area = 0
        for l, w in dimensions:
            diag = l * l + w * w
            area = l * w
            if diag > best_diag or (diag == best_diag and area > best_area):
                best_diag = diag
                best_area = area
        return best_area
