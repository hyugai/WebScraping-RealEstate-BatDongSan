# requests
from bs4 import BeautifulSoup
import requests
from lxml import etree

# asynchronous 
import aiohttp
from aiohttp_socks.connector import ProxyConnector

# fake user-agent, proxies
from fake_useragent import UserAgent
from stem.control import Controller
from stem import Signal

# playwright 
from playwright.async_api import Playwright, Page, async_playwright
from playwright.sync_api import sync_playwright

# data structures
import numpy as np
import pandas as pd

# others
import re, sqlite3, asyncio

# batdongsan's configurations
HOMEPAGE = 'https://batdongsan.com.vn'

# usr libs
from scrappers import URLScrapper
from trackers import *