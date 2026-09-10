# Author: Kaustav Ghosh
# Problem: Calculate Amount Paid in Taxes
# Approach: Taxes are progressive: only the income falling within each bracket is taxed at that bracket's rate. Walk the brackets in order, taxing the slice of income between the previous upper bound and the current one until the income runs out

class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable = min(income, upper) - prev
            tax += taxable * percent / 100.0
            prev = upper
        return tax
