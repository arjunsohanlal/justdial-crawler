import scrapy
import json

class jsSpider(scrapy.Spider):
    name = "justdialcrawl"

    # Headers for main page response
    headers_main = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }

    # Headers for paginated HTML responses
    headers_paginated = {
            "accept":"application/json, text/javascript, */*; q=0.01",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"en-US,en;q=0.9",
            "referer":"https://www.justdial.com/Delhi/House-On-Rent/nct-10192844",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "x-requested-with":"XMLHttpRequest"
        }
    
    # Essential cookie keys
    cookie_keys = ['ppc', 'TKY', '_ctok', 'main_city', 'akcty', 'inweb_city', 'attn_user', 'profbd', 'bdcheck', 'ak_bmsc', 'PHPSESSID', 'bm_mi']
    
    # Simple lookup dictionary for reading numbers off of CSS classes
    charDict = {
            'acb': '0',
            'yz': '1',
            'wx': '2',
            'vu': '3',
            'ts': '4',
            'rq': '5',
            'po': '6',
            'nm': '7',
            'lk': '8',
            'ji': '9',
            'hg': ')',
            'fe': '(',
            'dc': '+',
            'ba': '-'
        }
    
    # This is a built-in Scrapy function that runs first where we'll override the default headers
    # Documentation: https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.start_requests
    def start_requests(self):
        # First request on main page data
        url = 'https://www.justdial.com/Delhi/House-On-Rent/nct-10192844'
        yield scrapy.http.Request(url, headers=self.headers_main, callback=self.parse_main)

    # Standard parse function for response from main page
    def parse_main(self, response):
        # Pulling current cookies into dictionary 
        main_cookie_list = response.headers.getlist('Set-Cookie')
        main_cookie_list = [str(x)[2:].split(';')[0] for x in main_cookie_list]
        main_cookie_dict = { x.split('=',1)[0] : x.split('=',1)[1] for x in main_cookie_list }
        
        # Setting up new cookies for upcoming paginated HTML requests
        new_cookie_dict = {}
        new_cookie_str = ""

        # Referencing essential cookie key list
        for key in self.cookie_keys:
            new_cookie_dict[key] = main_cookie_dict.get(key,"")
            new_cookie_str = new_cookie_str + key + '=' + new_cookie_dict[key] + "; "
        new_cookie_str = new_cookie_str[:-2]

        # Storing new cookies
        self.headers_paginated['cookie'] = new_cookie_str

        # Extracting and storing CSRF auth token for new requests
        frsc = response.xpath('//meta[18]/@content').get()
        self.headers_paginated['x-frsc-token'] = str(frsc)
        
        # Iterating through list of companies
        for company in response.css("li.cntanr"):
            # Yielding each company's details in a dictionary format
            yield {
                'name': company.css('span.lng_cont_name::text').get(),
                'rating': float(company.css('span.exrt_count::text').get()),
                'phone': self.get_phone(company),
                'address': company.css("span.adWidth::text").get().strip('\t|\n'),
            }

        # Request URL for paginated HTML (lazy loaded section of the page)    
        url_paginated = "https://www.justdial.com/functions/ajxsearch.php?national_search=0&act=pagination_new&city=Delhi&search=House%20On%20Rent&where=&catid=0&psearch=&prid=&page=2&SID=&mntypgrp=0&toknbkt=&bookDate=&jdsrc=&median_latitude=28.664407557287&median_longitude=77.090145924828&ncatid=10192844&mncatname=Estate%20Agents%20For%20Residential%20Rental&dcity=Delhi&pncode=999999&htlis=0"
        yield scrapy.http.Request(url_paginated, headers=self.headers_paginated, callback=self.parse_paginated)

    def parse_paginated(self, response):
        # Parsing JSON response into dictionary
        parsedJson = json.loads(response.text)

        # Condition to check if JSON from requested URL is empty
        # Necessary to end recursive call of parse_paginated()
        if (parsedJson.get("results",0) == []):
            print("INTERNAL DEBUG: End of paginated lists.")
            return None

        # Constructing new scrapy.Selector object from HTML embedded in JSON (parsedJSON)
        selected = scrapy.Selector(text=parsedJson['markup'], type="html")

        # Iterating through each company listing
        for company in selected.css("li.cntanr"):
            # Yielding each company's details in a dictionary format
            yield {
                'name': company.css('span.lng_cont_name::text').get(),
                'rating': float(company.css('span.exrt_count::text').get()),
                'phone': self.get_phone(company),
                'address': company.css("span.adWidth::text").get().strip('\t|\n'),
            }

        # Generating request URL for next paginated HTML response
        old_url = response._url
        page_num_start = old_url.find('page=') + len('page=')
        page_num_end = old_url[page_num_start:].find('&') + page_num_start
        new_page_num = int(old_url[page_num_start:page_num_end]) + 1
        new_url = old_url[:page_num_start] + str(new_page_num) + old_url[page_num_end:]

        # Recursive call into parse_paginated() for newer responses
        yield scrapy.http.Request(new_url, headers=self.headers_paginated, callback=self.parse_paginated)

    def get_phone(self,company):
        # Listing out CSS classes of each element in <span> element containing number
        proxyPhone = company.css('span.mobilesv::attr(class)').getall()
        # Trimming out country codes
        charList = [x.split('-')[1] for x in proxyPhone]
        # Retrieving phone number from charDict lookup
        phone = ''.join(self.charDict.get(x) for x in charList)[6:]
        return phone
