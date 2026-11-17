# Author: Kaustav Ghosh
# Problem: Maximum Compatibility Score Sum
# Approach: This is an assignment problem on at most eight students and eight mentors, so I first build the full score table, where the score of a pair is the number of positions where their answers agree. Rather than trying all 8! = 40320 orderings I sweep a bitmask dynamic program over which mentors have been claimed: the number of set bits in a mask says which student is being placed next, so a state needs only the mask, and from each state I try every free mentor. That visits 2^m states with m transitions each, which is 2048 steps for m = 8 and is both faster and simpler to reason about than enumerating permutations.

class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        people = len(students)
        score = [[sum(1 for a, b in zip(student, mentor) if a == b)
                  for mentor in mentors]
                 for student in students]

        full = 1 << people
        best = [-1] * full
        best[0] = 0
        for mask in range(full):
            if best[mask] < 0:
                continue
            placed = bin(mask).count("1")
            if placed == people:
                continue
            for mentor in range(people):
                if mask & (1 << mentor):
                    continue
                nxt = mask | (1 << mentor)
                value = best[mask] + score[placed][mentor]
                if value > best[nxt]:
                    best[nxt] = value

        return best[full - 1]
