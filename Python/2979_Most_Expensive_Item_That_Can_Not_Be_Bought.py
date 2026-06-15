class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # Chicken McNugget theorem: for coprime a,b, largest non-representable = a*b - a - b
        return primeOne * primeTwo - primeOne - primeTwo
