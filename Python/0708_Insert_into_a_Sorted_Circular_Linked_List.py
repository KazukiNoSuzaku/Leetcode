# Insert a value into a sorted circular linked list in the correct sorted position.

# Author: Kaustav Ghosh

class Solution(object):
    def insert(self, head, insertVal):
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        cur = head
        while True:
            if cur.val <= insertVal <= cur.next.val:
                break
            if cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    break
            if cur.next == head:
                break
            cur = cur.next
        node.next = cur.next
        cur.next = node
        return head
