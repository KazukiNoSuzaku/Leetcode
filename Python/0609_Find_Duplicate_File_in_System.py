# Given a list paths of directory info, return all the groups of duplicate files in the file system.
# A group of duplicate files consists of at least two files that have the same content.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        content_map = defaultdict(list)
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for f in parts[1:]:
                name, content = f.split('(')
                content = content[:-1]
                content_map[content].append(directory + '/' + name)
        return [v for v in content_map.values() if len(v) > 1]
