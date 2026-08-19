# Author: Kaustav Ghosh
# Problem: Maximum Number of Tasks You Can Assign
# Approach: Binary search the number of tasks k. Feasibility uses the k easiest tasks and k strongest workers: process tasks hardest first, assigning the strongest free worker without a pill when possible, otherwise spending a pill on the weakest worker that can still reach the task. A Fenwick-tree multiset over worker strengths gives the needed max / smallest-at-least queries efficiently

import bisect

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        vals = sorted(set(workers))
        comp = {v: i for i, v in enumerate(vals)}
        V = len(vals)

        def check(k):
            tree = [0] * (V + 1)

            def upd(i, d):
                i += 1
                while i <= V:
                    tree[i] += d
                    i += i & (-i)

            def pref(i):  # sum of counts in values indices [0..i]
                i += 1
                s = 0
                while i > 0:
                    s += tree[i]
                    i -= i & (-i)
                return s

            def kth(rank):  # value index of the rank-th smallest (1-based)
                pos = 0
                for pw in range(V.bit_length(), -1, -1):
                    nxt = pos + (1 << pw)
                    if nxt <= V and tree[nxt] < rank:
                        pos = nxt
                        rank -= tree[nxt]
                return pos

            for w in workers[m - k:]:
                upd(comp[w], 1)

            total = k
            p = pills
            for i in range(k - 1, -1, -1):
                t = tasks[i]
                if total == 0:
                    return False
                strongest = kth(total)
                if vals[strongest] >= t:
                    upd(strongest, -1)
                    total -= 1
                else:
                    if p == 0:
                        return False
                    need = t - strength
                    lo = bisect.bisect_left(vals, need)
                    if lo >= V:
                        return False
                    cnt_less = pref(lo - 1) if lo > 0 else 0
                    if cnt_less >= total:
                        return False
                    widx = kth(cnt_less + 1)
                    if vals[widx] < need:
                        return False
                    upd(widx, -1)
                    total -= 1
                    p -= 1
            return True

        lo, hi, ans = 0, min(n, m), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
