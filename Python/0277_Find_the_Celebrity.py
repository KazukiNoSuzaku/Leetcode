# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may
# exist one celebrity. The definition of a celebrity is that all the other n - 1 people know them
# but they do not know any of them.
# You are given a helper function knows(a, b) which tells you whether a knows b.
# Return the label of the celebrity, if there is one, or -1.

# Example 1:
# Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
# Output: 1

# Constraints:
# n == graph.length == graph[i].length
# 2 <= n <= 100
# graph[i][j] is 0 or 1.
# graph[i][i] == 1

# Author: Kaustav Ghosh

def knows(a, b):
    pass  # provided by judge

class Solution(object):
    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
        return candidate
