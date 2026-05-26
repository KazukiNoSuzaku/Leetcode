class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return derived.count(1) % 2 == 0
