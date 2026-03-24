# Author: Kaustav Ghosh
# Problem 1990: Count the Number of Experiments (Premium)
#
# SQL Solution (Premium):
# SELECT p.platform, e.experiment_name,
#        COUNT(ex.experiment_id) AS num_experiments
# FROM (SELECT 'Android' AS platform UNION SELECT 'IOS' UNION SELECT 'Web') p
# CROSS JOIN (SELECT 'Reading' AS experiment_name UNION SELECT 'Sports' UNION SELECT 'Programming') e
# LEFT JOIN Experiments ex
#   ON p.platform = ex.platform AND e.experiment_name = ex.experiment_name
# GROUP BY p.platform, e.experiment_name;

class Solution(object):
    pass
