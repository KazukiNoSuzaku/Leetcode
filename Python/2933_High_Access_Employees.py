from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        emp = defaultdict(list)
        for name, t in access_times:
            emp[name].append(int(t[:2]) * 60 + int(t[2:]))
        res = []
        for name, times in emp.items():
            times.sort()
            if any(times[i + 2] - times[i] < 60 for i in range(len(times) - 2)):
                res.append(name)
        return res
