class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        ans_id, best = logs[0][0], logs[0][1]
        for i in range(1, len(logs)):
            duration = logs[i][1] - logs[i - 1][1]
            eid = logs[i][0]
            if duration > best or (duration == best and eid < ans_id):
                ans_id, best = eid, duration
        return ans_id
