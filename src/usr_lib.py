# playwright
from playwright.async_api import Playwright, Page, async_playwright
from playwright.sync_api import sync_playwright

# fake-useragent
from fake_useragent import UserAgent

# data structures
import numpy as np
import pandas as pd

# database
import sqlite3

# asychronous
import asyncio

# others
import os, re, sys

# target url
HOMEPAGE = "https://batdongsan.com.vn/"

# user-defined classes, functions
from scrapers import scrape_pages_hrefs
