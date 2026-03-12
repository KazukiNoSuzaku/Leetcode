# Author: Kaustav Ghosh
# Sort products, binary search for prefix match at each typed character

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        import bisect
        products.sort()
        result = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            idx = bisect.bisect_left(products, prefix)
            suggestions = []
            for i in range(idx, min(idx + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)
        return result
