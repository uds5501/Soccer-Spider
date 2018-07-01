# Soccer-Spider
Coding Challenge 1 : Scraping a web site without BeautifulSoup

Youtube Link : <To_be_added>

---
#### Introduction
The challenge was precisely to make a web scraper without using BeautifulSoup. Now, in my opinion, There are always certain alternatives for a famous method and this case is no exception. Admitted that the Beautiful soup not only makes life really easy for any beginner web scraper, but it also handles the scraping requests with comparatively less memory but with minimal multiple recursive link callbacks.

The module I am using in this tutorial, **Scrapy** is a web crawler with better callback functionality but with the drawback of memory management. One must notice that BeautifulSoup is simply a *parser* but Scrapy? Scrapy is a web crawling framework and if you are looking for crawling multiple pages at once with single spider, this is the method that I'd recommend.

PS : JavaScript Developer? A simple Express application with `cheerios`+`request` plugin usage would do the job too.

---

#### Environment Setup
For the crawler to work, I'd recommend the following setup
```
python >= 2.7.12
scrapy = 1.5.0
```

Note : for installation of scrapy, you would most probably require *win 32 api* (Of course, if using on windows). Recommended installation steps : 

```
>pip install pywin32
>pip install scrapy
```

---

#### How to Use
Simply follow theses steps:

```cmd
> cd path_to_repository
path_to_repository > scrapy runspider scraper.py
```
Result would be stored in `result.csv` ( You may delete it before running the scraper for personal confirmation)

And that's it, that's how you build a simple crawler !

For detailed description of the scraper's working, checkout the [youtube video]()!

Thank you [@Logan-47](https://github.com/Logan-47) for this fun challenge!
