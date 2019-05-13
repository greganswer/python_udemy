#! /usr/bin/env python3

import webbrowser
import sys
import pyperclip
import requests
import bs4
import logging
import subprocess
from selenium import webdriver


def open_address_in_browser():
    if len(sys.argv) > 1:
        # Get address from command line.
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' + address)


def view_text_from_site():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.status_code == requests.codes.ok
    len(res.text)
    print(res.text[:250])


def scrape_site():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    with open('RomeoAndJuliet.txt', 'wb') as playFile:
        for chunk in res.iter_content(100000):
            playFile.write(chunk)


def get_amazon_price(url):
    # Faking a User agent is required with sites like Amazon that try to prevent
    # bots from scraping their site.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#resultStats')
    logging.debug(elems)
    return elems[0].text.strip()


def navigate_website():
    chrome_driver = str(subprocess.check_output(['which', 'chromedriver']), 'utf-8').strip()
    logging.debug(chrome_driver)
    browser = webdriver.Chrome(executable_path=chrome_driver)

    url = "https://www.duckduckgo.com"
    browser.get(url)
    # browser = webdriver.Firefox()
    # browser.get('http://inventwithpython.com')


# price = get_amazon_price('https://www.google.com/search?q=kf%2Cv&oq=kf%2Cv&aqs=chrome..69i57j0l5.540j0j1&sourceid=chrome&ie=UTF-8')
# price = get_amazon_price('https://www.amazon.ca/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
# print('The price is %s', price)

# navigate_website()