# Author: Kaustav Ghosh
# Problem: Design Video Sharing Platform
# Approach: Store videos in a dict keyed by id, tracking content plus views/likes/dislikes. Assign the smallest free id: reuse released ids from a min-heap, otherwise hand out the next fresh counter value. watch returns the clamped substring and bumps views; all queries return the sentinel form when the id is absent

import heapq


class VideoSharingPlatform(object):
    def __init__(self):
        self.videos = {}          # id -> [content, views, likes, dislikes]
        self.freed = []           # min-heap of reusable ids
        self.next_id = 0

    def upload(self, video):
        """
        :type video: str
        :rtype: int
        """
        if self.freed:
            vid = heapq.heappop(self.freed)
        else:
            vid = self.next_id
            self.next_id += 1
        self.videos[vid] = [video, 0, 0, 0]
        return vid

    def remove(self, videoId):
        """
        :type videoId: int
        :rtype: None
        """
        if videoId in self.videos:
            del self.videos[videoId]
            heapq.heappush(self.freed, videoId)

    def watch(self, videoId, startMinute, endMinute):
        """
        :type videoId: int
        :type startMinute: int
        :type endMinute: int
        :rtype: str
        """
        if videoId not in self.videos:
            return "-1"
        v = self.videos[videoId]
        v[1] += 1
        end = min(endMinute, len(v[0]) - 1)
        return v[0][startMinute:end + 1]

    def like(self, videoId):
        """
        :type videoId: int
        :rtype: None
        """
        if videoId in self.videos:
            self.videos[videoId][2] += 1

    def dislike(self, videoId):
        """
        :type videoId: int
        :rtype: None
        """
        if videoId in self.videos:
            self.videos[videoId][3] += 1

    def getLikesAndDislikes(self, videoId):
        """
        :type videoId: int
        :rtype: List[int]
        """
        if videoId not in self.videos:
            return [-1]
        v = self.videos[videoId]
        return [v[2], v[3]]

    def getViews(self, videoId):
        """
        :type videoId: int
        :rtype: int
        """
        if videoId not in self.videos:
            return -1
        return self.videos[videoId][1]
