# You are given a doubly linked list which in addition to the next and previous pointers,
# it could have a child pointer, which may or may not point to a separate doubly linked list.
# Flatten the list so that all the nodes appear in a single-level, doubly linked list.

# Author: Kaustav Ghosh

class Solution(object):
    def flatten(self, head):
        cur = head
        while cur:
            if cur.child:
                child = cur.child
                next_node = cur.next
                cur.next = child
                child.prev = cur
                cur.child = None
                tail = child
                while tail.next:
                    tail = tail.next
                tail.next = next_node
                if next_node:
                    next_node.prev = tail
            cur = cur.next
        return head
