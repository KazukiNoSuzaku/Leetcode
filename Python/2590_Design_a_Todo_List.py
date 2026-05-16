class TodoList:
    def __init__(self):
        self.tasks = {}   # userId -> list of [taskId, dueDate, task, tags, done]
        self.next_id = 1

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: list[str]) -> int:
        tid = self.next_id
        self.next_id += 1
        self.tasks.setdefault(userId, []).append([tid, dueDate, taskDescription, set(tags), False])
        return tid

    def getAllTasks(self, userId: int) -> list[str]:
        user_tasks = self.tasks.get(userId, [])
        active = [t for t in user_tasks if not t[4]]
        active.sort(key=lambda t: t[1])
        return [t[2] for t in active]

    def getTasksForTag(self, userId: int, tag: str) -> list[str]:
        user_tasks = self.tasks.get(userId, [])
        active = [t for t in user_tasks if not t[4] and tag in t[3]]
        active.sort(key=lambda t: t[1])
        return [t[2] for t in active]

    def completeTask(self, userId: int, taskId: int) -> None:
        for t in self.tasks.get(userId, []):
            if t[0] == taskId:
                t[4] = True
                return
