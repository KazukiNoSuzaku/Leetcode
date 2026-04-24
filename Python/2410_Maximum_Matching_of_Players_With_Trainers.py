class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        p = t = ans = 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                ans += 1
                p += 1
            t += 1
        return ans
