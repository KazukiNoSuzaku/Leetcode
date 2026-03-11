# Merge accounts sharing emails using Union-Find.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name
                union(email, acc[1])
        groups = defaultdict(list)
        for email in email_to_name:
            groups[find(email)].append(email)
        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]
