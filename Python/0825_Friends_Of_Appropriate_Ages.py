# Count friend requests sent given age-based conditions.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def numFriendRequests(self, ages):
        count = Counter(ages)
        res = 0
        for age_a, cnt_a in count.items():
            for age_b, cnt_b in count.items():
                if age_b <= 0.5 * age_a + 7: continue
                if age_b > age_a: continue
                if age_b > 100 and age_a < 100: continue
                res += cnt_a * cnt_b
                if age_a == age_b: res -= cnt_a
        return res
