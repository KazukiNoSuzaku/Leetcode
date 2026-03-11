# Find minimum number of buses to take to travel from source to target stop.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target: return 0
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        visited_stops = {source}
        visited_routes = set()
        q = deque([(source, 0)])
        while q:
            stop, buses = q.popleft()
            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes: continue
                visited_routes.add(route_idx)
                for next_stop in routes[route_idx]:
                    if next_stop == target: return buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, buses + 1))
        return -1
