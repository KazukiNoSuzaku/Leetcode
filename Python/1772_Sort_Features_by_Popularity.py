# Author: Kaustav Ghosh
# Problem: Sort Features by Popularity
# Approach: A feature repeated inside one response still counts once, so each response is reduced to the set of distinct words it mentions before the tallies are incremented. Sorting the features by the negated tally then puts the most popular first, and because Python's sort is stable the features that tie keep the order they had in the input, which is exactly the required tie-break — no index needs to be carried along.

class Solution(object):
    def sortFeatures(self, features, responses):
        """
        :type features: List[str]
        :type responses: List[str]
        :rtype: List[str]
        """
        from collections import Counter

        popularity = Counter()
        for response in responses:
            popularity.update(set(response.split()))
        return sorted(features, key=lambda feature: -popularity[feature])
