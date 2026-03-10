# Given a string s represents the serialization of a nested list, implement a parser
# to deserialize it and return the deserialized NestedInteger.
# Each element is either an integer or a list whose elements may also be integers or other lists.

# Example 1:
# Input: s = "324"
# Output: 324

# Example 2:
# Input: s = "[123,[456,[789]]]"
# Output: [123,[456,[789]]]

# Constraints:
# 1 <= s.length <= 5 * 10^4
# s consists of digits, square brackets "[]", negative sign '-', and commas ','.
# s is the serialization of valid NestedInteger.
# All the values in the input are in the range [-10^6, 10^6].

# Author: Kaustav Ghosh

class Solution(object):
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        cur = None
        num_start = None
        for i, ch in enumerate(s):
            if ch == '[':
                if cur is not None:
                    stack.append(cur)
                cur = NestedInteger()
                num_start = None
            elif ch == ']':
                if num_start is not None:
                    cur.add(NestedInteger(int(s[num_start:i])))
                    num_start = None
                if stack:
                    top = stack.pop()
                    top.add(cur)
                    cur = top
            elif ch == ',':
                if num_start is not None:
                    cur.add(NestedInteger(int(s[num_start:i])))
                    num_start = None
            else:
                if num_start is None:
                    num_start = i
        return cur
