import requests
import time
import urllib2
from pyquery import PyQuery


class BeverageFetcher:
    def __init__(self):
        print 'init'
        self.urlAles = 'http://www.lcbo.com/lcbo/catalog/ale/11022#contentBeginIndex=0&productBeginIndex=432&beginIndex=432&orderBy=&categoryPath=beer%2Fale&pageView=grid&resultType=products&orderByContent=&searchTerm=&facet=&storeId=10151&catalogId=10001&langId=-1&fromPage=&objectId=&requesttype=ajax'
                   #http://www.lcbo.com/lcbo/catalog/ale/11022#contentBeginIndex=0&productBeginIndex=12&beginIndex=12&orderBy=&categoryPath=beer%2Fale&pageView=&resultType=products&orderByContent=&searchTerm=&facet=&storeId=10151&catalogId=10001&langId=-1&fromPage=&objectId=&requesttype=ajax
                   #http://www.lcbo.com/lcbo/catalog/ale/11022#contentBeginIndex=0&productBeginIndex=24&beginIndex=24&orderBy=&categoryPath=beer%2Fale&pageView=&resultType=products&orderByContent=&searchTerm=&facet=&storeId=10151&catalogId=10001&langId=-1&fromPage=&objectId=&requesttype=ajax
        self.urlMalts = 'http://www.lcbo.com/lcbo/catalog/malt-beverages/11501'
        self.urlLagers = 'http://www.lcbo.com/lcbo/catalog/lager/11027'
        self.urlHybrids = 'http://www.lcbo.com/lcbo/catalog/hybrid/11007'
        self.urlSpecialty = 'http://www.lcbo.com/lcbo/catalog/specialty/11006'
        self.urlCiders = 'http://www.lcbo.com/lcbo/catalog/cider/11013'
        self.urlGifts = 'http://www.lcbo.com/lcbo/catalog/gift-and-sampler-packs/11002'

    def fetch_ales(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlAles)
        total = self.getCounts(page)[2]
        print "# Ales: ", total

        current_pos = 0
        while current_pos < total:
             current_pos = self.fetchBeers('http://www.lcbo.com/lcbo/catalog/ale/11022#contentBeginIndex=0&orderBy=&categoryPath=beer%2Fale&pageView=&resultType=products&orderByContent=&searchTerm=&facet=&storeId=10151&catalogId=10001&langId=-1&fromPage=&requesttype=ajax&objectId=&productBeginIndex=', '&beginIndex=', current_pos, total, 12)

    #    page = urllib2.urlopen(self.urlAles)
    #    pq = PyQuery(page.read())
    #    page_total = pq('.product-name').size()
    #    current = 0
    #    while current < page_total:
    #        beer = pq('.product-name a')[current]
    #        print 'title: ' + beer.attrib['title']
    #        print 'href: ' + beer.attrib['href']
    #      #  print 'code: ' + pq('.product-code')[current].text
           # code = pq('.product-code')[current].text
           # print code.find(" ")
    #        print 'LCBO #: ' + pq('.product-code .plp-volume-grid')[current][0].tail
    #        print 'Price: ' + pq('.product-price .price')[current].text
    #        print 'Country: ' + pq('.product-extra .country')[current].text
    #        print 'Producer: ' + pq('.product-extra .producer')[current].text
            #discontinued? pq('.product-extra')[0][1].text
            #seasonal pq('.product-extra')[6][1].text
            #pq('.product-extra')[current][1].text == 'Product Discontinued'
    #        if not pq('.product-extra')[current][1].attrib['class'] == 'air-miles' :
    #            if pq('.product-extra')[current][1].attrib['class'] == 'product-discontinued' :
    #                print pq('.product-extra')[current][1].text
    #            if pq('.product-extra')[current][1].attrib['class'] == 'seasonal-product' :
    #                print pq('.product-extra')[current][1].text#

    #        print 'img src :' + pq('.product-image a img')[current].attrib['src']
    #        print 'img alt:' + pq('.product-image a img')[current].attrib['alt']
            #img src pq('.product-image')[current][0][0].attrib['src']
            #        pq('.product-image a img')[current].attrib['src']
            # full image http://www.lcbo.com/content/dam/lcbo/products/026971.jpg/jcr:content/renditions/cq5dam.web.1280.1280.jpeg

            #details at http://www.lcbo.com/lcbo/product/spitfire-premium-ale/32029
            #500 mL bottle
            #Alcohol/Vol4.5%
            #Made in:England, United Kingdom
            #By:Shepherd Neame
            #Style:Medium & Hoppy
            #
            #Colour; deep amber. Aromas; hops and spices. Palate; dry, full-bodied, tangy and malty.
            #Inventory:
            #http://www.foodanddrink.ca/lcbo-ear/lcbo/product/inventory/searchResults.do?language=EN&itemNumber=32029&version=mobile

     #       current=current+1


        #pq('.product-name').size() #12 from 0 to 11
        #pq('.product-name a').attr['title']
        #pq('.product-name a').attr['href']

