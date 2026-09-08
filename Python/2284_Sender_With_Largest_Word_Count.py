# Author: Kaustav Ghosh
# Problem: Sender With Largest Word Count
# Approach: Accumulate each sender's total word count across their messages, then return the sender with the most words, breaking ties by the lexicographically larger name

from collections import defaultdict


class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        totals = defaultdict(int)
        for msg, sender in zip(messages, senders):
            totals[sender] += msg.count(' ') + 1  # words = spaces + 1

        best = None
        for sender, count in totals.items():
            if best is None or count > totals[best] or (count == totals[best] and sender > best):
                best = sender
        return best
