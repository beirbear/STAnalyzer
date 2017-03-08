from basic.services import Services
from basic.definitions import Definitions as DF
from basic.sInfo import SInfo
from basic.cInfo import CInfo

class LocalDB(object):
    __stock = []
    __consensus = []
    __output = ""

    def __init__(self):
        # Read data from local database
        if not Services.is_file_exists(DF.get_stock_data_path()):
            raise FileNotFoundError("Stock data file doesn't exist!")

        if not Services.is_file_exists(DF.get_consensus_data_path()):
            raise FileNotFoundError("Consensus data file doesn't exist!")

        import datetime
        today = datetime.datetime.now()

        # Load data into the system
        with open(DF.get_stock_data_path()) as f:
            for line in f:
                item = SInfo(line)
                self.__stock.append(item)

                stock_in_focus = ['WORK', 'BANPU', 'EARTH', 'SAWAD']

                if item.fetch_time.day == today.day and \
                   item.fetch_time.month == today.month and \
                   item.fetch_time.year == today.year and \
                   item.stock_name in stock_in_focus:
                    self.__output += item.get_html_short_report()

        with open(DF.get_consensus_data_path()) as f:
            for line in f:
                item = CInfo(line)
                self.__consensus.append(item)

    def get_output(self):
        return self.__output

    def process(self, func):
        return func(self.__stock, self.__consensus)