# Author: Kaustav Ghosh

class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        import heapq
        MOD = 10 ** 9 + 7
        buy_heap = []   # max heap (negate prices)
        sell_heap = []   # min heap
        for price, amount, order_type in orders:
            if order_type == 0:  # buy
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sp, sa = heapq.heappop(sell_heap)
                    match = min(amount, sa)
                    amount -= match
                    sa -= match
                    if sa > 0:
                        heapq.heappush(sell_heap, (sp, sa))
                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))
            else:  # sell
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    bp, ba = heapq.heappop(buy_heap)
                    match = min(amount, ba)
                    amount -= match
                    ba -= match
                    if ba > 0:
                        heapq.heappush(buy_heap, (bp, ba))
                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))
        total = 0
        for _, a in buy_heap:
            total = (total + a) % MOD
        for _, a in sell_heap:
            total = (total + a) % MOD
        return total
