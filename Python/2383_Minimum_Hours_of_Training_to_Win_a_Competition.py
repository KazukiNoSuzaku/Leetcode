class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: list[int], experience: list[int]) -> int:
        hours = 0
        e, exp = initialEnergy, initialExperience
        for en, ex in zip(energy, experience):
            if e <= en:
                hours += en - e + 1
                e = en + 1
            if exp <= ex:
                hours += ex - exp + 1
                exp = ex + 1
            e -= en
            exp += ex
        return hours
