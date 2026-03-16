# Author: Kaustav Ghosh
# Problem: Friendly Movies Streamed Last Month (Premium SQL)
# Approach: JOIN TVProgram and Content, filter by June 2020 and Kids content
#
# SQL Solution:
# SELECT DISTINCT c.title
# FROM TVProgram t
# JOIN Content c ON t.content_id = c.content_id
# WHERE t.program_date BETWEEN '2020-06-01' AND '2020-06-30'
#   AND c.Kids_content = 'Y'
#   AND c.content_type = 'Movies'

class Solution(object):
    pass
