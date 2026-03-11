# We define str = [s, n] as the string str which consists of the string s concatenated n times.
# We define that string s1 can be obtained from string s2 if we can remove some characters from s2
# such that the remaining characters form the string s1.
# Given four integers n1, n2 and two strings s1 and s2, return the maximum integer m such that
# str = [s2, m] can be obtained from str = [s1, n1].

# Author: Kaustav Ghosh

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if not set(s2).issubset(set(s1)):
            return 0
        s1_count = s2_count = 0
        s2_idx = 0
        recall = {}
        while s1_count < n1:
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_count += 1
                        s2_idx = 0
            s1_count += 1
            if s2_idx in recall:
                prev_s1, prev_s2 = recall[s2_idx]
                cycle_s1 = s1_count - prev_s1
                cycle_s2 = s2_count - prev_s2
                remaining = (n1 - s1_count) // cycle_s1
                s2_count += remaining * cycle_s2
                s1_count += remaining * cycle_s1
            else:
                recall[s2_idx] = (s1_count, s2_count)
        return s2_count // n2
