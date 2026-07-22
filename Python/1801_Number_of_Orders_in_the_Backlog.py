# Author: Kaustav Ghosh
# Problem: Number of Orders in the Backlog
# Approach: Keep buys in a max-heap and sells in a min-heap; each new order matches against the best opposite-side orders while prices allow, and the remainder joins its backlog

import heapq

class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        buys = []   # max-heap by price: store (-price, amount)
        sells = []  # min-heap by price: store (price, amount)

        for price, amount, order_type in orders:
            if order_type == 0:  # buy
                while amount and sells and sells[0][0] <= price:
                    sell_price, sell_amt = heapq.heappop(sells)
                    matched = min(amount, sell_amt)
                    amount -= matched
                    sell_amt -= matched
                    if sell_amt:
                        heapq.heappush(sells, (sell_price, sell_amt))
                if amount:
                    heapq.heappush(buys, (-price, amount))
            else:  # sell
                while amount and buys and -buys[0][0] >= price:
                    buy_price, buy_amt = heapq.heappop(buys)
                    matched = min(amount, buy_amt)
                    amount -= matched
                    buy_amt -= matched
                    if buy_amt:
                        heapq.heappush(buys, (buy_price, buy_amt))
                if amount:
                    heapq.heappush(sells, (price, amount))

        total = sum(amt for _, amt in buys) + sum(amt for _, amt in sells)
        return total % MOD
