# Author: Kaustav Ghosh
# Problem: Smallest Missing Genetic Value in Each Subtree
# Approach: A subtree that does not contain the value one has one as its smallest missing value, so only the nodes on the path from the node holding one up to the root can ever answer anything else. Walking that path upward, each step adds exactly the nodes not already accounted for, so a visited marker keeps the total collection work linear rather than re-scanning each growing subtree. The smallest missing value only ever increases along that upward walk, so a single pointer is nudged forward past every value already collected, and the subtree search uses an explicit stack because the path can be a hundred thousand nodes deep.

class Solution(object):
    def smallestMissingValueSubtree(self, parents, nums):
        """
        :type parents: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        total = len(parents)
        answer = [1] * total
        holder = -1
        for node, value in enumerate(nums):
            if value == 1:
                holder = node
                break
        if holder == -1:
            return answer

        children = [[] for _ in range(total)]
        for node in range(1, total):
            children[parents[node]].append(node)

        collected = set()
        visited = [False] * total
        missing = 1
        node = holder
        while node != -1:
            stack = [node]
            while stack:
                current = stack.pop()
                if visited[current]:
                    continue
                visited[current] = True
                collected.add(nums[current])
                stack.extend(children[current])
            while missing in collected:
                missing += 1
            answer[node] = missing
            node = parents[node]
        return answer
