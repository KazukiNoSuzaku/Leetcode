class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        chemistry = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            chemistry += skill[i] * skill[n - 1 - i]
        return chemistry
