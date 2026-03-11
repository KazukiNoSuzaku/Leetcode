# You are given a string s representing an attendance record for a student.
# Return true if the student could be rewarded based on their attendance record.
# Not awarded if: more than 1 'A' or 3 or more consecutive 'L's.

# Author: Kaustav Ghosh

class Solution(object):
    def checkRecord(self, s):
        return s.count('A') <= 1 and 'LLL' not in s
