# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Semaphore-based bounded blocking queue

import threading
from collections import deque

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue = deque()
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.lock = threading.Lock()

    def enqueue(self, element):
        """
        :type element: int
        :rtype: None
        """
        self.pushing.acquire()
        with self.lock:
            self.queue.append(element)
        self.pulling.release()

    def dequeue(self):
        """
        :rtype: int
        """
        self.pulling.acquire()
        with self.lock:
            val = self.queue.popleft()
        self.pushing.release()
        return val

    def size(self):
        """
        :rtype: int
        """
        with self.lock:
            return len(self.queue)
