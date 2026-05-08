class DataStream:
    def __init__(self, value: int, k: int):
        # Track how many consecutive elements at the tail of the stream equal value.
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k
