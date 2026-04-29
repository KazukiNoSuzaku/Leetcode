class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        def within_two(a, b):
            return sum(x != y for x, y in zip(a, b)) <= 2

        return [q for q in queries if any(within_two(q, d) for d in dictionary)]
