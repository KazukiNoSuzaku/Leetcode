# Author: Kaustav Ghosh
# Problem: 1580 - Put Boxes Into the Warehouse II (Premium)
# Approach: Sort boxes, two-pointer from both warehouse ends

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        boxes.sort()
        n = len(warehouse)
        left, right = 0, n - 1

        # Preprocess warehouse from both ends
        from_left = warehouse[:]
        for i in range(1, n):
            from_left[i] = min(from_left[i], from_left[i-1])
        from_right = warehouse[:]
        for i in range(n-2, -1, -1):
            from_right[i] = min(from_right[i], from_right[i+1])

        # Effective height at each position
        effective = [max(from_left[i], from_right[i]) for i in range(n)]

        count = 0
        i = len(boxes) - 1
        left, right = 0, n - 1

        while i >= 0 and left <= right:
            if effective[left] >= boxes[i]:
                count += 1
                left += 1
                i -= 1
            elif effective[right] >= boxes[i]:
                count += 1
                right -= 1
                i -= 1
            else:
                i -= 1

        return count
