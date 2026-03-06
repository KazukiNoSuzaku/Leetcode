# Design an algorithm to encode a list of strings to a string. The encoded string is then
# sent over the network and decoded back to the original list of strings.

# Example 1:
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]

# Example 2:
# Input: dummy_input = [""]
# Output: [""]

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.

# Author: Kaustav Ghosh

class Codec:
    def encode(self, strs):
        return ''.join('{:04d}#{}'.format(len(s), s) for s in strs)

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            length = int(s[i:i+4])
            i += 5
            res.append(s[i:i+length])
            i += length
        return res
