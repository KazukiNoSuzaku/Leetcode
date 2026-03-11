# You are given a license key represented as a string s that consists of only alphanumeric
# characters and dashes. The string is separated into n + 1 groups by n dashes.
# Reformat the key by grouping k characters after removing dashes; first group may be shorter.

# Author: Kaustav Ghosh

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()
        first = len(s) % k
        parts = []
        if first:
            parts.append(s[:first])
        for i in range(first, len(s), k):
            parts.append(s[i:i+k])
        return '-'.join(parts)
