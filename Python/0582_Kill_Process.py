# Given n processes with pid and ppid, kill a process and all its children.
# Return a list of process ids that will be killed.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        children = defaultdict(list)
        for c, p in zip(pid, ppid):
            children[p].append(c)
        res = []
        queue = deque([kill])
        while queue:
            p = queue.popleft()
            res.append(p)
            queue.extend(children[p])
        return res
