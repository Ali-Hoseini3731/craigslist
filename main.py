import requests
from bs4 import BeautifulSoup


def get_page(craigslist_url):
    try:
        craigslist_response = requests.get(craigslist_url)
    except:
        return None
    print(craigslist_response.status_code)
    return craigslist_response


def find_links(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    adv_list = soup.find_all("li", attrs={"class": "cl-static-search-result"})
    all_links = []
    for link in adv_list:
        all_links.append(link.find("a").get("href"))
    return all_links


def start_crawl(craigslist_url):
    response = get_page(craigslist_url)
    links = find_links(response.text)
    for link in links:
        print(link)

    print(len(links))


if __name__ == "__main__":
    url = "https://paris.craigslist.org/search/hhh?cc=gb&lang=en"
    start_crawl(url)
