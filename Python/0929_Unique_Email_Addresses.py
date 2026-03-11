# Count unique email addresses after applying filtering rules.

# Author: Kaustav Ghosh

class Solution(object):
    def numUniqueEmails(self, emails):
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)
