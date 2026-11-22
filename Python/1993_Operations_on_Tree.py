# Author: Kaustav Ghosh
# Problem: Operations on Tree
# Approach: Keep the owner of every locked node in one array, zero meaning unlocked, plus a child list built once from the parent array. Locking and unlocking are then single array reads guarded by the owner check. An upgrade needs three facts: the node itself is free, no ancestor is locked, and at least one descendant is locked; the ancestor walk follows parent pointers upward, while the descendant search is an explicit stack over the child lists that collects every locked node it finds. Only if a locked descendant exists are those nodes released and the node itself locked, so a failed upgrade leaves the tree untouched.

class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        self.owner = [0] * len(parent)
        self.children = [[] for _ in parent]
        for node in range(1, len(parent)):
            self.children[parent[node]].append(node)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.owner[num] != 0:
            return False
        self.owner[num] = user
        return True

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.owner[num] != user:
            return False
        self.owner[num] = 0
        return True

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.owner[num] != 0:
            return False
        ancestor = self.parent[num]
        while ancestor != -1:
            if self.owner[ancestor] != 0:
                return False
            ancestor = self.parent[ancestor]
        locked = []
        stack = list(self.children[num])
        while stack:
            node = stack.pop()
            if self.owner[node] != 0:
                locked.append(node)
            stack.extend(self.children[node])
        if not locked:
            return False
        for node in locked:
            self.owner[node] = 0
        self.owner[num] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
