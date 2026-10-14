# Author: Kaustav Ghosh
# Problem: Design Parking System
# Approach: Nothing about which particular car took which particular space ever matters, only how many spaces of each size are left, so the whole state is three counters held in one list indexed by car type. Parking is then a check and a decrement in constant time and constant space.

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        # Indexed by carType, so slot 0 is unused.
        self.free = [0, big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.free[carType] == 0:
            return False
        self.free[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
