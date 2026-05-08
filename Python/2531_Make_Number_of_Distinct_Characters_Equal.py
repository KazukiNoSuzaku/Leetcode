from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # Try every (ch1, ch2) swap; simulate effect on distinct counts; O(26^2).
        cnt1, cnt2 = Counter(word1), Counter(word2)
        d1, d2 = len(cnt1), len(cnt2)

        for ch1 in list(cnt1):
            for ch2 in list(cnt2):
                if ch1 == ch2:
                    if d1 == d2:
                        return True
                    continue
                nd1 = d1 - (cnt1[ch1] == 1) + (ch2 not in cnt1)
                nd2 = d2 - (cnt2[ch2] == 1) + (ch1 not in cnt2)
                if nd1 == nd2:
                    return True
        return False
