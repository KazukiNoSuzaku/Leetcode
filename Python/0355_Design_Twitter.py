# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
# and is able to see the 10 most recent tweets in the user's news feed.
# Implement the Twitter class with postTweet, getNewsFeed, follow, and unfollow.

# Example 1:
# Input: ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
#        [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
# Output: [null,null,[5],null,null,[6,5],null,[5]]

# Constraints:
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

# Author: Kaustav Ghosh

import heapq
from collections import defaultdict

class Twitter(object):
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId)]
        self.following = defaultdict(set) # userId -> set of followees

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # use negative for min-heap to act as max-heap

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            if self.tweets[u]:
                t, tid = self.tweets[u][-1]
                heapq.heappush(heap, (t, tid, u, len(self.tweets[u]) - 1))
        res = []
        while heap and len(res) < 10:
            t, tid, u, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                nt, ntid = self.tweets[u][idx - 1]
                heapq.heappush(heap, (nt, ntid, u, idx - 1))
        return res

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
