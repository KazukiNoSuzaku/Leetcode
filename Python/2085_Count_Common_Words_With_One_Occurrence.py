# Author: Kaustav Ghosh
# Problem 2085: Count Common Words With One Occurrence

from collections import Counter

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        count1 = Counter(words1)
        count2 = Counter(words2)
        result = 0
        for word in count1:
            if count1[word] == 1 and count2.get(word, 0) == 1:
                result += 1
        return result
