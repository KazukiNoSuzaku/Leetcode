# Author: Kaustav Ghosh
# 1086. High Five
# https://leetcode.com/problems/high-five/

from collections import defaultdict

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)
        result = []
        for student_id in sorted(scores):
            top5 = sorted(scores[student_id], reverse=True)[:5]
            avg = sum(top5) // 5
            result.append([student_id, avg])
        return result
