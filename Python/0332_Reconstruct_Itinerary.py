# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the
# departure and the arrival airports of one flight. Reconstruct the itinerary in order and
# return it. All of the tickets must be used once and only once.
# The itinerary must begin with "JFK". If there are multiple valid itineraries, return the
# itinerary that has the smallest lexical order when read as a single string.

# Example 1:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Example 2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

# Constraints:
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3, toi.length == 3

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        res = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]
