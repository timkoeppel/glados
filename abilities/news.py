from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen


def getNews():
    """gets current news from Google News website via xml soup"""
    try:
        result = ''
        news_url = "https://news.google.com/news/rss"
        client = urlopen(news_url)
        xml_page = client.read()
        client.close()
        soup_page = Soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        for news in news_list[:5]:
            result = result + news.title.text.encode('utf-8')
        return result
    except Exception as e:
        print(e)
