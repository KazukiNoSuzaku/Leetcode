class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        # Premium: index each piece by its first element; greedily match arr left-to-right.
        d = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            p = d[arr[i]]
            if arr[i:i + len(p)] != p:
                return False
            i += len(p)
        return True
