import sys,os
sys.path.append(os.path.abspath('..'))
from beers.connectivity.MongoDBConnection import MongoDBConnection
import time
import json
import urllib2
from pyquery import PyQuery

class BeerFetcher:
    def __init__(self):
        self.base_url = 'http://www.thebeerstore.ca'
        self.search_suffix = '/beers/search'


    def fetch_all(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.base_url + self.search_suffix)
        pq = PyQuery(page.read())

        mongodb = MongoDBConnection()
        number_of_beers = len(pq(".brand-link"))
        beer = 0
        print '# Beers', number_of_beers
        while beer < number_of_beers:
            beer_details_url = self.base_url + pq(".brand-link")[beer].attrib['href']
            data = self.fetch_details(beer_details_url)        # self.fetch_details('http://www.thebeerstore.ca/beers/keiths')
            mongodb.insert_beer(data)
            beer += 1
        print 'fetch_all took [%.2f] seconds' %((time.clock()-tStartParseClock))

    @staticmethod
    def fetch_details(details_url):
        print 'Fetching Details for: ', details_url
        tStartParseClock = time.clock()
        page = urllib2.urlopen(details_url)
        pq = PyQuery(page.read())

        container_options = pq(".brand-pricing-wrapper table")
        current_option=0
        data_container = []
        while current_option < container_options.size():
            container_type = pq(".brand-pricing-wrapper table")[current_option][0][0][0].text   # CAN / BOTTLE / KEG
            #print 'Container: ', container_type
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
                #print size + ' ' + price + ' ' + locations
                data_container.append(({"type" : container_type, "size" : size, "price" : price, "location" : locations}))
                container_option += 1
            current_option += 1

        data_beer = {}
        data_beer['href'] = details_url
        data_beer['name'] = pq(".brand-info-container .brand-info-inner .only-desktop .page-title")[0].text
        desc = ''
        if len(pq(".brand-info-container .brand-info-inner .brand-description p")) > 0:
            desc = pq(".brand-info-container .brand-info-inner .brand-description p")[0].text
        data_beer['description'] = desc
        data_beer['brewer'] = pq(".brand-info-container dl dd")[0].text
        data_beer['alcohol'] = pq(".brand-info-container dl dd")[1].text
        data_beer['type'] = pq(".brand-info-container .brand-introduction span")[0].text
        data_beer['brewed'] = pq(".brand-info-container .brand-introduction span")[1].text
        data_beer['sizes'] = data_container
        json_beer = json.dumps(data_beer)
        print 'fetch_details took [%.2f] seconds' %((time.clock()-tStartParseClock))
        print json_beer
        return data_beer




beer = BeerFetcher()
beer.fetch_all()
#BeerFetcher.fetch_details("http://www.thebeerstore.ca/beers/hersbrucker-pilsner")  # No Description Test (this one has no desc)
