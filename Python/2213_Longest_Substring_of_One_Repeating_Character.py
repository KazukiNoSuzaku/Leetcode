# Author: Kaustav Ghosh
# Problem: 2213. Longest Substring of One Repeating Character
# URL: https://leetcode.com/problems/longest-substring-of-one-repeating-character/
# Difficulty: Hard
#
# Approach:
# Maintain a sorted structure of "runs" (consecutive same-character segments).
# For each query (index, new_char), update the character at that index and
# merge or split runs as needed. Track the maximum run length after each
# update using a sorted multiset (simulated with SortedList from sortedcontainers).

from sortedcontainers import SortedList

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: list[int]
        :rtype: list[int]
        """
        s = list(s)
        n = len(s)

        # Build initial runs: list of (start, end, char)
        # We'll track runs as a dict: start -> (end, char)
        # and index -> start of its run
        # Use SortedList of (-length) to track max efficiently

        # Represent runs as sorted list of [start, end] with char
        # For fast lookup by position, use a SortedList of start positions
        run_starts = SortedList()  # sorted start indices
        run_map = {}  # start -> [end, char]
        lengths = SortedList()  # all run lengths for max query

        def add_run(start, end, char):
            run_map[start] = [end, char]
            run_starts.add(start)
            lengths.add(end - start + 1)

        def remove_run(start):
            end, char = run_map[start]
            lengths.remove(end - start + 1)
            run_starts.remove(start)
            del run_map[start]

        # Build initial runs
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            add_run(i, j - 1, s[i])
            i = j

        results = []
        for qi, qc in zip(queryIndices, queryCharacters):
            if s[qi] != qc:
                s[qi] = qc
                # Find the run containing qi
                idx = run_starts.bisect_right(qi) - 1
                r_start = run_starts[idx]
                r_end, r_char = run_map[r_start]

                # Remove current run
                remove_run(r_start)

                # Split into up to 3 parts: before qi, qi itself, after qi
                new_runs = []
                if r_start < qi:
                    new_runs.append((r_start, qi - 1, r_char))
                new_runs.append((qi, qi, qc))
                if qi < r_end:
                    new_runs.append((qi + 1, r_end, r_char))

                # Merge adjacent runs with same character
                # Check left neighbour
                merged_left = False
                if run_starts and new_runs:
                    left_idx = run_starts.bisect_left(new_runs[0][0]) - 1
                    if left_idx >= 0:
                        l_start = run_starts[left_idx]
                        l_end, l_char = run_map[l_start]
                        if l_end == new_runs[0][0] - 1 and l_char == new_runs[0][2]:
                            remove_run(l_start)
                            new_runs[0] = (l_start, new_runs[0][1], l_char)
                            merged_left = True

                # Check right neighbour
                if run_starts and new_runs:
                    right_start_candidate = new_runs[-1][1] + 1
                    if right_start_candidate in run_map:
                        r2_end, r2_char = run_map[right_start_candidate]
                        if r2_char == new_runs[-1][2]:
                            remove_run(right_start_candidate)
                            new_runs[-1] = (new_runs[-1][0], r2_end, r2_char)

                # Merge the new_runs list itself if middle collapsed
                # Merge consecutive segments with same char in new_runs
                merged = [new_runs[0]]
                for seg in new_runs[1:]:
                    if seg[2] == merged[-1][2]:
                        merged[-1] = (merged[-1][0], seg[1], seg[2])
                    else:
                        merged.append(seg)

                for seg in merged:
                    add_run(seg[0], seg[1], seg[2])

            results.append(lengths[-1])

        return results
