# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Hashmap storing path to value, validate parent exists

class FileSystem(object):
    def __init__(self):
        self.paths = {"": -1}

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if path in self.paths or path == "":
            return False
        parent = path[:path.rfind('/')]
        if parent not in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        return self.paths.get(path, -1)
