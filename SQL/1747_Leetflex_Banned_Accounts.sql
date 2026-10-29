-- Author: Kaustav Ghosh
-- Problem: Leetflex Banned Accounts
-- Approach: An account is banned when two of its sessions from different addresses were live at the same instant, and two intervals overlap exactly when one of them begins inside the other; checking only that one direction is enough, because whichever session started later is the one whose login falls inside the other's span, and the self-join sees both orderings anyway. So the table is joined to itself on the account with differing addresses, keeping the rows whose login lies within the other session's window, and the comparison is inclusive at both ends since the problem treats a logout and a login at the very same second as an overlap. DISTINCT collapses an account that trips the condition several times, which matters because the table is allowed duplicate rows.

SELECT DISTINCT a.account_id
FROM LogInfo a
JOIN LogInfo b
  ON b.account_id = a.account_id
 AND b.ip_address <> a.ip_address
 AND a.login BETWEEN b.login AND b.logout;
