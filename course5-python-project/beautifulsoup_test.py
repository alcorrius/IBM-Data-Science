#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:47:33 2024

@author: vdotsenko
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/Data_science").text

soup = BeautifulSoup(page, "html.parser")

sections = soup.find_all("h3")

for section in sections:
    print(section)