class Solution:
    def countSeniors(self, details: list[str]) -> int:
        return sum(1 for d in details if int(d[11:13]) > 60)
