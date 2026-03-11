-- Get the highest answer rate question.
-- Author: Kaustav Ghosh

SELECT question_id AS survey_log
FROM SurveyLog
GROUP BY question_id
ORDER BY SUM(action = 'answer') / SUM(action = 'show') DESC
LIMIT 1;
