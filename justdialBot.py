import scrapy
import json

class jsSpider(scrapy.Spider):
    name = "justdial4"

    headers_paginated = {
            "accept":"application/json, text/javascript, */*; q=0.01",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"en-US,en;q=0.9",
            "cookie":"ppc=; TKY=c0bf3418a73b1fd4bd6ef5166684f897c17919161f1235018d81851fdad41f06; _ctok=5c72268a8bd489e3e5d3424fb3434fd87eace35dbb5cdab06e1e265f67d9fa0e; main_city=Delhi; akcty=Delhi; inweb_city=Delhi; attn_user=logout; profbd=0; bdcheck=1; tab=toprs; bd_inputs=2|4|Estate%20Agents%20For%20Residential%20Rental; view=lst_v; scity=Delhi; sarea=; dealBackCity=Delhi; docidarray=%7B%22011PXX11.XX11.150930185126.K1Q8%22%3A%222020-07-24%22%7D; prevcatid=10192844; BDprofile=1; PHPSESSID=42829c31e453f2a14063ca9de1ee9f66; ak_bmsc=F2505E4BC81B9C5DEA2A1C44775F93DD173945A0BB7C00006F451C5FDF616E73~plWSVS24KDVTJRYsLkfuW24jtEtUsTUVe8gd2y76bksvJcwZResN13n6Hk4mF1aR14Bk/m9waBXf26SEkY7GT87QvY8ngYkuHetQy9+S5HVNhxW3XkNmhd6TsppwtsKp7YbdQ/AhVLyS1etttmZxKwcp4W9gDRWFHNZpZzqb4H+VU0l1KLZabYTSphw1hob/z3v4Ul3zxsiYv1RM9AVvEpYw2v+ievMrIclgndACxS2E4=; bm_mi=E03C31427DF290A373FC34515961DF68~vaRaKxxO09W/7d27AFTFO3IAwVx3bHrcgFlRV4jt6mF4etoWE6/77idPt8lH4MHEw/lDLdQxXnsTpbE3bBJPELeG2gxp+Rd9ECcsIDt+TmS6DrR1ffgzOWkB2edpvqENQ6IqcQaNMN3D3DOEZ/10Al1uanYwGkfJ2jWz1WFQVcwh5dh9xxntPz8tTiLevQylyawdyYPGj96uh8LP5JnL7fOM8t+73L3I9sY+8wG+DYMYFpjQBODVNuGwEk8xLRCj; bm_sv=063F8B5A31AC59E6EC453CCA774449E1~XLHphGaFVN/uqZ6VzM6ty28hsi07eygR1QoaH4TC62b0fi6AI+0LfT0VEfc8eJtZPwvL3kNBPy+QbVHqIXcYk/ckdy4h+LodMd3T4tHqcCmgxGyhQDDHZTOvSauJjd8kTdQuTW0aRP60IE20kA+xHS1DhkNZOU9slBT42BPTiUQ=",
            "referer":"https://www.justdial.com/Delhi/House-On-Rent/nct-10192844",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "x-frsc-token":"c0bf3418a73b1fd4bd6ef5166684f897c17919161f1235018d81851fdad41f06",
            "x-requested-with":"XMLHttpRequest"
        }

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
        url = 'https://www.justdial.com/Delhi/House-On-Rent/nct-10192844'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'ppc=; TKY=c0bf3418a73b1fd4bd6ef5166684f897c17919161f1235018d81851fdad41f06; _ctok=5c72268a8bd489e3e5d3424fb3434fd87eace35dbb5cdab06e1e265f67d9fa0e; main_city=Delhi; akcty=Delhi; inweb_city=Delhi; attn_user=logout; profbd=0; bdcheck=1; tab=toprs; bd_inputs=2|4|Estate%20Agents%20For%20Residential%20Rental; view=lst_v; scity=Delhi; sarea=; dealBackCity=Delhi; docidarray=%7B%22011PXX11.XX11.150930185126.K1Q8%22%3A%222020-07-24%22%7D; prevcatid=10192844; BDprofile=1; PHPSESSID=42829c31e453f2a14063ca9de1ee9f66; ak_bmsc=F2505E4BC81B9C5DEA2A1C44775F93DD173945A0BB7C00006F451C5FDF616E73~plWSVS24KDVTJRYsLkfuW24jtEtUsTUVe8gd2y76bksvJcwZResN13n6Hk4mF1aR14Bk/m9waBXf26SEkY7GT87QvY8ngYkuHetQy9+S5HVNhxW3XkNmhd6TsppwtsKp7YbdQ/AhVLyS1etttmZxKwcp4W9gDRWFHNZpZzqb4H+VU0l1KLZabYTSphw1hob/z3v4Ul3zxsiYv1RM9AVvEpYw2v+ievMrIclgndACxS2E4=; bm_mi=E03C31427DF290A373FC34515961DF68~vaRaKxxO09W/7d27AFTFO3IAwVx3bHrcgFlRV4jt6mF4etoWE6/77idPt8lH4MHEw/lDLdQxXnsTpbE3bBJPELeG2gxp+Rd9ECcsIDt+TmS6DrR1ffgzOWkB2edpvqENQ6IqcQaNMN3D3DOEZ/10Al1uanYwGkfJ2jWz1WFQVcwh5dh9xxntPz8tTiLevQylyawdyYPGj96uh8LP5JnL7fOM8t+73L3I9sY+8wG+DYMYFpjQBODVNuGwEk8xLRCj; bm_sv=063F8B5A31AC59E6EC453CCA774449E1~XLHphGaFVN/uqZ6VzM6ty28hsi07eygR1QoaH4TC62b0fi6AI+0LfT0VEfc8eJtZPwvL3kNBPy+QbVHqIXcYk/ckdy4h+LodMd3T4tHqcCkiX2Y/CaXlOv0fB7o3qtz5OP3nMJLSWCzAPZZK0qh9K90v5+WlBfZK1yMlEdtY9rs=',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }

        yield scrapy.http.Request(url, headers=headers, callback=self.parse)

        url_paginated = "https://www.justdial.com/functions/ajxsearch.php?national_search=0&act=pagination_new&city=Delhi&search=House%20On%20Rent&where=&catid=0&psearch=&prid=&page=2&SID=&mntypgrp=0&toknbkt=&bookDate=&jdsrc=&median_latitude=28.664407557287&median_longitude=77.090145924828&ncatid=10192844&mncatname=Estate%20Agents%20For%20Residential%20Rental&dcity=Delhi&pncode=999999&htlis=0"
        yield scrapy.http.Request(url_paginated, headers=self.headers_paginated, callback=self.parse_paginated)

    def parse(self, response):
        for company in response.css("li.cntanr"):
            proxyPhone = company.css('span.mobilesv::attr(class)').getall()
            charList = [x.split('-')[1] for x in proxyPhone]
            phone = ''.join(self.charDict.get(x) for x in charList)[6:]
            
            yield {
                'name': company.css('span.lng_cont_name::text').get(),
                'rating': float(company.css('span.exrt_count::text').get()),
                'phone': phone,
                'address': company.css("span.adWidth::text").get().strip('\t|\n'),
            }

    def parse_paginated(self, response):
        print("CALLED!")
        # print('--------------'+str(len(response)))
        parsedJson = json.loads(response.text)

        if (parsedJson.get("results",0) == []):
            print("****************** NONE RETURNED")
            return None

        print(parsedJson.keys())
        print("--------------------Len of markup: "+str(len(parsedJson.get("markup"))))
        print("--------------------Type of markup: "+str(type(parsedJson.get("markup"))))

        selected = scrapy.Selector(text=parsedJson['markup'], type="html")

        for company in selected.css("li.cntanr"):
            proxyPhone = company.css('span.mobilesv::attr(class)').getall()
            charList = [x.split('-')[1] for x in proxyPhone]
            phone = ''.join(self.charDict.get(x) for x in charList)[6:]
            yield {
                'name': company.css('span.lng_cont_name::text').get(),
                'rating': float(company.css('span.exrt_count::text').get()),
                'phone': phone,
                'address': company.css("span.adWidth::text").get().strip('\t|\n'),
            }

        
        old_url = response._url
        page_num_start = old_url.find('page=') + len('page=')
        page_num_end = old_url[page_num_start:].find('&') + page_num_start
        new_page_num = int(old_url[page_num_start:page_num_end]) + 1
        new_url = old_url[:page_num_start] + str(new_page_num) + old_url[page_num_end:]

        yield scrapy.http.Request(new_url, headers=self.headers_paginated, callback=self.parse_paginated)
