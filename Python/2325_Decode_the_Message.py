# Author: Kaustav Ghosh
# Problem: 2325. Decode the Message
# URL: https://leetcode.com/problems/decode-the-message/
# Difficulty: Easy
#
# Approach:
# Scan the key and build a mapping: for each letter (ignoring spaces and already-mapped letters),
# map it to the next available letter starting from 'a'. Then decode the message using this map.

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {}
        next_char = ord('a')

        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = chr(next_char)
                next_char += 1

        return ''.join(mapping.get(c, ' ') for c in message)
