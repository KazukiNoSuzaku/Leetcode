# Check if all rooms can be visited starting from room 0 with collected keys.

# Author: Kaustav Ghosh

class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)
