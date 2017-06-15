# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, web


def main(wf):
    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    # url = 'http://jsonplaceholder.typicode.com/posts'
    url = 'https://poloniex.com/public?command=returnTicker'
    r = web.get(url)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    result = r.json()
    if query:
        usd_query = 'USDT_' + query.upper()
        usd_link = 'https://poloniex.com/exchange#' + usd_query
        if usd_query in result:
            wf.add_item(title=query.upper() + ': $' + result[usd_query]['last'],
                    subtitle=result[usd_query]['high24hr'],
                    arg=usd_link,
                    valid=True,
                    icon=ICON_WEB)
        else:
            wf.add_item(title='Couldn\'t find a quote for that symbol.',
                    subtitle='Please try again.',
                    icon=ICON_WEB)
    else:
        wf.add_item(title='BTC: $' + result['USDT_BTC']['last'],
                    subtitle=result['USDT_BTC']['high24hr'],
                    arg='https://poloniex.com/exchange#usdt_btc',
                    valid=True,
                    icon=ICON_WEB)

        wf.add_item(title='ETH: $' + result['USDT_ETH']['last'],
                    subtitle=result['USDT_ETH']['high24hr'],
                    arg='https://poloniex.com/exchange#usdt_eth',
                    valid=True,
                    icon=ICON_WEB)

        wf.add_item(title='LTC: $' + result['USDT_LTC']['last'],
                    subtitle=result['USDT_LTC']['high24hr'],
                    arg='https://poloniex.com/exchange#usdt_ltc',
                    valid=True,
                    icon=ICON_WEB)

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))