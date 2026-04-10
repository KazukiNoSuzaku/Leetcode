# Author: Kaustav Ghosh
# Problem: 2253. Dynamic Unpivoting of a Table
# URL: https://leetcode.com/problems/dynamic-unpivoting-of-a-table/
# Difficulty: Hard
# Note: Premium SQL problem
#
# SQL Approach:
# Use dynamic SQL to unpivot. Query INFORMATION_SCHEMA.COLUMNS to get all
# column names except 'product'. For each column, generate a SELECT that
# produces (product, column_name, column_value) and UNION ALL them together.
#
# CREATE PROCEDURE UnpivotProducts()
# BEGIN
#     SELECT GROUP_CONCAT(
#         CONCAT('SELECT product, ''', COLUMN_NAME, ''' AS store, ',
#                COLUMN_NAME, ' AS price FROM Products WHERE ',
#                COLUMN_NAME, ' IS NOT NULL')
#         SEPARATOR ' UNION ALL ')
#     INTO @sql
#     FROM INFORMATION_SCHEMA.COLUMNS
#     WHERE TABLE_NAME = 'Products' AND COLUMN_NAME <> 'product';
#     PREPARE stmt FROM @sql;
#     EXECUTE stmt;
#     DEALLOCATE PREPARE stmt;
# END

class Solution(object):
    pass
