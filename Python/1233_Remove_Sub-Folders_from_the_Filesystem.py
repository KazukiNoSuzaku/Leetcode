# Author: Kaustav Ghosh
# Sort folders, skip any that start with previous folder prefix

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            if not folder[i].startswith(result[-1] + '/'):
                result.append(folder[i])
        return result
