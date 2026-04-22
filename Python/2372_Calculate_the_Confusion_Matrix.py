# Premium SQL problem
#
# SELECT
#   SUM(CASE WHEN actual=1 AND predicted=1 THEN 1 ELSE 0 END) AS TP,
#   SUM(CASE WHEN actual=0 AND predicted=1 THEN 1 ELSE 0 END) AS FP,
#   SUM(CASE WHEN actual=1 AND predicted=0 THEN 1 ELSE 0 END) AS FN,
#   SUM(CASE WHEN actual=0 AND predicted=0 THEN 1 ELSE 0 END) AS TN
# FROM Predictions
