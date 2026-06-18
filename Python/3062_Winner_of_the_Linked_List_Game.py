from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even_wins = odd_wins = 0
        curr = head
        while curr and curr.next:
            if curr.val > curr.next.val:
                even_wins += 1
            elif curr.next.val > curr.val:
                odd_wins += 1
            curr = curr.next.next
        if even_wins > odd_wins:
            return "Even"
        if odd_wins > even_wins:
            return "Odd"
        return "Tie"
