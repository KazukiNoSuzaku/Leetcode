# Author: Kaustav Ghosh
# Problem: Fair Distribution of Cookies
# Approach: With few bags, assign each bag to one of the k children by backtracking, tracking each child's running total. Prune branches whose current maximum already meets the best found. Sorting bags descending makes pruning fire early. The answer is the minimum achievable maximum total

class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        cookies.sort(reverse=True)
        n = len(cookies)
        totals = [0] * k
        self.best = sum(cookies)

        def backtrack(i):
            if i == n:
                self.best = min(self.best, max(totals))
                return
            seen = set()
            for c in range(k):
                if totals[c] in seen:
                    continue  # symmetry: skip children with identical totals
                seen.add(totals[c])
                totals[c] += cookies[i]
                if totals[c] < self.best:
                    backtrack(i + 1)
                totals[c] -= cookies[i]

        backtrack(0)
        return self.best