#for link in e('li.

        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_malts(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlMalts)
        print "# Malts: ", self.getCounts(page)[2]
        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_lagers(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlLagers)
        print "# Lagers: ", self.getCounts(page)[2]
        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_hybrids(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlHybrids)
        print "# Hybrids: ", self.getCounts(page)[2]
        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_specialty(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlSpecialty)
        print "# Specialty: ", self.getCounts(page)[2]
        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_ciders(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlCiders)
        print "# Ciders: ", self.getCounts(page)[2]
        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_gift_and_sampler_packs(self):
        tStartParseClock = time.clock()
        page = urllib2.urlopen(self.urlGifts)
        print "# Gift&SamplerPacks: ", self.getCounts(page)[2]
        print 'fetch took [%.2f] seconds' %((time.clock()-tStartParseClock))

    def fetch_all(self):
        self.fetch_ales()
        self.fetch_malts()
        self.fetch_ciders()
        self.fetch_gift_and_sampler_packs()
        self.fetch_hybrids()
        self.fetch_lagers()
        self.fetch_specialty()

    def getCounts(self, page):
        pq = PyQuery(page.read())
        lcbo_only = pq('#facet_count-1043116114117101').html()
        vintage_only = pq('#facet_count-1042116114117101').html()

        if vintage_only is None:
            vintage_only = 0
        if lcbo_only is None:
            lcbo_only = 0
        return int(lcbo_only), int(vintage_only), (int(lcbo_only) + int(vintage_only))

    def fetchBeers(self, url_base, url_suffix, current_pos, end_pos, page_size):
        #http://www.lcbo.com/lcbo/catalog/ale/11022#facet=&requesttype=ajax&productBeginIndex=12&beginIndex=12
        new_url = url_base + str(current_pos) + url_suffix + str(current_pos)
        print 'fetching URL: ' + new_url
        page = urllib2.urlopen(new_url)
        pq = PyQuery(page.read())

        current = 0
        while (current < page_size) & ((current + current_pos) < end_pos) :
            beer = pq('.product-name a')[current]
            print 'ALE #' + str(current_pos)
            print ' title: ' + beer.attrib['title']
            print ' href: ' + beer.attrib['href']
          #  print 'code: ' + pq('.product-code')[current].text
           # code = pq('.product-code')[current].text
           # print code.find(" ")
            print ' LCBO #: ' + pq('.product-code .plp-volume-grid')[current][0].tail
            print ' Price: ' + pq('.product-price .price')[current].text
            print ' Country: ' + pq('.product-extra .country')[current].text
            print ' Producer: ' + pq('.product-extra .producer')[current].text
            #discontinued? pq('.product-extra')[0][1].text
            #seasonal pq('.product-extra')[6][1].text
            #pq('.product-extra')[current][1].text == 'Product Discontinued'
            if not pq('.product-extra')[current][1].attrib['class'] == 'air-miles' :
                if pq('.product-extra')[current][1].attrib['class'] == 'product-discontinued' :
                    print ' ' + pq('.product-extra')[current][1].text
                if pq('.product-extra')[current][1].attrib['class'] == 'seasonal-product' :
                    print ' ' + pq('.product-extra')[current][1].text

            print ' img src :' + pq('.product-image a img')[current].attrib['src']
            print ' img alt:' + pq('.product-image a img')[current].attrib['alt']

            current=current+1
            current_pos = current_pos + 1
        return current_pos




#bf = BeverageFetcher()
#bf.fetch_all()
#payload = ''
#r = requests.post("http://www.thebeerstore.ca/beers/search", data=payload)
#print r.status_code
#print r.content