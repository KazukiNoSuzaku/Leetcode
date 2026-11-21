# Author: Kaustav Ghosh
# Problem: Minimum Number of Work Sessions to Finish the Tasks
# Approach: With at most fourteen tasks the state can be the set of tasks already placed, but the set alone is not enough because what matters next is how much room is left in the session currently open; so each state carries the pair of sessions opened so far and time used in the open one, kept at its lexicographic minimum. That pair is the right thing to minimise because fewer sessions always dominates, and among equal counts a less-full open session dominates: anything the fuller one can do the emptier one can do too, since closing a session is always available. From each state I try every unplaced task, fitting it into the open session when it still fits and opening a new one otherwise, which explores every assignment order without enumerating submasks. That is O(2^n * n) states and transitions, about a quarter of a million steps at the limit.

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        count = len(tasks)
        full = 1 << count
        best = [None] * full
        best[0] = (1, 0)

        for mask in range(full):
            state = best[mask]
            if state is None:
                continue
            sessions, used = state
            for index in range(count):
                bit = 1 << index
                if mask & bit:
                    continue
                if used + tasks[index] <= sessionTime:
                    candidate = (sessions, used + tasks[index])
                else:
                    candidate = (sessions + 1, tasks[index])
                nxt = mask | bit
                if best[nxt] is None or candidate < best[nxt]:
                    best[nxt] = candidate

        return best[full - 1][0]
