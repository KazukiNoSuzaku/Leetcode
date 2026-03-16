# Design a system to record tweets and query tweet counts per time delta bucket.

# Author: Kaustav Ghosh

from collections import defaultdict
import bisect

class TweetCounts(object):
    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName, time):
        bisect.insort(self.data[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        delta = {'minute': 60, 'hour': 3600, 'day': 86400}[freq]
        buckets = (endTime - startTime) // delta + 1
        res = [0] * buckets
        times = self.data[tweetName]
        lo = bisect.bisect_left(times, startTime)
        hi = bisect.bisect_right(times, endTime)
        for t in times[lo:hi]:
            res[(t - startTime) // delta] += 1
        return res
