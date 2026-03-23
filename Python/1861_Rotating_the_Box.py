# Author: Kaustav Ghosh
# Problem 1861: Rotating the Box

class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(box), len(box[0])
        # Apply gravity: move stones to the right
        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    empty = j - 1
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][empty] = '#'
                    empty -= 1
        # Rotate 90 degrees clockwise
        result = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box[i][j]
        return result
