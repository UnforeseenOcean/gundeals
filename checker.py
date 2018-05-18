#!/usr/bin/env python
'''
Pretty simplistic web scraper for AR parts
'''

from bs4 import BeautifulSoup as bs
import requests
import yaml

_BRAND_ALERT = False

# Parse config file
def get_config(filename):
    global _BRAND_ALERT

    with open(filename) as fr:
        config = yaml.safe_load(fr)
        if config['brand_alert']:
            _BRAND_ALERT = True
        return config


# Query webpage and return HTML
def get_html(url):
    content = requests.get(url).text
    return bs(content, 'html.parser').lower()


# Do any of our part show up in the HTML?
def check_sale(html, parts):
    pass


def main():
    # Parse t3h config
    config = get_config('config.yml')
    print(config)

    # Iterate through websites
    for site in config['sites']:
        html = get_html(site)
        check_sale(html, config['parts'])


if __name__ == '__main__':
    main()
