import requests
from parsel import Selector


# pip install parsel
# pip install requests
# pip install lxml==4.9.4

class NewsScraper:
    URL = "https://animestars.org/"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.5",
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0"
    }
    PHONE_NUMBER = '//div[@class="footer-num "]/a/text()'
    DESCRIPTION_XPATH = '//p[@class="remove-outline"]/text()'
    DATE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/small/text()'
    IMAGE_XPATH = '//div[@class="row newsCards"]//img/@src'
    TITLE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/text()'
    LINK_XPATH = '//img[@class="lazy-loaded"]/@data-src'

    def scrape_data(self):
        response = requests.get(self.URL, headers=self.HEADERS)
        # print(response.text)
        tree = Selector(text=response.text)
        imgs = tree.xpath(self.IMAGE_XPATH).getall()
        titles = tree.xpath(self.TITLE_XPATH).getall()
        dates = tree.xpath(self.DATE_XPATH).getall()
        descriptions = tree.xpath(self.DESCRIPTION_XPATH).getall()
        links = tree.xpath(self.LINK_XPATH).getall()
        print(links)
        return links[:5]
        # for description in descriptions:
        #     print(description)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()
