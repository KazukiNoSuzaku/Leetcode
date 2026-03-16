# Author: Kaustav Ghosh
# Problem: Display Table of Food Orders in a Restaurant
# Approach: Pivot table with sorted keys

from collections import defaultdict

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        tables = defaultdict(lambda: defaultdict(int))
        foods = set()
        for _, table, food in orders:
            tables[int(table)][food] += 1
            foods.add(food)

        foods = sorted(foods)
        result = [["Table"] + foods]
        for table_num in sorted(tables.keys()):
            row = [str(table_num)]
            for food in foods:
                row.append(str(tables[table_num][food]))
            result.append(row)
        return result
