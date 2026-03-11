# There are buckets buckets of liquid, where exactly one of them is poisonous.
# To figure out which one is poisonous, you can feed some number of (poor) pigs the liquid.
# Each pig can drink any number of buckets in minutesToTest / minutesToDie rounds.
# Return the minimum number of pigs needed to figure out the poisonous bucket.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        rounds = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets) / math.log(rounds + 1))
