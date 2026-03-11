# You are given an integer array nums which is a permutation of all the integers in the range [1, n].
# Given a 2D integer array sequences, check if nums is the only shortest supersequence.
# Return true if nums is the only shortest supersequence or false otherwise.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def sequenceReconstruction(self, nums, sequences):
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        all_nodes = set()
        for seq in sequences:
            for node in seq:
                all_nodes.add(node)
            for i in range(len(seq) - 1):
                if seq[i+1] not in graph[seq[i]]:
                    graph[seq[i]].add(seq[i+1])
                    in_degree[seq[i+1]] += 1
        if set(nums) != all_nodes:
            return False
        queue = deque(n for n in nums if in_degree[n] == 0)
        order = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        return order == nums
