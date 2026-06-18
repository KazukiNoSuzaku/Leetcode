from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = head
        while curr:
            freq = 1
            while curr.next and curr.next.val == curr.val:
                freq += 1
                curr = curr.next
            tail.next = ListNode(freq)
            tail = tail.next
            curr = curr.next
        return dummy.next
