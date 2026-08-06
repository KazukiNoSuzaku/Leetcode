# Author: Kaustav Ghosh
# Problem: Maximum Genetic Difference Query
# Approach: Answer queries offline during a DFS. A binary trie holds exactly the node values on the current root-to-node path (with counts so values can be removed on backtrack). At each node we insert it, answer its queries with a max-XOR trie walk, recurse, then remove it

class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(parents)
        BITS = 17  # values < 2^17 = 131072

        children = [[] for _ in range(n)]
        root = 0
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        # trie arrays: two children slots and a subtree count per node
        child = [[-1, -1]]
        cnt = [0]

        def insert(x):
            cur = 0
            for b in range(BITS, -1, -1):
                bit = (x >> b) & 1
                if child[cur][bit] == -1:
                    child[cur][bit] = len(child)
                    child.append([-1, -1])
                    cnt.append(0)
                cur = child[cur][bit]
                cnt[cur] += 1

        def remove(x):
            cur = 0
            for b in range(BITS, -1, -1):
                bit = (x >> b) & 1
                cur = child[cur][bit]
                cnt[cur] -= 1

        def query(x):
            cur = 0
            res = 0
            for b in range(BITS, -1, -1):
                bit = (x >> b) & 1
                want = 1 - bit
                nxt = child[cur][want]
                if nxt != -1 and cnt[nxt] > 0:
                    res |= (1 << b)
                    cur = nxt
                else:
                    cur = child[cur][bit]
            return res

        queries_at = [[] for _ in range(n)]
        for qi, (node, val) in enumerate(queries):
            queries_at[node].append((qi, val))

        ans = [0] * len(queries)
        stack = [(root, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                remove(node)
                continue
            insert(node)
            for qi, val in queries_at[node]:
                ans[qi] = query(val)
            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))
        return ans
