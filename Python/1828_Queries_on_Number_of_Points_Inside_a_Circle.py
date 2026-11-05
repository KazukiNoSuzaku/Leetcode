# Author: Kaustav Ghosh
# Problem: Queries on Number of Points Inside a Circle
# Approach: With at most five hundred points and five hundred circles, testing every pair is a quarter of a million checks, which is far cheaper than any spatial index would be to build. A point lies inside or on a circle when its squared distance to the centre does not exceed the squared radius, so comparing squares keeps everything in integers and avoids a square root per test.

class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answers = []
        for cx, cy, radius in queries:
            reach = radius * radius
            answers.append(sum(1 for x, y in points
                               if (x - cx) ** 2 + (y - cy) ** 2 <= reach))
        return answers
