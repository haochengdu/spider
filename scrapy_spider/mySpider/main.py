#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/9 9:08
@Author  : TX
@File    : main.py
@Software: PyCharm
"""
import os
import sys

from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'itcast'])
# execute(['scrapy', 'crawl', 'tencent'])
execute(['scrapy', 'crawl', 'sunhotline'])
