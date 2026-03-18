# Author: Kaustav Ghosh
# Problem: 1538 - Guess the Majority in a Hidden Array (Premium)
# Approach: Query API to deduce majority by comparing query results

# This is an interactive problem using an ArrayReader interface.
# class ArrayReader:
#     def query(self, a, b, c, d) -> int: ...
#     def length(self) -> int: ...

class Solution(object):
    def guessMajority(self, reader):
        """
        :type reader: ArrayReader
        :rtype: int
        """
        n = reader.length()
        # query(0,1,2,3) vs query(i,1,2,3) to find if arr[i] == arr[0]
        q0 = reader.query(0, 1, 2, 3)
        group_a = [0]  # same as arr[0]
        group_b = []

        for i in range(4, n):
            if reader.query(i, 1, 2, 3) == q0:
                group_a.append(i)
            else:
                group_b.append(i)

        # Compare indices 1,2,3 with 0
        # query(1,2,3,4) vs q0's base
        for i in range(1, 4):
            # query(0,1,2,3) with i replaced by something else
            indices = [0, 1, 2, 3]
            indices[i] = 4 if n > 4 else (indices[i-1] if i > 0 else 1)
            # Use a fresh comparison: replace position i with position 4
            if n > 4:
                ref = reader.query(0, 1, 2, 3)
                new_q = reader.query(*([j if j != i else 4 for j in [0, 1, 2, 3]]))
                # This approach is complex; use simpler: compare query(1,2,3,4) == q0?
            pass

        # Simpler approach: compare each of 1,2,3 against 0
        # query(0,1,2,3): depends on arr[0],arr[1],arr[2],arr[3]
        # query(1,2,3,4): depends on arr[1],arr[2],arr[3],arr[4]
        # if equal -> arr[0] == arr[4]

        # Re-implement cleanly
        group_a = [0]
        group_b = []
        base = reader.query(0, 1, 2, 3)

        # Check indices 4..n-1
        for i in range(4, n):
            if reader.query(i, 1, 2, 3) == base:
                group_a.append(i)
            else:
                group_b.append(i)

        # Check index 1
        if reader.query(1, 0, 2, 3) == base:
            group_a.append(1)
        else:
            group_b.append(1)

        # Check index 2
        if reader.query(2, 0, 1, 3) == base:
            group_a.append(2)
        else:
            group_b.append(2)

        # Check index 3
        if reader.query(3, 0, 1, 2) == base:
            group_a.append(3)
        else:
            group_b.append(3)

        if len(group_a) > len(group_b):
            return group_a[0]
        elif len(group_b) > len(group_a):
            return group_b[0]
        return -1
