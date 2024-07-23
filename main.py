import sys
import requests
from bs4 import BeautifulSoup


def get_page(craigslist_url):
    try:
        craigslist_response = requests.get(craigslist_url)
    except:
        return None
    return craigslist_response


def find_links(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    adv_list = soup.find_all("li", attrs={"class": "cl-static-search-result"})
    all_links = []
    for link in adv_list:
        all_links.append(link.find("a").get("href"))
    return all_links


def start_crawl_city(craigslist_url):
    response = get_page(craigslist_url)
    links = find_links(response.text)
    return links


def start_crawl():
    cities = ["paris", "berlin", "rome"]
    url = "https://{}.craigslist.org/search/hhh?cc=gb&lang=en"

    print("your crawl is: ")
    for city in cities:
        links = start_crawl_city(url.format(city))
        print(f"{city}:", len(links))


if __name__ == "__main__":
    switch = sys.argv[1]
    if switch == "find":
        start_crawl()
    elif switch == "extract":
        raise NotImplementedError
