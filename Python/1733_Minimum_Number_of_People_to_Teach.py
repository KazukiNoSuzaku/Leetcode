# Author: Kaustav Ghosh

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        lang_sets = [set(l) for l in languages]
        # Find friendships where no common language
        need_comm = set()
        for u, v in friendships:
            if not lang_sets[u - 1] & lang_sets[v - 1]:
                need_comm.add(u)
                need_comm.add(v)
        if not need_comm:
            return 0
        # Try each language, find min people to teach
        res = len(need_comm)
        for lang in range(1, n + 1):
            count = 0
            for person in need_comm:
                if lang not in lang_sets[person - 1]:
                    count += 1
            res = min(res, count)
        return res
