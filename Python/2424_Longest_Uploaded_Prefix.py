class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = set()
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded.add(video)
        while self.prefix + 1 in self.uploaded:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix
