# RandomizedCollection is a data structure that contains a collection of numbers,
# possibly with duplicates. Implement the RandomizedCollection class with insert, remove,
# and getRandom in average O(1) time. Remove should remove one occurrence if present.

# Example 1:
# Input: ["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]
#        [[],[1],[1],[2],[],[1],[]]
# Output: [null,true,false,true,1,true,2]

# Constraints:
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made.

# Author: Kaustav Ghosh

import random
from collections import defaultdict

class RandomizedCollection(object):
    def __init__(self):
        self.val_to_idxs = defaultdict(set)
        self.vals = []

    def insert(self, val):
        self.val_to_idxs[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.val_to_idxs[val]) == 1

    def remove(self, val):
        if not self.val_to_idxs[val]:
            return False
        remove_idx = next(iter(self.val_to_idxs[val]))
        last_val = self.vals[-1]
        self.vals[remove_idx] = last_val
        self.val_to_idxs[last_val].add(remove_idx)
        self.val_to_idxs[last_val].discard(len(self.vals) - 1)
        self.val_to_idxs[val].discard(remove_idx)
        self.vals.pop()
        return True

    def getRandom(self):
        return random.choice(self.vals)
