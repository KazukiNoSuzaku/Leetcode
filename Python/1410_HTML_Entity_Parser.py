# Author: Kaustav Ghosh
# Problem: HTML Entity Parser
# Approach: Replace HTML entities with corresponding characters

class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        # Replace &amp; last to avoid double replacement
        for entity in ["&quot;", "&apos;", "&gt;", "&lt;", "&frasl;", "&amp;"]:
            text = text.replace(entity, entities[entity])
        return text
