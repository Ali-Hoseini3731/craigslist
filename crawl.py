import json
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

from config import BASE_URL


class BaseCrawl(ABC):
    @abstractmethod
    def start(self):
        pass

    def store(self, data):
        pass


class CrawlLinks(BaseCrawl):

    def __init__(self, cities, url=BASE_URL):
        self.cities = cities
        self.url = url

    def get_page(self, url):
        try:
            response = requests.get(url)
        except:
            response = None
        return response

    def find_links(self, html_doc):

        soup = BeautifulSoup(html_doc, 'html.parser')
        li_list = soup.find_all("li", attrs={"class": "cl-static-search-result"})
        links = list()
        for li in li_list:
            links.append(li.find("a").get("href"))
        return links

    def start_crawl_city(self, url):

        response = self.get_page(url)
        links = self.find_links(response.text)
        return links

    def start(self):
        adv_links = list()

        for city in self.cities:
            links = self.start_crawl_city(self.url.format(city))
            print(f"{city}: {len(links)}")
            adv_links.extend(links)

        self.store(adv_links)

    def store(self, data):
        with open("fixtures/data.json", "w") as f:
            f.write(json.dumps(data))


class CrawlData(BaseCrawl):
    def start(self):
        pass

    def store(self, data):
        pass

    def get_data_pages(self):
        print("hi Ali completes me")
