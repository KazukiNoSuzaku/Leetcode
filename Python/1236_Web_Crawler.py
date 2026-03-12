# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: BFS using htmlParser, filter by hostname

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        from collections import deque

        def get_hostname(url):
            return url.split('/')[2]

        hostname = get_hostname(startUrl)
        visited = {startUrl}
        queue = deque([startUrl])

        while queue:
            url = queue.popleft()
            for next_url in htmlParser.getUrls(url):
                if next_url not in visited and get_hostname(next_url) == hostname:
                    visited.add(next_url)
                    queue.append(next_url)
        return list(visited)
