# Author: Kaustav Ghosh
# Problem: Guess the Majority in a Hidden Array (Premium, Interactive)
# Approach: XOR trick — query(1,2,3,i) XOR query(0,1,2,3) = arr[0] XOR arr[i]; group indices by match with arr[0]

class Solution(object):
    def guessMajority(self, reader):
        """
        :type reader: ArrayReader
        :rtype: int
        """
        n = reader.length()
        q0123 = reader.query(0, 1, 2, 3)

        same = [0]
        diff = []

        for i in range(4, n):
            if reader.query(1, 2, 3, i) == q0123:
                same.append(i)
            else:
                diff.append(i)

        if n >= 5:
            ref = reader.query(1, 2, 3, 4)
            for idx, qi in [
                (1, reader.query(0, 2, 3, 4)),
                (2, reader.query(0, 1, 3, 4)),
                (3, reader.query(0, 1, 2, 4)),
            ]:
                if qi == ref:
                    same.append(idx)
                else:
                    diff.append(idx)
        else:
            if q0123 == 0:
                same.extend([1, 2, 3])

        if len(same) > len(diff):
            return same[0]
        if len(diff) > len(same):
            return diff[0]
        return -1
