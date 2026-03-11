# Design an in-memory file system to simulate the following functions:
# ls, mkdir, addContentToFile, readContentFromFile

# Author: Kaustav Ghosh

class FileSystem(object):
    def __init__(self):
        self.dirs = {'': {'files': {}, 'dirs': set()}}

    def _traverse(self, path):
        node = self.dirs['']
        if path == '/': return node
        for part in path.split('/')[1:]:
            if part not in self.dirs:
                self.dirs[part] = {'files': {}, 'dirs': set()}
            node = self.dirs[part]
        return node

    def ls(self, path):
        node = self._traverse(path)
        return sorted(list(node['dirs']) + list(node['files'].keys()))

    def mkdir(self, path):
        node = self.dirs['']
        parts = path.split('/')[1:]
        for i, part in enumerate(parts):
            node['dirs'].add(part)
            key = '/'.join(parts[:i+1])
            if key not in self.dirs:
                self.dirs[key] = {'files': {}, 'dirs': set()}
            node = self.dirs[key]

    def addContentToFile(self, filePath, content):
        parts = filePath.split('/')
        dirPath = '/'.join(parts[:-1])
        fname = parts[-1]
        if dirPath: self.mkdir(dirPath)
        node = self._traverse(dirPath if dirPath else '/')
        node['files'][fname] = node['files'].get(fname, '') + content

    def readContentFromFile(self, filePath):
        parts = filePath.split('/')
        dirPath = '/'.join(parts[:-1])
        node = self._traverse(dirPath if dirPath else '/')
        return node['files'][parts[-1]]
