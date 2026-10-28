# Author: Kaustav Ghosh
# Problem: Minimum Number of People to Teach
# Approach: Only one language may be taught, and friendships that already share a language can never be broken by teaching, so the first step is to isolate the people involved in at least one failing friendship; nobody outside that set ever needs teaching. For a given choice of language the cost is then simply how many of those people do not already know it, since teaching it to all of them makes every failing friendship work and cannot harm the others. Trying all n languages against that set gives the minimum, and using sets of known languages keeps each membership test constant.

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        known = [None] + [set(spoken) for spoken in languages]

        needy = set()
        for u, v in friendships:
            if not (known[u] & known[v]):
                needy.add(u)
                needy.add(v)

        if not needy:
            return 0
        best = len(needy)
        for language in range(1, n + 1):
            missing = sum(1 for person in needy if language not in known[person])
            if missing < best:
                best = missing
        return best
