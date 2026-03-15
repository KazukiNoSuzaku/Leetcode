# Find videos watched by friends at exactly level hops away, sorted by frequency then name.

# Author: Kaustav Ghosh

from collections import deque, Counter

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        visited = {id}
        q = deque([id])
        for _ in range(level):
            for _ in range(len(q)):
                node = q.popleft()
                for f in friends[node]:
                    if f not in visited:
                        visited.add(f)
                        q.append(f)
        count = Counter()
        for person in q:
            for v in watchedVideos[person]:
                count[v] += 1
        return sorted(count, key=lambda x: (count[x], x))
