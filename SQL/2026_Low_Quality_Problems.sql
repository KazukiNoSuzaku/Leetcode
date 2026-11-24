-- Author: Kaustav Ghosh
-- Problem: Low-Quality Problems
-- Approach: A problem is low quality when its likes divided by its total votes falls strictly below sixty percent, which is a straightforward row filter needing no join or grouping. Rather than dividing, the comparison is cleared of fractions by multiplying through: ten times the likes against six times the total votes expresses the same threshold using only integer arithmetic, so a ratio sitting exactly on the boundary is classified correctly instead of hinging on how precisely six tenths can be represented as a floating-point value. A problem with no votes at all fails the comparison and is left out, matching what dividing by a zero total would yield.

SELECT problem_id
FROM Problems
WHERE likes * 10 < (likes + dislikes) * 6
ORDER BY problem_id;
