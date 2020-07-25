import scrapy
import json

class jsSpider(scrapy.Spider):
    name = "justdial3"

    headers_paginated = {
            "accept":"application/json, text/javascript, */*; q=0.01",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"en-US,en;q=0.9",
            "cookie": "",
            # "cookie":"ppc=; TKY=c0bf3418a73b1fd4bd6ef5166684f897c17919161f1235018d81851fdad41f06; _ctok=5c72268a8bd489e3e5d3424fb3434fd87eace35dbb5cdab06e1e265f67d9fa0e; main_city=Delhi; akcty=Delhi; inweb_city=Delhi; attn_user=logout; profbd=0; bdcheck=1; tab=toprs; bd_inputs=2|4|Estate%20Agents%20For%20Residential%20Rental; view=lst_v; scity=Delhi; sarea=; dealBackCity=Delhi; docidarray=%7B%22011PXX11.XX11.150930185126.K1Q8%22%3A%222020-07-24%22%7D; prevcatid=10192844; BDprofile=1; ak_bmsc=604928AB3FE085DB253C8F59815E771017CB3F1CE150000061121C5F70E63B67~plnDsavxg/M7Sg2/VYU3REmc6SVqbe1u1lcc8o8tW96VCP4OCHW6XSotj+UKLgi4qVUNBwtA+30PK9gVt6LZnB7J6RVQRWelvH85otQ0eTMUVZDnn3Hz4QWojBA4QLWu08mbG0f0vaEb/xeGHQOJq0B9UiopxMiSOKx4PS5f6BI8fObEV5g2qmp7FRWzjZml8lxHlLK0xdzqqXXEDMqOo3G0FbipguKsuhWjTDCSH+xFA=; PHPSESSID=8v0h9cjkp62q0j0dcogcpb5q22; bm_mi=0B35FCCD50D8E56AB54B93FF2ED14813~/K5ZmkanMyeqABEyHRnSV6VR3c/GEP9S83fy2GvuLZP0/0zUjMF3u4qe8stnoS7GHvoN5oCSuT8yjwGFJPfb/3aru8b7htfGP74Cf94VmWNzXwdimkcD3PmlZFxH0rTlHGlzrPcH0w9yk8YbDJdSlxMBDTZ9ez+TJrTGKRbCn/BG2TBbce28mf+kFFyhsj/gQVz639A6bSwfGgQCHa4IOAGbfHZf38pJEvIFqUZ36R0uF3DwJs5BGQgM/0Q4ofs8Dc5Ce2gc9nY0+469g8aGxw==; bm_sv=E96C287E40EC63914A75D2D77DC10253~hX56gQLuLI4vftBWp2H/FjD6NlmmWGBBvbpP0ILK9Da4boDG+GeLvUXpDEGEzykxaQUTyEkz1y6fE4RjdDIk00jd/afUNxynJCQwV3RJBeCAUUVpOOpG0z4qtkXV+gKWrLpDJBWofLhX9kvbn0OX79I/7vhX1vgRH84sFpdtKaQ=",
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
            # 'cookie': 'ppc=; TKY=c0bf3418a73b1fd4bd6ef5166684f897c17919161f1235018d81851fdad41f06; _ctok=5c72268a8bd489e3e5d3424fb3434fd87eace35dbb5cdab06e1e265f67d9fa0e; main_city=Delhi; akcty=Delhi; inweb_city=Delhi; attn_user=logout; profbd=0; bdcheck=1; tab=toprs; bd_inputs=2|4|Estate%20Agents%20For%20Residential%20Rental; view=lst_v; scity=Delhi; sarea=; dealBackCity=Delhi; detailmodule=011PXX11.XX11.150930185126.K1Q8; docidarray=%7B%22011PXX11.XX11.150930185126.K1Q8%22%3A%222020-07-24%22%7D; PHPSESSID=d9b35d5fa2d8694f3864d8d53589a31c; prevcatid=10192844; BDprofile=1; ak_bmsc=604928AB3FE085DB253C8F59815E771017CB3F1CE150000061121C5F70E63B67~plnDsavxg/M7Sg2/VYU3REmc6SVqbe1u1lcc8o8tW96VCP4OCHW6XSotj+UKLgi4qVUNBwtA+30PK9gVt6LZnB7J6RVQRWelvH85otQ0eTMUVZDnn3Hz4QWojBA4QLWu08mbG0f0vaEb/xeGHQOJq0B9UiopxMiSOKx4PS5f6BI8fObEV5g2qmp7FRWzjZml8lxHlLK0xdzqqXXEDMqOo3G0FbipguKsuhWjTDCSH+xFA=; bm_mi=0B35FCCD50D8E56AB54B93FF2ED14813~/K5ZmkanMyeqABEyHRnSV6VR3c/GEP9S83fy2GvuLZP0/0zUjMF3u4qe8stnoS7GHvoN5oCSuT8yjwGFJPfb/3aru8b7htfGP74Cf94VmWPNC119nneiDrg1AF4bcNnya6hameRJGUjK4n6dzqifiCwyMvn5rTgFLBz9BltMlhBSYuGFvSIiE6rt6HEp14X2zxsaZMJVmhy5r1ZxiW/QABYgTYJwXsDTvcpOeiTh8Uv2CGlLa8ckmAlsyIjBqWyYxtkV3JXY8nCEKoIlhol1Aw==; bm_sv=E96C287E40EC63914A75D2D77DC10253~hX56gQLuLI4vftBWp2H/FjD6NlmmWGBBvbpP0ILK9Da4boDG+GeLvUXpDEGEzykxaQUTyEkz1y6fE4RjdDIk00jd/afUNxynJCQwV3RJBeBbh+7E8b5Dzkudp6t7Qfu9IxN5Xb7K+J5GXpfH5vHcm1kevy+QBta2MMSHcpb+StM=; ppc=; main_city=Delhi; attn_user=logout; profbd=0; bdcheck=1; PHPSESSID=3f5954d25448f1d8a93a019a41d84073; akcty=Delhi; inweb_city=Delhi; bm_mi=0B35FCCD50D8E56AB54B93FF2ED14813~/K5ZmkanMyeqABEyHRnSV6VR3c/GEP9S83fy2GvuLZP0/0zUjMF3u4qe8stnoS7GHvoN5oCSuT8yjwGFJPfb/3aru8b7htfGP74Cf94VmWNzXwdimkcD3PmlZFxH0rTlHGlzrPcH0w9yk8YbDJdSlxMBDTZ9ez+TJrTGKRbCn/BG2TBbce28mf+kFFyhsj/gQVz639A6bSwfGgQCHa4IOOn5YIl8xmJNzV5S1YHQf2MEuarWkzvcAik3Fuk3Nz8gW/Xpx2tiJeQAGS+ESPk95Q==; bm_sv=E96C287E40EC63914A75D2D77DC10253~hX56gQLuLI4vftBWp2H/FjD6NlmmWGBBvbpP0ILK9Da4boDG+GeLvUXpDEGEzykxaQUTyEkz1y6fE4RjdDIk00jd/afUNxynJCQwV3RJBeCpgviqHu2LgHTCFmsN3yh+2mvPVCDNNXwtCY0afPk4DCFkqKc8suhiXZf4zv4XHls=',
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

            cookieList = response.headers.getlist('Set-Cookie')
            print("\n\n\nCookie type: " + str(type(cookieList)))
            print("\n\n\nCookie Length: " + str(len(cookieList)))

            cookies = ";".join(cookieList)
            cookies = cookies.split(";")
            cookies = { cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies }
            self.headers_paginated['cookie'] = cookies

            print("\n\n\nCookie deets: -------------------------")
            print(cookies)

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