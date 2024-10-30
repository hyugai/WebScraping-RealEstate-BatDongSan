# libs
from libs import *

# URLScrapper
class URLScrapper():
    def __init__(self, 
                 headers: dict[str, str]) -> None:
        self.headers = headers 

    def sellingTypesURLs_collector(self):
        self.headers['User-Agent'] = UserAgent().random
        with requests.Session() as s:
            r = s.get(HOMEPAGE, headers=self.headers) 
            
            if r.status_code == 200:
                print('OK')
            else:
                raise ValueError(f'Failed fetching (error code: {r.status_code})')