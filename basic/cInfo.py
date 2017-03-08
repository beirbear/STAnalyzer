import datetime

class CInfo(object):
    last_update = None
    stock_name = None
    broker_name = None
    year_f = None
    change_p = None
    next_year_f = None
    next_change_p = None
    year_pe = None
    year_pvb = None
    year_div_p = None
    target_price = None
    rec = None
    group_date = None

    def __init__(self, data_str):
        tmp = data_str.split('|')
        self.last_update = datetime.datetime.fromtimestamp(int(tmp[0][:-3]))
        self.stock_name = tmp[2]
        self.broker_name = tmp[3]
        self.year_f = tmp[4]
        self.change_p = tmp[5]
        self.next_year_f = tmp[6]
        self.next_change_p = tmp[7]
        self.year_pe = tmp[8]
        self.year_pvb = tmp[9]
        self.year_div_p = tmp[10]
        self.target_price = tmp[11]
        self.rec = tmp[12]
        self.group_date = tmp[13]