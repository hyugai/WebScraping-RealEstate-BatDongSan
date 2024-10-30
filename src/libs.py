# requests
from bs4 import BeautifulSoup
import requests
from lxml import etree

# aiohttp
import aiohttp

# data structures
import numpy as np
import pandas as pd

# others
import re, sqlite3, asyncio

# batdongsan's configurations
HEADERS = {'Accept': 'application/x-clarity-gzip', 
           'Accept-Encoding': 'gzip,deflate,br,zstd', 
           'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8,nl;q=0.7'}
HOMEPAGE = 'https://batdongsan.com.vn/'