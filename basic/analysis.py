import numpy as np
import datetime


class Analysis(object):

    @staticmethod
    def volume_surge(stock_data, consensus_data):
        # Group data according to stock name
        stock_name = []
        output = "<p><h2>Surged Volume</h2><table><tr><th>Stock Name</th><th>Price</th><th>Changed</th><th>Traded Volume</th><th>Surge</th></tr>"
        for item in stock_data:
            if item.stock_name not in stock_name and " XD" not in item.stock_name:
                stock_name.append(item.stock_name)

        # Get a list of historical data vy each stock_name
        tmpp = []
        for item in stock_name:
            history = []

            for eItem in stock_data:
                if eItem.stock_name == item and eItem.fetch_time.strftime("%Y-%m-%d") != datetime.datetime.now().strftime('%Y-%m-%d'):
                    history.append(eItem)
                if eItem.stock_name == item and eItem.fetch_time.strftime("%Y-%m-%d") == datetime.datetime.now().strftime('%Y-%m-%d'):
                    today = eItem

            # Convert io numpy list
            tmp = []
            for eachItem in history:
                tmp.append(eachItem.trade_volume)

            np_data = np.array(tmp)
            v_std = np_data.std()
            v_mean = np_data.mean()
            if today.trade_volume > v_mean + v_std + v_std:
                tmpp.append((today, today.get_html_surge_report(int(today.trade_volume / v_mean * 100)), int(today.trade_volume / v_mean * 100),))

        tmpp = sorted(tmpp, key=lambda p:p[2], reverse=True)

        for line in tmpp:
            output += line[1]

        output += "</table></p>"

        return output