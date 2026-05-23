class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        def score(pins):
            total = 0
            for i, p in enumerate(pins):
                if (i >= 1 and pins[i-1] == 10) or (i >= 2 and pins[i-2] == 10):
                    total += 2 * p
                else:
                    total += p
            return total

        s1, s2 = score(player1), score(player2)
        return 1 if s1 > s2 else 2 if s2 > s1 else 0
