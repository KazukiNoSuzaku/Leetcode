# Split a linked list into k parts as evenly as possible.

# Author: Kaustav Ghosh

class Solution(object):
    def splitListToParts(self, head, k):
        length = 0
        cur = head
        while cur: length += 1; cur = cur.next
        base, extra = length // k, length % k
        res = []
        cur = head
        for i in range(k):
            part_head = cur
            size = base + (1 if i < extra else 0)
            for _ in range(size - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            res.append(part_head)
        return res
