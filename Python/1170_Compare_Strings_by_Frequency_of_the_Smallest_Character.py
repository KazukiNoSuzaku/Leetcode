# Author: Kaustav Ghosh
# Precompute f values for words, use binary search for each query

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        import bisect

        def f(s):
            return s.count(min(s))

        word_freqs = sorted(f(w) for w in words)
        result = []
        for q in queries:
            fq = f(q)
            idx = bisect.bisect_right(word_freqs, fq)
            result.append(len(word_freqs) - idx)
        return result
