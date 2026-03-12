# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Lock-based traffic light with current green road tracking

import threading

class TrafficLight(object):
    def __init__(self):
        self.current_green = 1  # road 1 is green initially
        self.lock = threading.Lock()

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        """
        :type carId: int
        :type roadId: int
        :type direction: int
        :type turnGreen: callable
        :type crossCar: callable
        :rtype: None
        """
        with self.lock:
            if self.current_green != roadId:
                turnGreen()
                self.current_green = roadId
            crossCar()
