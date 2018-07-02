import scrapy
import re
import pandas as pd

class MyScraper(scrapy.Spider):
    name = "football_satan"
    start_urls=['https://beyondminute90.wordpress.com/category/much-about-football/']

    def parse(self, response):
        '''The main parsing unit'''
        title = response.xpath('//h2/a/text()').extract()

        # Removing Latin unicodes from our code and converting to strings
        for i in range(len(title)):
            title[i] = re.sub(u"(\u2018|\u2019)", "'", title[i])
            title[i] = re.sub(u"\xa0", " ", title[i])
            title[i] = str(title[i])
        
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
