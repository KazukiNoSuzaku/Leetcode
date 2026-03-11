# Design a log storage system that can retrieve logs within a time range at given granularity.

# Author: Kaustav Ghosh

class LogSystem(object):
    def __init__(self):
        self.logs = []
        self.units = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, id, timestamp):
        self.logs.append((timestamp, id))

    def retrieve(self, start, end, granularity):
        n = self.units[granularity]
        return [id for ts, id in self.logs if start[:n] <= ts[:n] <= end[:n]]
