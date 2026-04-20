import heapq

class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_rating = {}
        self.food_cuisine = {}
        self.cuisine_heap = {}  # cuisine -> min-heap of (-rating, food)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_rating[f] = r
            self.food_cuisine[f] = c
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        c = self.food_cuisine[food]
        heapq.heappush(self.cuisine_heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        while True:
            neg_r, food = heap[0]
            if -neg_r == self.food_rating[food]:
                return food
            heapq.heappop(heap)
