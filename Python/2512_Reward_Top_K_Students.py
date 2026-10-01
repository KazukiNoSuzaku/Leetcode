# Author: Kaustav Ghosh
# Problem: Reward Top K Students
# Approach: Score each report by splitting it into words and adding three for every positive word and subtracting one for every negative word, using sets for the lookups. Then order the students by score descending with the lower id winning ties, and take the first k

class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        good = set(positive_feedback)
        bad = set(negative_feedback)
        scored = []
        for text, sid in zip(report, student_id):
            score = 0
            for word in text.split():
                if word in good:
                    score += 3
                elif word in bad:
                    score -= 1
            scored.append((-score, sid))
        scored.sort()
        return [sid for _, sid in scored[:k]]
