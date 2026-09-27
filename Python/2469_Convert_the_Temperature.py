# Author: Kaustav Ghosh
# Problem: Convert the Temperature
# Approach: Apply the two conversion formulas directly: Kelvin is Celsius plus 273.15 and Fahrenheit is Celsius times 1.80 plus 32.00

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [celsius + 273.15, celsius * 1.80 + 32.00]
