# Design a data structure that accepts a stream of integers and checks if it has a pair of
# integers that sum up to a particular value.
# Implement the TwoSum class:
# - TwoSum() Initializes the TwoSum object with an empty array.
# - void add(int number) Adds number to the data structure.
# - boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value.

# Example 1:
# Input: ["TwoSum","add","add","add","find","find"]
#        [[],[1],[3],[5],[4],[7]]
# Output: [null,null,null,null,true,false]

# Constraints:
# -10^5 <= number <= 10^5
# -2^31 <= value <= 2^31 - 1
# At most 10^4 calls will be made to add and find.

# Author: Kaustav Ghosh

class TwoSum(object):
    def __init__(self):
        self.count = {}

    def add(self, number):
        self.count[number] = self.count.get(number, 0) + 1

    def find(self, value):
        for n in self.count:
            complement = value - n
            if complement != n:
                if complement in self.count:
                    return True
            elif self.count[n] >= 2:
                return True
        return False
