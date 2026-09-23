# Author: Kaustav Ghosh
# Problem: Longest Uploaded Prefix
# Approach: Keep the uploaded videos in a set plus the current prefix length. An upload can only extend the prefix from where it already ends, so walk that pointer forward while the next video is present; each video moves it at most once, so the whole run of uploads costs linear time

class LUPrefix(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.uploaded = set()
        self.prefix = 0

    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        self.uploaded.add(video)
        while self.prefix + 1 in self.uploaded:
            self.prefix += 1

    def longest(self):
        """
        :rtype: int
        """
        return self.prefix
