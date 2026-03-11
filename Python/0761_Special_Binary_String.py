# Make special binary string lexicographically largest by swapping special substrings.

# Author: Kaustav Ghosh

class Solution(object):
    def makeLargestSpecial(self, s):
        count = i = 0
        specials = []
        for j, c in enumerate(s):
            count += 1 if c == '1' else -1
            if count == 0:
                specials.append('1' + self.makeLargestSpecial(s[i+1:j]) + '0')
                i = j + 1
        return ''.join(sorted(specials, reverse=True))
