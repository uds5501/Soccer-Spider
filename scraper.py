import scrapy
import pandas as pd

class MyScraper(scrapy.Spider):
    name = "football_satan"
    start_urls=['https://beyondminute90.wordpress.com/category/much-about-football/']

    def parse(self, response):
        '''The main parsing unit'''
        title = response.xpath('//h2/a/text()').extract()

        # Removing Latin unicodes from our code and converting to strings
        for i in range(len(title)):
            title[i] = str(title[i].replace(u'\xa0', u' '))
        
        publishedOn = response.xpath("//a/time[@class='updated']/text()").extract()

        # Converting dates to strings
        for i in range(len(publishedOn)):
            publishedOn[i] = str(publishedOn[i])
        
        # Displaying results on CLI
        print "\n\n\n\nResults"
        for result in zip(title,publishedOn):
            print "{"+ result[0] +":"+result[1]+"}"
        print "\n\n\n\n"

        df = pd.DataFrame(data=[title, publishedOn]).transpose()
        df.columns = ['Title', 'Publishing Date']
        df.to_csv('result.csv', index = False)
        return None
