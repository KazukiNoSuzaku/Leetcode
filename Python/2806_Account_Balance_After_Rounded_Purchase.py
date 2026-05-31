class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        remainder = purchaseAmount % 10
        rounded = purchaseAmount - remainder if remainder < 5 else purchaseAmount + (10 - remainder)
        return 100 - rounded
