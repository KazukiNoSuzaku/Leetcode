# Author: Kaustav Ghosh
# Problem: Making File Names Unique
# Approach: Hashmap tracking next suffix number per name

class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        used = {}
        result = []
        for name in names:
            if name not in used:
                used[name] = 1
                result.append(name)
            else:
                k = used[name]
                new_name = "{}({})".format(name, k)
                while new_name in used:
                    k += 1
                    new_name = "{}({})".format(name, k)
                used[name] = k + 1
                used[new_name] = 1
                result.append(new_name)
        return result
