# Author: Kaustav Ghosh
# Problem: 2288. Apply Discount to Prices
# URL: https://leetcode.com/problems/apply-discount-to-prices/
# Difficulty: Medium
#
# Approach:
# Split sentence by spaces. For each word starting with '$' followed by digits,
# apply discount and format to 2 decimal places.

class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        words = sentence.split()
        result = []
        for word in words:
            if word[0] == '$' and len(word) > 1 and word[1:].isdigit():
                price = int(word[1:])
                new_price = price * (100 - discount) / 100.0
                result.append('$%.2f' % new_price)
            else:
                result.append(word)
        return ' '.join(result)
