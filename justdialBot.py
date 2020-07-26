import scrapy
import json

class jsSpider(scrapy.Spider):
    name = "justdialcrawl"

    # Headers for main page response
    headers_main = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'ppc=; TKY=8414a442ee750876e3fc08c5b8f60f25c84b5da6239f77b3b0c8970ead23530c; _ctok=c60d64f66892cf5baf99a56a8ebc929e7bb4192ccc84b37ab8cbe6b0eb4f0b6d; main_city=Delhi; akcty=Delhi; inweb_city=Delhi; attn_user=logout; PHPSESSID=fba34180ed9b2ceaa2c352528d505570; profbd=0; bdcheck=1; ak_bmsc=3D3018614F18A1C85D5020DB7D07757F7D38DE9C674B0000BD4F1D5F3D7E9F75~plgiULj+AntRuvycXOiMTO74YGM3ro+wzn/+fPezrcO3V/oeSalUwHlMCt0mzB/kZVSoNUsHwUaASJmk/kaVMlu7UgI8pDY9iCKJU7lLl39eT4STtTLsl5wqPRcG60oAtLt7C2CynJPcJD/L/Ypa4NxuX2ddyPAfx8w54LwHZk+eaLWbBvcCS05LabcgC1AFAk0Z/pQjp9/bOkikUxCj/QbE0ixnEtQRLa61od/9i3QDM=; tab=toprs; prevcatid=10192844; bd_inputs=2|4|Estate%20Agents%20For%20Residential%20Rental; view=lst_v; scity=Delhi; sarea=; dealBackCity=Delhi; BDprofile=1; bm_mi=EEA783DBF4C6CACA9E1B4070CEC8A441~Bikg1G6eA9IlRDxSpTd/KZn7eagwgji0q4w6M/hqVRxG7v4tiel6shl0zNVBpsp8/N/z+IpIHrgUMgnrXO9gGmlKpLaR5HnfNWY0fjKyBn//l9Ia+or2VvHhtye1vaQv4H1oa9/rSHNElqY/6/6Lao2Mtif6DAIMBjvd4n1vD6BBO7cRkBj0kPE5DASzTqWOm3CQ3mC1K18madU+cVXSW7KdGtmD/XyzIAZdbeWyErA9T9F4WZW+3uoncfj17I95IaVpBT/Wxy5frmDVV9eZJA==; bm_sv=8127AFCF4CA83E61A985C6EBE2D671FE~9Bpd/4lRHLrpicigwbICGCgVxbFVc9gFqbxxCD8ftNOBN5AvnrvSz+qESYgKBfw9pWBp0cjtf7Zbq01EOtnoERNz9Zfpl9SOg0oU3EIzXxWYj2URXKszas7wrd6mnEwksja+888cPxAX6ursug0FkBFia/i6fz0uAFRdpOT3eVg=',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }

    # Headers for paginated HTML responses
    headers_paginated = {
            "accept":"application/json, text/javascript, */*; q=0.01",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"en-US,en;q=0.9",
            "cookie":"ppc=; TKY=8414a442ee750876e3fc08c5b8f60f25c84b5da6239f77b3b0c8970ead23530c; _ctok=c60d64f66892cf5baf99a56a8ebc929e7bb4192ccc84b37ab8cbe6b0eb4f0b6d; main_city=Delhi; akcty=Delhi; inweb_city=Delhi; attn_user=logout; PHPSESSID=fba34180ed9b2ceaa2c352528d505570; profbd=0; bdcheck=1; ak_bmsc=3D3018614F18A1C85D5020DB7D07757F7D38DE9C674B0000BD4F1D5F3D7E9F75~plgiULj+AntRuvycXOiMTO74YGM3ro+wzn/+fPezrcO3V/oeSalUwHlMCt0mzB/kZVSoNUsHwUaASJmk/kaVMlu7UgI8pDY9iCKJU7lLl39eT4STtTLsl5wqPRcG60oAtLt7C2CynJPcJD/L/Ypa4NxuX2ddyPAfx8w54LwHZk+eaLWbBvcCS05LabcgC1AFAk0Z/pQjp9/bOkikUxCj/QbE0ixnEtQRLa61od/9i3QDM=; tab=toprs; prevcatid=10192844; bd_inputs=2|4|Estate%20Agents%20For%20Residential%20Rental; view=lst_v; scity=Delhi; sarea=; dealBackCity=Delhi; BDprofile=1; bm_mi=EEA783DBF4C6CACA9E1B4070CEC8A441~Bikg1G6eA9IlRDxSpTd/KZn7eagwgji0q4w6M/hqVRxG7v4tiel6shl0zNVBpsp8/N/z+IpIHrgUMgnrXO9gGmlKpLaR5HnfNWY0fjKyBn/cBnW5HPssYKr3Z82FlMHxaZqUykELdGVSu6qX/NKSM5UTA4C7p/k2127DbrMG419dA9Ka19ULeyr4phq8kMUNF/3bhZnKBnz4sSc1xc1TR0jRcnx9xDkKdqTuPTWZf4TaSCRkl9y4a/czztP54qHPhZ5pfmnaHn2aXbPrDRRPlQ==; bm_sv=8127AFCF4CA83E61A985C6EBE2D671FE~9Bpd/4lRHLrpicigwbICGCgVxbFVc9gFqbxxCD8ftNOBN5AvnrvSz+qESYgKBfw9pWBp0cjtf7Zbq01EOtnoERNz9Zfpl9SOg0oU3EIzXxWVAPq3lutpHJHhtdcJcwIAaz5ez8zYve5th3Pb6RiSKul578cuBNSCixgqZuXOeAE=",
            "referer":"https://www.justdial.com/Delhi/House-On-Rent/nct-10192844",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "x-frsc-token":"8414a442ee750876e3fc08c5b8f60f25c84b5da6239f77b3b0c8970ead23530c",
            "x-requested-with":"XMLHttpRequest"
        }

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
        url_main = 'https://www.justdial.com/Delhi/House-On-Rent/nct-10192844'
        yield scrapy.http.Request(url_main, headers=self.headers_main, callback=self.parse_main)

        # Request URL for paginated HTML (lazy loaded section of the page)
        url_paginated = "https://www.justdial.com/functions/ajxsearch.php?national_search=0&act=pagination_new&city=Delhi&search=House%20On%20Rent&where=&catid=0&psearch=&prid=&page=2&SID=&mntypgrp=0&toknbkt=&bookDate=&jdsrc=&median_latitude=28.664407557287&median_longitude=77.090145924828&ncatid=10192844&mncatname=Estate%20Agents%20For%20Residential%20Rental&dcity=Delhi&pncode=999999&htlis=0"
        yield scrapy.http.Request(url_paginated, headers=self.headers_paginated, callback=self.parse_paginated)


    # Standard parse function for response from main page
    def parse_main(self, response):
        # Iterating through list of companies
        for company in response.css("li.cntanr"):
            # Yielding each company's details in a dictionary format
            yield {
                'name': company.css('span.lng_cont_name::text').get(),
                'rating': float(company.css('span.exrt_count::text').get()),
                'phone': self.get_phone(company),
                'address': company.css("span.adWidth::text").get().strip('\t|\n'),
            }

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
