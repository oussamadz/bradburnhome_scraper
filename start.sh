#!/bin/bash
echo "start: `date`";
echo "crawling designers";
scrapy crawl designers -o designers.csv 1&2>/dev/null;
echo "crawling products";
scrapy crawl products -o products.csv 1&2>/dev/null;
echo "end: `date`";
