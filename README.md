# Web Scraping with Python and Scrapy: Amazon Book Title and Price Scraper
This Python project utilizes Scrapy to scrape the Amazon website for book titles and prices. The code can be easily modified to search for any type of product on Amazon.

# Prerequisites
- Python 3.x
- Scrapy (https://scrapy.org/)
# Installation
- Install Python 3.x on your machine. Instructions can be found at https://www.python.org/downloads/
- Install Scrapy by running in your terminal/command prompt.
```python
pip install scrapy
```
# Usage
1- Clone or download the project files to your local machine.
2- Navigate to the project directory in your terminal/command prompt.
3- Open the amazon_spider.py file in a text editor.
4- Modify the start_urls variable to reflect the Amazon page you wish to scrape.
5- Modify the BOOK_SELECTOR and PRICE_SELECTOR variables to match the CSS selectors of the book titles and prices on the Amazon page you wish to scrape.
6- Save the amazon_spider.py file.
7- In your terminal/command prompt, run the command scrapy crawl amazon to run the spider.
8- The book titles and prices will be outputted to the terminal/command prompt.
# Contributing
If you wish to contribute to this project, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
