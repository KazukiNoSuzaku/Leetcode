class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        return sorted(score, key=lambda row: -row[k])
