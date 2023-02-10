#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import html5lib
from datetime import datetime

""" 

Scraper to find and record prices, generalizable through config

"""
class Scraper:

    # class variables
    json_schema = ["buy_sites", "brands", "product_names", "sell_sites"]

    ## Basic input sanitization
    def enforce_schema(config_dict):
        for s in json_schema:
            if s not in config_dict or type(config_dict[s]) != type([]):
                raise ValueError("Schema Error")
            for e in config_dict[s]:
                if type(e) != type(""):
                    raise ValueError("Schema Error")


    ## Create run-time exception if config is invalid format, does not instantiate Scraper
    def __init__(self, config_json):
        self.config_dict = json.loads(config_json)
        try: 
            enforce_schema(config_dict)
        except ValueError:
            raise Exception('Configuration not interpeted correctly, check for schema match or other error')


    ## Entry point into getting class to work, using instance variable config_dict
    def run():
        buy_prices = scrape_page_for_price(config_dict["buy_sites"])
        sell_prices = scrape_page_for_price(config_dict["sell_sites"])
        send_to_SNS(buy_prices, 'BUY')
        send_to_SNS(sell_prices, 'SELL')


    ### 
    def scrape_page_for_price(URLS):
        price = None
        for u in URLS:
            r = requests.get(u)
            print(r.content)
        return price

    def send_to_SNS(data, metadata):


scraper = Scraper() # get config file 


