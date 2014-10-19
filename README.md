python_webscraping_practice
===========================

Quick experiments in webscraping using python.

Repo contains two web scapers: 

**1. web_scraper.py**
Should be run using Python 3.4.0.
Quick attempt at a basic web scraper to get a basic sense of how they work.

**2. QC_Spider**
Implementation using the Scrapy library. 
Crawls website for blog entries. Gets the URL, title and date of each blog post.

To run, use the command shown below (you need to have Scrapy installed).
  scrapy crawl blog_spider

Data output into a SQLite database in current working directory. 


