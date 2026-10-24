# Author: Kaustav Ghosh
# Problem: Maximum Height by Stacking Cuboids
# Approach: Each cuboid may be rotated freely, and the useful rotation is always the one putting its largest dimension vertical with the other two sorted, because a cuboid can sit on another exactly when all three of its sorted dimensions are no greater, and that test is unaffected by how either is turned. Sorting every cuboid's dimensions therefore loses nothing while making stackability a simple componentwise comparison. Sorting the cuboids themselves then means any stack is an increasing subsequence, so the tallest tower is a longest-increasing-subsequence search weighted by height rather than by count.

class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        boxes = sorted(sorted(box) for box in cuboids)
        n = len(boxes)
        tallest = [0] * n
        answer = 0
        for i in range(n):
            best = boxes[i][2]
            for j in range(i):
                if boxes[j][0] <= boxes[i][0] and boxes[j][1] <= boxes[i][1] \
                        and boxes[j][2] <= boxes[i][2]:
                    if tallest[j] + boxes[i][2] > best:
                        best = tallest[j] + boxes[i][2]
            tallest[i] = best
            if best > answer:
                answer = best
        return answer
