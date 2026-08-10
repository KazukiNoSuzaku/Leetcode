# Author: Kaustav Ghosh
# Problem: Count the Number of Experiments
# Approach: Build the full grid of the three platforms and three experiment names, then left-join the actual per-group counts, filling missing combinations with zero

import pandas as pd

def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    platforms = pd.DataFrame({'platform': ['Android', 'IOS', 'Web']})
    names = pd.DataFrame({'experiment_name': ['Reading', 'Sports', 'Programming']})
    base = platforms.merge(names, how='cross')

    counts = (experiments.groupby(['platform', 'experiment_name'])
              .size()
              .reset_index(name='num_experiments'))

    result = base.merge(counts, on=['platform', 'experiment_name'], how='left')
    result['num_experiments'] = result['num_experiments'].fillna(0).astype(int)
    return result
