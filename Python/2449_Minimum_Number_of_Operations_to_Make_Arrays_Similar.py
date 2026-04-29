class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        # Each op changes a value by ±2, so parities are fixed.
        # Sort odd/even elements of each array and pair them greedily.
        def split(arr):
            return sorted(x for x in arr if x % 2), sorted(x for x in arr if x % 2 == 0)

        n_odd, n_even = split(nums)
        t_odd, t_even = split(target)
        total = sum(abs(a - b) for a, b in zip(n_odd, t_odd))
        total += sum(abs(a - b) for a, b in zip(n_even, t_even))
        return total // 4  # each op counted twice (source loses 2, target gains 2)
