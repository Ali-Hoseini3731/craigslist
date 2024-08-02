import sys

from crawl import CrawlLinks, CrawlData

if __name__ == "__main__":
    cities = ["paris", "berlin"]
    switch = sys.argv[1]

    if switch == "find_links":
        crawl_links = CrawlLinks(cities=cities)
        crawl_links.start(store=True)
    elif switch == "extract_pages":
        crawl_data = CrawlData()
        crawl_data.start(store=True)