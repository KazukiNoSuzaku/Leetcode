# Author: Kaustav Ghosh
# Problem: 2252. Dynamic Pivoting of a Table
# URL: https://leetcode.com/problems/dynamic-pivoting-of-a-table/
# Difficulty: Hard
# Note: Premium SQL problem
#
# SQL Approach:
# Use dynamic SQL to build a pivot query. First collect all distinct store
# names, then generate a SUM(CASE WHEN store = 'X' THEN price END) column
# for each store, grouped by product.
#
# CREATE PROCEDURE PivotProducts()
# BEGIN
#     SET SESSION group_concat_max_len = 1000000;
#     SELECT GROUP_CONCAT(DISTINCT
#         CONCAT('SUM(CASE WHEN store = ''', store, ''' THEN price END) AS ', store)
#         ORDER BY store)
#     INTO @sql
#     FROM Products;
#     SET @sql = CONCAT('SELECT product, ', @sql, ' FROM Products GROUP BY product');
#     PREPARE stmt FROM @sql;
#     EXECUTE stmt;
#     DEALLOCATE PREPARE stmt;
# END

class Solution(object):
    pass
