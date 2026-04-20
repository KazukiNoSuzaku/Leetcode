# SQL solution (Premium)
# SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
# FROM Teacher
# GROUP BY teacher_id

# Python simulation
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')
