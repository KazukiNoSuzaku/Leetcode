# Author: Kaustav Ghosh
# Problem: Operations on Tree
# Approach: Track each node's locking user (or -1). lock/unlock are direct checks. upgrade succeeds only when the node is unlocked, has no locked ancestor (walk up parents), and has at least one locked descendant (scan the subtree); on success it locks the node and clears every locked descendant

class LockingTree(object):
    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        self.locked = [-1] * len(parent)
        self.children = [[] for _ in range(len(parent))]
        for node, par in enumerate(parent):
            if par != -1:
                self.children[par].append(node)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] != -1:
            return False

        # no locked ancestor
        anc = self.parent[num]
        while anc != -1:
            if self.locked[anc] != -1:
                return False
            anc = self.parent[anc]

        # collect locked descendants
        locked_descendants = []
        stack = list(self.children[num])
        while stack:
            node = stack.pop()
            if self.locked[node] != -1:
                locked_descendants.append(node)
            stack.extend(self.children[node])

        if not locked_descendants:
            return False

        for node in locked_descendants:
            self.locked[node] = -1
        self.locked[num] = user
        return True
