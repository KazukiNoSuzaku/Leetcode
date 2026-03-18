# Premium SQL problem - Find countries where average call duration is strictly greater
# than the global average call duration.

# Author: Kaustav Ghosh

# SQL solution:
# SELECT co.name AS country
# FROM Person p
# JOIN Calls c ON p.phone_number IN (c.caller_id, c.callee_id)
# JOIN Country co ON LEFT(p.phone_number, 3) = co.country_code
# GROUP BY co.name
# HAVING AVG(c.duration) > (SELECT AVG(duration) FROM Calls);

class Solution(object):
    pass
