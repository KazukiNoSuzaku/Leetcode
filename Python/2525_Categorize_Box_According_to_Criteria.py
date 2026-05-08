class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = max(length, width, height) >= 10**4 or length * width * height >= 10**9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
