# Author: Kaustav Ghosh
# Dining philosophers with semaphore limiting concurrent eaters

import threading

class DiningPhilosophers(object):
    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]
        self.limit = threading.Semaphore(4)  # limit to 4 to prevent deadlock

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5
        self.limit.acquire()
        self.locks[left].acquire()
        self.locks[right].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.locks[right].release()
        self.locks[left].release()
        self.limit.release()
