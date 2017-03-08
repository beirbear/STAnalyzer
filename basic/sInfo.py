import datetime
import locale

class SInfo(object):
    fetch_time = None
    stock_name = None
    price_recent = None
    price_changed = None
    price_changeR = None
    price_closedPrev = None
    price_openDay = None
    price_topDay = None
    price_bottomDay = None
    price_avgDay = None
    trade_volume = None
    trade_value = None
    par_value = None
    price_ceiling = None
    price_floor = None
    bi_volume = None
    bid_price = None
    offer_price = None
    offer_volume = None

    def __init__(self, data_str):
        tmp = data_str.split('|')
        self.fetch_time = datetime.datetime.fromtimestamp(int(tmp[0][:-3]))
        self.stock_name = tmp[2]
        self.price_recent = tmp[3]
        self.price_changed = tmp[4]
        self.price_changeR = tmp[5]
        self.price_closedPrev = tmp[6]
        self.price_openDay = tmp[7]
        self.price_topDay = tmp[8]
        self.price_bottomDay = tmp[9]
        self.price_avgDay = tmp[10]
        self.trade_volume = int(tmp[11])
        self.trade_value = int(tmp[12])
        self.par_value = tmp[13]
        self.price_ceiling = tmp[14]
        self.price_floor = tmp[15]
        self.bi_volume = tmp[16]
        self.bid_price = tmp[17]
        self.offer_price = tmp[18]
        self.offer_volume = tmp[19]
        locale.setlocale(locale.LC_ALL, '')

    def __str__(self):
        return self.stock_name + ":" + str(self.fetch_time) + ": " + str(self.trade_volume)

    def get_html_short_report(self):
        return "<p><strong>{0}</strong><br>Price: {1} ({2})<br>Traded: {3}  ({4})</p>".format(self.stock_name, self.price_recent, self.price_changed, locale.format("%d", self.trade_volume, grouping=True), locale.format("%d", self.trade_value, grouping=True))

    def get_html_surge_report(self, surged_value):
        return "<p><strong>{0}</strong><br>Price: {1} ({2})<br>Traded Volume: {3}  ({4}%)</p>".format(self.stock_name, self.price_recent, self.price_changed, locale.format("%d", self.trade_volume, grouping=True), locale.format("%d", surged_value, grouping=True))

