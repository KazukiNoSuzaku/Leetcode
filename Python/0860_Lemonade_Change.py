# Check if you can give correct change to each customer paying with 5, 10, or 20.

# Author: Kaustav Ghosh

class Solution(object):
    def lemonadeChange(self, bills):
        fives = tens = 0
        for bill in bills:
            if bill == 5: fives += 1
            elif bill == 10:
                if not fives: return False
                fives -= 1; tens += 1
            else:
                if tens and fives: tens -= 1; fives -= 1
                elif fives >= 3: fives -= 3
                else: return False
        return True
