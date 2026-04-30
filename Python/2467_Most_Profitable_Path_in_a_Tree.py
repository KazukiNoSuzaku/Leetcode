from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Find Bob's path to root and record his arrival time at each node
        bob_time = {}

        def find_bob(node, parent, t):
            if node == 0:
                bob_time[node] = t
                return True
            for nei in adj[node]:
                if nei != parent and find_bob(nei, node, t + 1):
                    bob_time[node] = t
                    return True
            return False

        find_bob(bob, -1, 0)

        # Alice's DFS from root: maximize income, collect based on timing vs Bob
        ans = float('-inf')

        def dfs(node, parent, t, income):
            nonlocal ans
            if node in bob_time:
                if t < bob_time[node]:
                    income += amount[node]
                elif t == bob_time[node]:
                    income += amount[node] // 2
                # Bob was here first: +0
            else:
                income += amount[node]
            children = [nei for nei in adj[node] if nei != parent]
            if not children:
                ans = max(ans, income)
            for nei in children:
                dfs(nei, node, t + 1, income)

        dfs(0, -1, 0, 0)
        return ans
