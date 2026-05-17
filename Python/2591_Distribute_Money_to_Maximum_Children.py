class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children  # give each child 1 dollar baseline
        eights = min(money // 7, children)
        money -= eights * 7
        remaining = children - eights
        # If no leftover but one child got 4 total (baseline 1 + 3 extra = 4), fix it
        if remaining == 0 and money > 0:
            eights -= 1
        elif remaining == 1 and money == 3:
            eights -= 1
        return eights
