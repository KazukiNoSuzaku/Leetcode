# Author: Kaustav Ghosh
# Problem: Minimum Hours of Training to Win a Competition
# Approach: Energy only ever drops, so it must start above the total energy of all opponents. Experience only grows, so walk the opponents in order and whenever the current experience is not strictly greater than the opponent's, train just enough to exceed it by one before absorbing their experience

class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        hours = max(0, sum(energy) + 1 - initialEnergy)
        current = initialExperience
        for opponent in experience:
            if current <= opponent:
                hours += opponent + 1 - current
                current = opponent + 1
            current += opponent
        return hours
