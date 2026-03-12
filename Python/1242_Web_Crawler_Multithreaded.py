# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Concurrent BFS with thread pool for web crawling

import threading
from collections import deque

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        def get_hostname(url):
            return url.split('/')[2]

        hostname = get_hostname(startUrl)
        visited = {startUrl}
        lock = threading.Lock()
        queue = deque([startUrl])

        def worker(url):
            urls = htmlParser.getUrls(url)
            new_urls = []
            with lock:
                for u in urls:
                    if u not in visited and get_hostname(u) == hostname:
                        visited.add(u)
                        new_urls.append(u)
            return new_urls

        while queue:
            threads = []
            batch = []
            while queue:
                batch.append(queue.popleft())
            results = [[] for _ in batch]

            def crawl_url(idx, url):
                results[idx] = worker(url)

            for i, url in enumerate(batch):
                t = threading.Thread(target=crawl_url, args=(i, url))
                threads.append(t)
                t.start()
            for t in threads:
                t.join()
            for r in results:
                queue.extend(r)

        return list(visited)
