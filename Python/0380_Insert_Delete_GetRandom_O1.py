# Implement the RandomizedSet class:
# - RandomizedSet() Initializes the RandomizedSet object.
# - bool insert(int val) Inserts an item val into the set if not present.
# - bool remove(int val) Removes an item val from the set if present.
# - int getRandom() Returns a random element from the current set of elements.
# Each function must work in average O(1) time complexity.

# Example 1:
# Input: ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
#        [[],[1],[2],[2],[],[1],[2],[]]
# Output: [null,true,false,true,2,true,false,2]

# Constraints:
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# Author: Kaustav Ghosh

import random

class RandomizedSet(object):
    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val):
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last = self.vals[-1]
        self.vals[idx] = last
        self.val_to_idx[last] = idx
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self):
        return random.choice(self.vals)
