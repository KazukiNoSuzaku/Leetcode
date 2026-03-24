# Author: Kaustav Ghosh
# Problem 2058: Find the Minimum and Maximum Number of Nodes Between Critical Points

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        critical = []
        prev = head
        curr = head.next
        idx = 1
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(idx)
            prev = curr
            curr = curr.next
            idx += 1

        if len(critical) < 2:
            return [-1, -1]

        min_dist = float('inf')
        for i in range(1, len(critical)):
            min_dist = min(min_dist, critical[i] - critical[i - 1])
        max_dist = critical[-1] - critical[0]
        return [min_dist, max_dist]
