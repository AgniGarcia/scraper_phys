import scrapy

# XPath
# links_to_articles = /html/body/main/div/div[1]/div/div/div/article/div/div/h3/a/@href'
# titles = ''/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/h1/text()''
# brief = '/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p[1]/text()[1]'
# body = '/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p/text()'


class ArticlesSpider(scrapy.Spider):
    name = 'notes'
    start_urls = [
        'https://phys.org/'
    ]
    custom_settings = {
        'FEED_URI' : 'articles.json',
        'FEED_FORMAT' : 'json'
    }

    # def parse_only_notes(self, response, **kwargs):
    #     if kwargs:
    #         notes = kwargs['notes']
    #     notes.extend(response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p/text()').getall())
        
    #     links_to_articles = response.xpath('/html/body/main/div/div[1]/div/div/div/article/div/div/h3/a/@href').getall()
    #     if links_to_articles:
    #         yield response.follow(links_to_articles, callback=self.parse_only_notes, cb_kwargs={'notes':notes})
    #     else:
    #         yield {
    #             'notes' : notes
    #         }

    def parse(self, response):

        titles = response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/h1/text()').get()
        body = response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p/text()').getall()
        briefs = response.xpath('/html/body/main/div[1]/div[3]/div[2]/section/div/div[4]/article/div[2]/p[1]/text()[1]').get()

        yield {
            'title' : title,
            'briefs' : briefs,
            'body' : body
        }

        links_to_articles = response.xpath('/html/body/main/div/div[1]/div/div/div/article/div/div/h3/a/@href').getall()
        #yield response.follow(links_to_articles, callback=self.parse)
        for link in links_to_articles:
            parse(self, response)
