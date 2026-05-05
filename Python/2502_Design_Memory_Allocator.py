class Allocator:
    def __init__(self, n: int):
        self.mem = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i <= self.n - size:
            if self.mem[i] != 0:
                i += 1
                continue
            j = i
            while j < i + size and self.mem[j] == 0:
                j += 1
            if j == i + size:
                self.mem[i:j] = [mID] * size
                return i
            i = j
        return -1

    def mFree(self, mID: int) -> int:
        freed = self.mem.count(mID)
        self.mem = [0 if x == mID else x for x in self.mem]
        return freed
