
# bradburnhome scraper

bradburnhome scraper is a scrapy script used to crawl products according to given fields to be saved in csv format file.

## how it works
the project consists of two scrapers:

1 - designers spider that will scrape products names and their designer from each designer page and store them in `designers.csv` file

2 - products spider that will do the rest of the data scraping from products pages and fetch designer name from `designers.csv` file if product name exists in it.
## usage 
You can either run the scrapers in the following order:

`scrapy crawl designers -o designers.csv`

`scrapy crawl products -o products.csv`

or use the bash file:

`bash start.sh`
## requirements

To run this project, you will need the following requirements installed:

`scrapy`

`word2number`

`scrapy-item`


## Authors

- [@oussamadz](https://www.github.com/oussamadz)
