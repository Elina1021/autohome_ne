# -*- coding: utf-8 -*-
# @Author: solidjoker
# @Date:   2019-08-13 16:38:58
# @Last Modified by:   solidjoker
# @Last Modified time: 2019-08-13 16:58:11

import aiohttp
import asyncio
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(errors='ignore')


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        return html


def get_bsobj(url):
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_html(url.strip()))
    if result:
        bsobj = BeautifulSoup(result, 'lxml')
        return bsobj
