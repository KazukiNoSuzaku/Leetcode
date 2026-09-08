# Author: Kaustav Ghosh
# Problem: Apply Discount to Prices
# Approach: Split into words. A word is a price when it starts with '$' and the remainder is a non-empty run of digits. For each price, apply the discount and reformat to two decimals with a leading '$'; leave other words unchanged

class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        factor = (100 - discount) / 100.0
        words = sentence.split(' ')
        for i, w in enumerate(words):
            if len(w) > 1 and w[0] == '$' and w[1:].isdigit():
                value = int(w[1:]) * factor
                words[i] = "${:.2f}".format(value)
        return " ".join(words)
