# Premium problem
# DP: track min cost ending on local vs express rail at each station
# local[i]   = min cost to reach station i on local line
# express[i] = min cost to reach station i on express line

class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)
        local = express_cost = 0
        express_rail = expressCost
        ans = []
        for i in range(n):
            new_local = min(local + regular[i], express_rail + regular[i])
            new_express = min(local + expressCost + express[i], express_rail + express[i])
            local, express_rail = new_local, new_express
            ans.append(min(local, express_rail))
        return ans
