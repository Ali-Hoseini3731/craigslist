from bs4 import BeautifulSoup


class AdvertisementPageParse:
    def __init__(self):
        self.soup = None

    @property
    def price(self):
        try:
            price_tag = self.soup.find("span", {"class": "price"}).text
        except:
            return None

        if price_tag:
            return price_tag
        return None

    @property
    def housing(self):
        try:
            housing_tag = self.soup.find("span", {"class": "housing"}).text
        except:
            return None
        if housing_tag:
            return housing_tag
        return None

    @property
    def title(self):
        try:
            title_tag = self.soup.find(id="titletextonly").text
        except:
            return None
        if title_tag:
            return title_tag
        return None

    @property
    def address(self):
        try:
            selector = "body > section > section > h1 > span > span:nth-child(4)"
            address_tag = self.soup.select_one(selector).text
        except:
            return None
        if address_tag:
            return address_tag
        return None

    @property
    def description(self):
        try:
            description_tag = self.soup.select_one("#postingbody").text
        except:
            return None
        if description_tag:
            return description_tag
        return None

    @property
    def post_id(self):
        try:
            selector = "body > section > section > section > div.postinginfos > p:nth-child(1)"
            post_id_tag = self.soup.select_one(selector).text.replace("Id publi: ","")
        except:
            return None
        if post_id_tag:
            return post_id_tag
        return None

    @property
    def created_time(self):
        try:
            selector = "body > section > section > section > div.postinginfos > p:nth-child(2) > time"
            created_time_tag = self.soup.select_one(selector).attrs["datetime"]
        except:
            return None
        if created_time_tag:
            return created_time_tag
        return None

    def parse(self, html_doc):
        self.soup = BeautifulSoup(html_doc, "html.parser")
        data = dict(
            price=self.price, housing=self.housing, title=self.title, address=self.address,
            description=self.description, post_id=self.post_id, created_time=self.created_time,
        )
        return data
