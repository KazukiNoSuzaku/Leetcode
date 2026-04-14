# Author: Kaustav Ghosh
# 2314. The First Day of the Maximum Recorded Degree in Each City
# Premium SQL problem
#
# SQL Solution:
#
# SELECT city_id, day
# FROM (
#     SELECT city_id, day, degree,
#            RANK() OVER (PARTITION BY city_id ORDER BY degree DESC, day ASC) AS rnk
#     FROM Weather
# ) ranked
# WHERE rnk = 1
# ORDER BY city_id;
#
# Approach: use RANK() window function partitioned by city_id,
# ordered by degree DESC then day ASC to get the first day
# with the maximum recorded temperature for each city.

class Solution(object):
    pass
