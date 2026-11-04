# Author: Kaustav Ghosh
# Problem: Number of Orders in the Backlog
# Approach: Only the extremes of each backlog can ever trade: an incoming buy is matched against the cheapest sell on the books and an incoming sell against the most expensive buy, so both sides are kept as heaps and nothing deeper than the top is ever examined. Each order repeatedly consumes the opposing top while the prices still cross, partially filling it when the amounts differ, and whatever remains of the order joins its own heap. Orders are counted at the end rather than tracked along the way, so the running total never has to be corrected.

class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        from heapq import heappop, heappush

        MOD = 10 ** 9 + 7
        buys = []   # negated prices, so the most expensive buy is on top
        sells = []  # plain prices, so the cheapest sell is on top

        for price, amount, is_sell in orders:
            if is_sell:
                while amount and buys and -buys[0][0] >= price:
                    best_price, available = heappop(buys)
                    traded = min(amount, available)
                    amount -= traded
                    if available > traded:
                        heappush(buys, (best_price, available - traded))
                if amount:
                    heappush(sells, (price, amount))
            else:
                while amount and sells and sells[0][0] <= price:
                    best_price, available = heappop(sells)
                    traded = min(amount, available)
                    amount -= traded
                    if available > traded:
                        heappush(sells, (best_price, available - traded))
                if amount:
                    heappush(buys, (-price, amount))

        return sum(amount for _, amount in buys + sells) % MOD
