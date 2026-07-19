# Author: Kaustav Ghosh
# Problem: Sort Features by Popularity (Premium)
# Approach: Count in how many responses (distinct words per response) each feature appears, then sort by that count descending, keeping the original order for ties

from collections import Counter

class Solution(object):
    def sortFeatures(self, features, responses):
        """
        :type features: List[str]
        :type responses: List[str]
        :rtype: List[str]
        """
        feature_set = set(features)
        popularity = Counter()
        for response in responses:
            for word in set(response.split()):
                if word in feature_set:
                    popularity[word] += 1

        order = {f: i for i, f in enumerate(features)}
        return sorted(features, key=lambda f: (-popularity[f], order[f]))
