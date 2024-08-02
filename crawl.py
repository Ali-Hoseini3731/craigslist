import json
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup

from config import BASE_LINK
from parser import AdvertisementPageParse


class BaseCrawl(ABC):
    @abstractmethod
    def start(self, *args):
        pass

    def store(self, data):
        pass

    @staticmethod
    def get(link):
        try:
            response = requests.get(link)
        except requests.HTTPError:
            return None
        return response


class CrawlLinks(BaseCrawl):

    def __init__(self, cities, link=BASE_LINK):
        self.cities = cities
        self.link = link

    @staticmethod
    def find_links(html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        li_list = soup.find_all("li", attrs={"class": "cl-static-search-result"})
        links = list()
        for li in li_list:
            links.append(li.find("a").get("href"))
        return links

    def start_crawl_city(self, link):

        response = self.get(link)
        links = self.find_links(response.text)
        return links

    def start(self, store=False):
        adv_links = list()

        for city in self.cities:
            links = self.start_crawl_city(self.link.format(city))
            print(f"{city}: {len(links)}")
            adv_links.extend(links)
        if store:
            self.store(adv_links)

    def store(self, data):
        with open("fixtures/all_links.json", "w") as f:
            f.write(json.dumps(data))


class CrawlData(BaseCrawl):

    def __init__(self):
        self.links = self.__load_links()
        self.parser = AdvertisementPageParse()

    @staticmethod
    def __load_links():
        links = list()
        with open("fixtures/all_links.json", "r") as f:
            links = json.loads(f.read())
        return links

    def start(self, store=False):
        for link in self.links:
            response = self.get(link)
            data = self.parser.parse(response.text)
            if store:
                self.store(data)

    def store(self, data):
        with open(f"fixtures/data/{data['post_id']}.json", "w") as f:
            f.write(json.dumps(data))
