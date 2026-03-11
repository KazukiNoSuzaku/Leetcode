# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars,
# if the group's length is 1, append the character to s. Otherwise, append the character
# followed by the group's length. The compressed string should not be returned separately,
# but instead be stored in the input character array chars.

# Author: Kaustav Ghosh

class Solution(object):
    def compress(self, chars):
        write = i = 0
        while i < len(chars):
            ch = chars[i]
            count = 0
            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write
