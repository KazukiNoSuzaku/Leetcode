# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-genetic-difference-query/

from collections import defaultdict

class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(parents)
        children = defaultdict(list)
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # Group queries by node
        query_map = defaultdict(list)
        for idx, (node, val) in enumerate(queries):
            query_map[node].append((val, idx))

        ans = [0] * len(queries)

        # Trie with count
        BITS = 18
        trie = [[0, 0] for _ in range(n * BITS * 2 + 2)]
        cnt = [0] * (n * BITS * 2 + 2)
        trie_idx = [1]  # next available index

        def new_node():
            idx = trie_idx[0]
            trie_idx[0] += 1
            return idx

        def insert(num):
            node = 0
            for i in range(BITS - 1, -1, -1):
                bit = (num >> i) & 1
                if trie[node][bit] == 0:
                    trie[node][bit] = new_node()
                node = trie[node][bit]
                cnt[node] += 1

        def remove(num):
            node = 0
            for i in range(BITS - 1, -1, -1):
                bit = (num >> i) & 1
                node = trie[node][bit]
                cnt[node] -= 1

        def query(num):
            node = 0
            result = 0
            for i in range(BITS - 1, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                if trie[node][want] != 0 and cnt[trie[node][want]] > 0:
                    result |= (1 << i)
                    node = trie[node][want]
                else:
                    node = trie[node][bit]
            return result

        # DFS
        stack = [(root, False)]
        while stack:
            node, leaving = stack.pop()
            if leaving:
                remove(node)
                continue
            insert(node)
            stack.append((node, True))
            # Answer queries for this node
            for val, idx in query_map[node]:
                ans[idx] = query(val)
            for child in children[node]:
                stack.append((child, False))

        return ans
