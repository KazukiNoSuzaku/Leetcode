# Author: Kaustav Ghosh
class Solution(object):
    def calculateTax(self, brackets, income):
        # type: (List[List[int]], int) -> float
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable = min(income, upper) - prev
            tax += taxable * percent / 100.0
            prev = upper
        return tax
