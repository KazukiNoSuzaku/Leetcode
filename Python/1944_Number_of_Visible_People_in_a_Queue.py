# Author: Kaustav Ghosh
# Problem: Number of Visible People in a Queue
# Approach: Person i sees person j when everyone strictly between them is shorter than both, so the people i can see are exactly the strictly increasing run of record heights starting just to the right of i, ending with the first person taller than i. Walking from the right and keeping a stack of heights that is increasing from the top down gives each of those runs for free: everyone shorter than the current person can never be seen past them again, so I pop them and count each pop as one visible person, then add one more if the stack still holds someone, who is the first taller person. Every person is pushed and popped at most once, so the whole pass is O(n).

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        total = len(heights)
        visible = [0] * total
        shorter = []

        for index in range(total - 1, -1, -1):
            height = heights[index]
            seen = 0
            while shorter and shorter[-1] < height:
                shorter.pop()
                seen += 1
            if shorter:
                seen += 1
            visible[index] = seen
            shorter.append(height)

        return visible
