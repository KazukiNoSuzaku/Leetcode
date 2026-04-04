# Author: Kaustav Ghosh

# Premium SQL Problem
# Given tables Posts (post_id, content) and Keywords (topic_id, word),
# find the topic of each post by matching keywords in post content (case-insensitive).
# If a post matches no topic, return "Ambiguous!" and if multiple, return all joined by comma.
#
# SQL Approach:
# SELECT p.post_id,
#        IFNULL(
#          GROUP_CONCAT(DISTINCT k.topic_id ORDER BY k.topic_id SEPARATOR ','),
#          'Ambiguous!'
#        ) AS topic
# FROM Posts p
# LEFT JOIN Keywords k
#   ON LOWER(p.content) REGEXP CONCAT('(^| )', LOWER(k.word), '( |$)')
# GROUP BY p.post_id;

class Solution(object):
    pass
