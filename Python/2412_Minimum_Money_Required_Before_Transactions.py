class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        # total_loss = sum of net losses from all lossy transactions
        total_loss = sum(max(0, c - b) for c, b in transactions)
        # For each transaction i, consider it the "critical" last transaction:
        # - If lossy (c > b): need total_loss - (c-b) + c = total_loss + b
        # - If profitable (b >= c): need total_loss + c (all losses already taken)
        ans = 0
        for c, b in transactions:
            if c > b:
                ans = max(ans, total_loss + b)
            else:
                ans = max(ans, total_loss + c)
        return ans
