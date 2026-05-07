class Solution:
    def topStudents(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int,
    ) -> list[int]:
        # Score each report: +3 per positive word, -1 per negative word; sort by (-score, id).
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        scores = []
        for sid, rep in zip(student_id, report):
            score = 0
            for word in rep.split():
                if word in pos:
                    score += 3
                elif word in neg:
                    score -= 1
            scores.append((-score, sid))
        scores.sort()
        return [sid for _, sid in scores[:k]]
