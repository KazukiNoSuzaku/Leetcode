# Author: Kaustav Ghosh
# Problem: Minimum Number of People to Teach
# Approach: Only users in a friendship with no shared language matter; teaching one language, the best choice is the one most of them already know, so the answer is (broken users) - (max already knowing a language)

from collections import Counter

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        known = [set(langs) for langs in languages]

        broken = set()
        for u, v in friendships:
            if not (known[u - 1] & known[v - 1]):
                broken.add(u - 1)
                broken.add(v - 1)

        if not broken:
            return 0

        counts = Counter()
        for user in broken:
            for lang in known[user]:
                counts[lang] += 1

        already = max(counts.values()) if counts else 0
        return len(broken) - already
