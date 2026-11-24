-- Author: Kaustav Ghosh
-- Problem: Number of Accounts That Did Not Stream
-- Approach: An account counts when its subscription covers some part of 2021 and it has no stream session during that year, so the subscription side is a plain year comparison on the start and end dates while the stream side is an absence test. The absence is expressed with a correlated NOT EXISTS rather than a left join filtered in the WHERE clause, because a filter on the joined date would discard precisely the accounts that have no stream rows at all, which are the clearest qualifiers, and it would also count an account once per non-2021 session it happens to have. Testing existence per account instead counts each qualifying account exactly once regardless of how many sessions it has.

SELECT COUNT(*) AS accounts_count
FROM Subscriptions AS s
WHERE YEAR(s.start_date) <= 2021
  AND YEAR(s.end_date) >= 2021
  AND NOT EXISTS (
      SELECT 1
      FROM Streams AS t
      WHERE t.account_id = s.account_id
        AND YEAR(t.stream_date) = 2021
  );
