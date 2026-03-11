# Given a string input representing the file system, return the length of the longest
# absolute path to a file in the abstracted file system. If there is no file in the
# system, return 0. A file is a name containing a period.

# Author: Kaustav Ghosh

class Solution(object):
    def lengthLongestPath(self, input):
        stack = {0: 0}
        max_len = 0
        for line in input.split('\n'):
            depth = len(line) - len(line.lstrip('\t'))
            name = line.lstrip('\t')
            if '.' in name:
                max_len = max(max_len, stack[depth] + len(name))
            else:
                stack[depth + 1] = stack[depth] + len(name) + 1
        return max_len
