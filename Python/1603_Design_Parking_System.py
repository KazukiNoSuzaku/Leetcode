# Author: Kaustav Ghosh
# Problem: 1603 - Design Parking System
# Approach: Track counts per size

class ParkingSystem(object):
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spaces = [0, big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.spaces[carType] > 0:
            self.spaces[carType] -= 1
            return True
        return False
