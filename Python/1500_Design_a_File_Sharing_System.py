# Author: Kaustav Ghosh
# Problem: Design a File Sharing System (Premium)
# Approach: Track chunk owners with sorted sets, reuse user IDs with min-heap

import heapq
from collections import defaultdict

class Solution(object):
    pass

class FileSharing(object):

    def __init__(self, m):
        """
        :type m: int
        """
        self.m = m
        self.next_id = 1
        self.available_ids = []
        self.user_chunks = {}  # user_id -> set of chunks
        self.chunk_owners = defaultdict(set)  # chunk -> set of user_ids

    def join(self, ownedChunks):
        """
        :type ownedChunks: List[int]
        :rtype: int
        """
        if self.available_ids:
            user_id = heapq.heappop(self.available_ids)
        else:
            user_id = self.next_id
            self.next_id += 1
        self.user_chunks[user_id] = set(ownedChunks)
        for chunk in ownedChunks:
            self.chunk_owners[chunk].add(user_id)
        return user_id

    def leave(self, userID):
        """
        :type userID: int
        :rtype: None
        """
        if userID in self.user_chunks:
            for chunk in self.user_chunks[userID]:
                self.chunk_owners[chunk].discard(userID)
            del self.user_chunks[userID]
            heapq.heappush(self.available_ids, userID)

    def request(self, userID, chunkID):
        """
        :type userID: int
        :type chunkID: int
        :rtype: List[int]
        """
        owners = sorted(self.chunk_owners[chunkID])
        if owners:
            self.user_chunks[userID].add(chunkID)
            self.chunk_owners[chunkID].add(userID)
        return owners
