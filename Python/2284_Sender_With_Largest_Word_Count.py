# Author: Kaustav Ghosh
# Problem: 2284. Sender With Largest Word Count
# URL: https://leetcode.com/problems/sender-with-largest-word-count/
# Difficulty: Medium
#
# Approach:
# Count total words per sender. Return sender with max word count,
# breaking ties by lexicographically largest name.

from collections import defaultdict

class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        count = defaultdict(int)
        for msg, sender in zip(messages, senders):
            count[sender] += len(msg.split())
        return max(count.keys(), key=lambda s: (count[s], s))
