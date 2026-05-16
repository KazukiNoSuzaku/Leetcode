from collections import defaultdict

class Solution:
    def rootCount(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        guess_set = {(u, v) for u, v in guesses}

        # Count correct guesses when rooted at 0
        correct = 0
        def dfs(node, parent):
            nonlocal correct
            for child in tree[node]:
                if child != parent:
                    if (node, child) in guess_set:
                        correct += 1
                    dfs(child, node)

        dfs(0, -1)

        # Rerooting: moving root from u to v gains (v,u) if guessed, loses (u,v) if guessed
        ans = 0
        def reroot(node, parent, curr):
            nonlocal ans
            if curr >= k:
                ans += 1
            for child in tree[node]:
                if child != parent:
                    delta = ((child, node) in guess_set) - ((node, child) in guess_set)
                    reroot(child, node, curr + delta)

        reroot(0, -1, correct)
        return ans
