#!/usr/bin/python
# -*- coding: utf8 -*-

import requests
from bs4 import BeautifulSoup
import subprocess
import os

devnull = open(os.devnull, "wb")

kernel = subprocess.check_output(["uname", "-r"]
                                 ).decode("utf-8").replace("\n", "")[:-5]

try:
    html = requests.get("https://kernel.org").text
except requests.exceptions.ConnectionError:
    print(kernel)
else:
    html = BeautifulSoup(html, "lxml")
    print(kernel, html.find_all("strong")[2].get_text(), sep="/")
