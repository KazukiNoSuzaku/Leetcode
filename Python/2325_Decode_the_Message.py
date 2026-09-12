# Author: Kaustav Ghosh
# Problem: Decode the Message
# Approach: The substitution table maps the first 26 distinct non-space letters of key (in order of appearance) to 'a'..'z'. Build that mapping, then translate each message character, leaving spaces unchanged

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {}
        nxt = ord('a')
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = chr(nxt)
                nxt += 1
        return "".join(' ' if ch == ' ' else mapping[ch] for ch in message)
