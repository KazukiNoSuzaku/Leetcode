# Filter restaurants by vegan-friendly flag, max price, max distance.
# Sort by rating desc, then id desc.

# Author: Kaustav Ghosh

class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        filtered = [
            r for r in restaurants
            if (not veganFriendly or r[2] == 1)
            and r[3] <= maxPrice
            and r[4] <= maxDistance
        ]
        filtered.sort(key=lambda r: (r[1], r[0]), reverse=True)
        return [r[0] for r in filtered]
