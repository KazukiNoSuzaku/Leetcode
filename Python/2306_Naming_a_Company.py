# Author: Kaustav Ghosh
class Solution(object):
    def distinctNames(self, ideas):
        # type: (List[str]) -> int
        groups = [set() for _ in range(26)]
        for w in ideas:
            groups[ord(w[0]) - ord('a')].add(w[1:])

        ans = 0
        for i in range(26):
            for j in range(i + 1, 26):
                common = len(groups[i] & groups[j])
                a = len(groups[i]) - common
                b = len(groups[j]) - common
                ans += 2 * a * b
        return ans
