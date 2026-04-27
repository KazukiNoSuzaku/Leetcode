class Solution:
    def countTime(self, time: str) -> int:
        count = 0
        for h in range(24):
            for m in range(60):
                s = f"{h:02d}:{m:02d}"
                if all(time[i] == '?' or time[i] == s[i] for i in range(5)):
                    count += 1
        return count
