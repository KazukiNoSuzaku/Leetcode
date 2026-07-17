# Author: Kaustav Ghosh
# Problem: Find the Subtasks That Did Not Execute (Premium)
# Approach: Expand each task into its full subtask id range 1..subtasks_count, then anti-join against Executed to keep the ones never run

import pandas as pd

def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for task_id, count in zip(tasks['task_id'], tasks['subtasks_count']):
        for subtask_id in range(1, count + 1):
            rows.append((task_id, subtask_id))
    everything = pd.DataFrame(rows, columns=['task_id', 'subtask_id'])

    merged = everything.merge(executed, on=['task_id', 'subtask_id'], how='left', indicator=True)
    return merged[merged['_merge'] == 'left_only'][['task_id', 'subtask_id']]
