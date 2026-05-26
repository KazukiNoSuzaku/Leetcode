class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int) -> bool:
            if not s:
                return target == 0
            for i in range(1, len(s) + 1):
                if int(s[:i]) <= target and can_partition(s[i:], target - int(s[:i])):
                    return True
            return False

        return sum(i * i for i in range(1, n + 1) if can_partition(str(i * i), i))
