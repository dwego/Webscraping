import scrapy

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://www.amazon.com.br/s?k=livros',
    ]

    def parse(self, response):
        for livro in response.css('div.s-result-item'):
            yield {
                'titulo': livro.css('h2.a-size-mini span.a-text-normal::text').get(),
                'preco': livro.css('span.a-price-whole::text').get(),
            }

        next_page = response.css('a.s-pagination-item.s-pagination-next.s-pagination-button').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, self.parse)