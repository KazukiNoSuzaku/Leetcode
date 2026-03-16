# Author: Kaustav Ghosh
# Problem: Number of Trusted Contacts of a Customer (Premium SQL)
# Approach: JOIN Customers, Contacts, and Invoices to count trusted contacts
#
# SQL Solution:
# SELECT i.invoice_id, c.customer_name, i.price,
#        COUNT(co.contact_name) AS contacts_cnt,
#        COUNT(t.customer_name) AS trusted_contacts_cnt
# FROM Invoices i
# JOIN Customers c ON i.user_id = c.customer_id
# LEFT JOIN Contacts co ON c.customer_id = co.user_id
# LEFT JOIN Customers t ON co.contact_email = t.email
# GROUP BY i.invoice_id, c.customer_name, i.price
# ORDER BY i.invoice_id

class Solution(object):
    pass
