import scrapy

# XPATH
# links_to_articles = '/html/body/main/div/div[1]/div/div/div/article/div/div/h3/a/@href'
# titles = ''/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/h1/text()''
# brief = '/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p[1]/text()[1]'
# body = '/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p/text()'

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    start_urls = [
        'https://phys.org/'
    ]
    custom_settings = {
        'FEED_URI' : 'articles.json',
        'FEED_FORMAT' : 'json'
    }

    def parse(self, response):
        links_to_articles = response.xpath('/html/body/main/div/div[1]/div/div/div/article/div/div/h3/a/@href')
        for link in links_to_articles:
            yield response.follow(link.get(), callback=self.parse_articles)

    def parse_articles(self, response):

        title = response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/h1/text()').get()
        brief = response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p[1]/text()[1]').get()
        body = response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p/text()').getall()

        yield {
            'title' : title,
            'brief' : brief,
            'body'  : body   
        }
