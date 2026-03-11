# Remove block and line comments from C++ source code.

# Author: Kaustav Ghosh

class Solution(object):
    def removeComments(self, source):
        res = []
        in_block = False
        current = ''
        for line in source:
            i = 0
            if not in_block: current = ''
            while i < len(line):
                if in_block:
                    if line[i:i+2] == '*/':
                        in_block = False
                        i += 2
                    else:
                        i += 1
                elif line[i:i+2] == '/*':
                    in_block = True
                    i += 2
                elif line[i:i+2] == '//':
                    break
                else:
                    current += line[i]
                    i += 1
            if not in_block and current:
                res.append(current)
        return res
