# Author: Kaustav Ghosh
# 1117. Building H2O
# https://leetcode.com/problems/building-h2o/

import threading

class H2O(object):
    def __init__(self):
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(0)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.h_sem.acquire()
        releaseHydrogen()
        self.barrier.wait()
        self.o_sem.release()

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.o_sem.acquire()
        releaseOxygen()
        self.barrier.wait()
        self.h_sem.release()
        self.h_sem.release()
