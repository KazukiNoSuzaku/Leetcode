# Author: Kaustav Ghosh
# Problem: Parallel Courses III
# Approach: Unlimited courses may run at once, so a course is held up only by its own prerequisites and starts the moment the last of them finishes, which makes its completion time the longest chain of durations ending at it. Processing the courses in an order where every prerequisite comes first lets each completion time be settled once and for all, and that order is produced by repeatedly taking courses whose remaining prerequisite count has fallen to zero. As each course is finalised it offers its finishing time to its dependents, each of which keeps the latest offer it receives, so the overall answer is the largest completion time anywhere in the graph.

class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        from collections import deque
        following = [[] for _ in range(n + 1)]
        outstanding = [0] * (n + 1)
        for earlier, later in relations:
            following[earlier].append(later)
            outstanding[later] += 1

        finish = [0] * (n + 1)
        queue = deque()
        for course in range(1, n + 1):
            if outstanding[course] == 0:
                finish[course] = time[course - 1]
                queue.append(course)

        answer = 0
        while queue:
            course = queue.popleft()
            if finish[course] > answer:
                answer = finish[course]
            for later in following[course]:
                candidate = finish[course] + time[later - 1]
                if candidate > finish[later]:
                    finish[later] = candidate
                outstanding[later] -= 1
                if outstanding[later] == 0:
                    queue.append(later)
        return answer
