from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        for x in cnt:
            if x == 1:
                # All 1s are usable since 1^2=1; any length is valid
                ans = max(ans, cnt[1])
                continue

            # Structure A: x as CENTER (smallest), outer pairs ascend x^2, x^4, ...
            #   Palindrome: [..., x^4, x^2, x, x^2, x^4, ...]
            length_a = 1
            u = x * x
            while u in cnt and cnt[u] >= 2:
                length_a += 2
                u = u * u
            ans = max(ans, length_a)

            # Structure B: x as OUTERMOST (smallest), center is LARGEST
            #   Palindrome: [x, x^2, ..., center, ..., x^2, x]
            #   Need cnt[x] >= 2 to use x as outer pair; else x can only be center (length 1)
            length_b = 0
            v = x
            while v in cnt:
                if cnt[v] >= 2:
                    length_b += 2
                    v = v * v
                else:
                    length_b += 1  # single copy = center
                    break
            else:
                # Exited because v not in cnt; last level was an outer pair with no center above it
                # Downgrade last outer pair to center: net -2+1 = -1
                length_b -= 1
            ans = max(ans, length_b)

        return ans
