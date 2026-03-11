# Find the minimum cost to buy exactly the required number of items using offers or individual prices.

# Author: Kaustav Ghosh

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        def dfs(needs):
            res = sum(needs[i] * price[i] for i in range(len(needs)))
            for offer in special:
                new_needs = [needs[i] - offer[i] for i in range(len(needs))]
                if all(x >= 0 for x in new_needs):
                    res = min(res, offer[-1] + dfs(new_needs))
            return res
        return dfs(needs)
