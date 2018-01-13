# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, ICON_ERROR, web

def format_strings_from_quote(ticker, quote_data):
    usd_query = 'USDT_' + ticker.upper()
    last = "{:,.2f}".format(float(quote_data[usd_query]['last']))
    high = "{:,.2f}".format(float(quote_data[usd_query]['high24hr']))
    low = "{:,.2f}".format(float(quote_data[usd_query]['low24hr']))
    change = '%.2f' % float(quote_data[usd_query]['percentChange'])
    change = '+' + change if float(change) > 0 else change
    formatted = {}
    formatted['title'] = ticker.upper() + ': $' + last + ' (' + change + '%)'
    formatted['subtitle'] = '24hr High: $' + high + ' 24hr low $' + low
    return formatted

def main(wf):
    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    url = 'https://poloniex.com/public?command=returnTicker'
    r = web.get(url)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    result = r.json()
    if query:
        usd_query = 'USDT_' + query.upper()
        usd_link = 'https://poloniex.com/exchange#' + usd_query
        if usd_query in result:
            formatted = format_strings_from_quote(query, result)
            wf.add_item(title=formatted['title'],
                        subtitle=formatted['subtitle'],
                        arg=usd_link,
                        valid=True,
                        icon=ICON_WEB)
        else:
            wf.add_item(title='Couldn\'t find a quote for that symbol.',
                        subtitle='Please try again.',
                        icon=ICON_ERROR)
    else:
        formatted = format_strings_from_quote('BTC', result)
        wf.add_item(title=formatted['title'],
                    subtitle=formatted['subtitle'],
                    arg='https://poloniex.com/exchange#usdt_btc',
                    valid=True,
                    icon='icon/btc.png')

        formatted = format_strings_from_quote('ETH', result)
        wf.add_item(title=formatted['title'],
                    subtitle=formatted['subtitle'],
                    arg='https://poloniex.com/exchange#usdt_eth',
                    valid=True,
                    icon='icon/eth.png')

        formatted = format_strings_from_quote('LTC', result)
        wf.add_item(title=formatted['title'],
                    subtitle=formatted['subtitle'],
                    arg='https://poloniex.com/exchange#usdt_ltc',
                    valid=True,
                    icon='icon/ltc.png')

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
