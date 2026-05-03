from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Monotonic decreasing stack: a node survives only if no greater value follows it.
        stack = []
        node = head
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next

        dummy = ListNode(0)
        cur = dummy
        for n in stack:
            cur.next = n
            cur = cur.next
        cur.next = None
        return dummy.next
