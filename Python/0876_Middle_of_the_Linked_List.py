# Return the middle node of a linked list (second middle if even length).

# Author: Kaustav Ghosh

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
