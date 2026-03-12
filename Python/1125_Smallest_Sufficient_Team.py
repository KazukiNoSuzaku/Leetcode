# Author: Kaustav Ghosh
# 1125. Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/

class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        skill_idx = {s: i for i, s in enumerate(req_skills)}
        n = len(req_skills)
        full = (1 << n) - 1

        # dp[mask] = list of people who cover exactly mask skills
        dp = {0: []}
        for i, skills in enumerate(people):
            mask = 0
            for s in skills:
                if s in skill_idx:
                    mask |= (1 << skill_idx[s])
            for state, team in list(dp.items()):
                new_state = state | mask
                if new_state not in dp or len(dp[new_state]) > len(team) + 1:
                    dp[new_state] = team + [i]

        return dp[full]
