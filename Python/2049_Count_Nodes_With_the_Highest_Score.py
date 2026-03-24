# Author: Kaustav Ghosh
# Problem 2049: Count Nodes With the Highest Score

class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        subtree_size = [0] * n

        # Post-order to compute subtree sizes
        stack = [(0, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                subtree_size[node] = 1
                for child in children[node]:
                    subtree_size[node] += subtree_size[child]
            else:
                stack.append((node, True))
                for child in children[node]:
                    stack.append((child, False))

        max_score = 0
        count = 0
        for i in range(n):
            score = 1
            remaining = n - 1
            for child in children[i]:
                score *= subtree_size[child]
                remaining -= subtree_size[child]
            if remaining > 0:
                score *= remaining
            if score > max_score:
                max_score = score
                count = 1
            elif score == max_score:
                count += 1
        return count
