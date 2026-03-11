# Given an integer array data representing the data, return whether it is a valid UTF-8 encoding.
# A character in UTF-8 can be from 1 to 4 bytes long.

# Author: Kaustav Ghosh

class Solution(object):
    def validUtf8(self, data):
        i = 0
        while i < len(data):
            byte = data[i]
            if byte >> 7 == 0:
                n = 0
            elif byte >> 5 == 0b110:
                n = 1
            elif byte >> 4 == 0b1110:
                n = 2
            elif byte >> 3 == 0b11110:
                n = 3
            else:
                return False
            for j in range(1, n + 1):
                if i + j >= len(data) or data[i + j] >> 6 != 0b10:
                    return False
            i += n + 1
        return True
