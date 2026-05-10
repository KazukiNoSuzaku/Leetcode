class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # A '1' can be moved anywhere or duplicated; '0' can never become '1' without an existing '1'.
        # Possible iff both are all-zeros OR both contain at least one '1'.
        has1_s = '1' in s
        has1_t = '1' in target
        return has1_s == has1_t
