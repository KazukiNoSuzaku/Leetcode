# Author: Kaustav Ghosh

class Solution(object):
    def cellsInRange(self, s):
        # type: (str) -> List[str]
        result = []
        for col in range(ord(s[0]), ord(s[3]) + 1):
            for row in range(int(s[1]), int(s[4]) + 1):
                result.append(chr(col) + str(row))
        return result
