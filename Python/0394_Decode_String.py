# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square
# brackets is being repeated exactly k times.

# Author: Kaustav Ghosh

class Solution(object):
    def decodeString(self, s):
        stack = []
        cur_str = ''
        cur_num = 0
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur_str, cur_num))
                cur_str = ''
                cur_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                cur_str = prev_str + num * cur_str
            else:
                cur_str += ch
        return cur_str
