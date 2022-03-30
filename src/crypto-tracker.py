#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# giovanni from Rahul Sethuram
# Clear ☀️   🌡️+32°F (feels +24°F, 37%) 🌬️↓12mph 🌑 Wed Mar 30 05:07:37 2022


import sys
import requests
import json


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


def format_strings_from_quote(ticker, quote_data):
    data = quote_data['RAW'][ticker.upper()]['USD']
    price = '{:,.2f}'.format(data['PRICE'])
    high = '{:,.2f}'.format(data['HIGH24HOUR'])
    low = '{:,.2f}'.format(data['LOW24HOUR'])
    change = '{:,.2f}'.format(data['CHANGEPCT24HOUR'])
    formatted = {}
    formatted['title'] = '{}: ${} ({}%)'.format(ticker.upper(), price, change)
    formatted['subtitle'] = '24hr high: ${} | 24hr low: ${}'.format(high, low)
    return formatted


def main():
    
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = None

    result = {"items": []}

            
    if query:
        url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + \
            query.upper() + '&tsyms=USD'
        
        resp = requests.get(url)
        myData = resp.json()
        
                      
        try:
            formatted = format_strings_from_quote(query, myData)
            
            result["items"].append({
            "title": formatted['title'],
            'subtitle': formatted['subtitle'],
            'valid': True,
            
            "icon": {
                "path": 'icon/BookmarkIcon.icns'
            },
            'arg': 'https://www.cryptocompare.com/coins/' + query + '/overview/USD'
                }) 

        
        except:
            result["items"].append({
            "title": 'Couldn\'t find a quote for that symbol 😞',
            'subtitle': 'Please try again.',
            
            
            "icon": {
                "path": 'icon/AlertStopIcon.icns'
            },
                }) 
        
    else:
        url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,LTC,BCH&tsyms=USD'
        resp = requests.get(url)
        myData = resp.json()
        
        
        formatted = format_strings_from_quote('BTC', myData)
        result["items"].append({
            "title": formatted['title'],
            'subtitle': formatted['subtitle'],
            'valid': True,
            
            "icon": {
                "path": 'icon/btc.png'
            },
            'arg': 'https://www.cryptocompare.com/'
                }) 
        
        

        formatted = format_strings_from_quote('ETH', myData)

        result["items"].append({
        "title": formatted['title'],
        'subtitle': formatted['subtitle'],
        'valid': True,
        
        "icon": {
            "path": 'icon/eth.png'
        },
        'arg': 'https://www.cryptocompare.com/'
            }) 

        
        formatted = format_strings_from_quote('LTC', myData)
        result["items"].append({
        "title": formatted['title'],
        'subtitle': formatted['subtitle'],
        'valid': True,
        
        "icon": {
            "path": 'icon/ltc.png'
        },
        'arg': 'https://www.cryptocompare.com/'
            }) 
        
        formatted = format_strings_from_quote('BCH', myData)
        result["items"].append({
            "title": formatted['title'],
            'subtitle': formatted['subtitle'],
            'valid': True,
            
            "icon": {
                "path": 'icon/bch.png'
            },
            'arg': 'https://www.cryptocompare.com/'
                }) 

    
    print (json.dumps(result))


if __name__ == u"__main__":
   main()
