import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    

    myBaseUrl = ''
    start_urls = []
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'tutorial/outputfile.json', 'CLOSESPIDER_TIMEOUT' : 15}  
    
    def parse(self, response):
        image = response.css('img').xpath('@src').getall()
        url = response.css('a::attr(href)').getall()
        p_tags =response.xpath('//p/text()').getall()
        title = response.xpath('//title/text()').getall()
        heading1 = response.xpath('//h1/text()').getall()
        heading2 = response.xpath('//h2/text()').getall()
        heading3 = response.xpath('//h3/text()').getall()
        heading4 = response.xpath('//h4/text()').getall()
        heading5 = response.xpath('//h5/text()').getall()
        heading6 = response.xpath('//h6/text()').getall()

        
        yield{
            'title' :title,
            'image':image,
            'url':url,
            'p_tags':p_tags,
             'heading1' :heading1,
            'heading2' : heading2,
            'heading3' :heading3,
            'heading4'  :heading4,
            'heading5' :heading5,
            'heading6' :heading6
        }
