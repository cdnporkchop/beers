#import requests
import urllib2
from pyquery import PyQuery

class BeerFetcher:
    def __init__(self):
        self.base_url = 'http://www.thebeerstore.ca'
        self.search_suffix = '/beers/search'

    def fetch_all(self):
        page = urllib2.urlopen(self.base_url + self.search_suffix)
        pq = PyQuery(page.read())

        number_of_beers = len(pq(".brand-link"))
        beer = 0
        print '# Beers', number_of_beers
        while beer < number_of_beers:
            beer_details_url = self.base_url + pq(".brand-link")[beer].attrib['href']
            self.fetch_details(beer_details_url)        # self.fetch_details('http://www.thebeerstore.ca/beers/keiths')
            beer += 1

    @staticmethod
    def fetch_details(details_url):
        print 'Fetching Details for: ', details_url
        page = urllib2.urlopen(details_url)
        pq = PyQuery(page.read())

        container_options = pq(".brand-pricing-wrapper table")
        current_option=0
        while current_option < container_options.size():
            print 'Container: ', pq(".brand-pricing-wrapper table")[current_option][0][0][0].text  # CAN / BOTTLE / KEG
            option_items = pq(".brand-pricing-wrapper table tbody")[current_option].findall('tr')
            container_option=0
            while container_option < len(option_items):
                size = pq(".brand-pricing-wrapper table tbody")[current_option].findall('tr')[container_option].find('td').text
                price = pq(".brand-pricing-wrapper table tbody")[current_option].findall('tr')[container_option][1].text
                locations = pq(".brand-pricing-wrapper table tbody")[current_option].findall('tr')[container_option][2][0].attrib['href']
                if price is None:
                    price = pq(".brand-pricing-wrapper table tbody")[current_option].findall('tr')[container_option][1][1].text
                    old_price = pq(".brand-pricing-wrapper table tbody")[current_option].findall('tr')[container_option][1][0].text
                    print 'old price: ' + old_price
                print size + ' ' + price + ' ' + locations
                container_option += 1
            current_option += 1

beer = BeerFetcher()
beer.fetch_all()
