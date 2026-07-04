# Author: Kaustav Ghosh
# Problem: Design Parking System
# Approach: Keep remaining slots indexed by car type (1/2/3); addCar consumes one if available, otherwise rejects

class ParkingSystem(object):
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.slots = [0, big, medium, small]  # index 0 unused

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False
