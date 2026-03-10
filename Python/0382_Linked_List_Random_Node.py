# Given a singly linked list, return a random node's value from the linked list.
# Each node must have the same probability of being chosen.
# Implement the Solution class with getRandom() returning a random value.
# The linked list is very large and its length is unknown to you.

# Constraints:
# The number of nodes in the linked list will be in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# At most 10^4 calls will be made to getRandom.

# Author: Kaustav Ghosh

import random

class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        # Reservoir sampling
        result = None
        node = self.head
        i = 1
        while node:
            if random.randint(1, i) == 1:
                result = node.val
            node = node.next
            i += 1
        return result
