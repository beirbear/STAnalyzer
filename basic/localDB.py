from basic.services import Services
from basic.definitions import Definitions as DF

class LocalDB(object):
    __stock = None
    __consensus = None
    __output = None

    def __init__(self):
        # Read data from local database
        if not Services.is_file_exists(DF.get_stock_data_path()):
            raise FileNotFoundError("Stock data file doesn't exist!")

        if not Services.is_file_exists(DF.get_consensus_data_path()):
            raise FileNotFoundError("Consensus data file doesn't exist!")

        import datetime
        today = datetime.datetime.now()
        # today = datetime.datetime.fromtimestamp(1482233489)

        stock_in_focus = ['WORK', 'BANPU', 'EARTH', 'SAWAD']

        output = "<h2>STOCK INFO</h2>"

        # Load data into the system
        with open(DF.get_stock_data_path()) as f:
            for line in f:
                tmp = line.split('|')
                data_time = datetime.datetime.fromtimestamp(int(tmp[0][:-3]))

                if data_time.day == today.day and \
                   data_time.month == today.month and \
                   data_time.year == today.year and \
                   tmp[2] in stock_in_focus:
                    # print(line)
                    output += line + "<br>"

        output += "\n\n<h2>CONSENSUS INFO</h2>\n"
        with open(DF.get_consensus_data_path()) as f:
            current_date = today.strftime('%Y-%m-%d')
            for line in f:
                tmp = line.strip().split('|')
                # print(line)
                if tmp[-1] == current_date and \
                   tmp[2] in stock_in_focus:
                    # print(line)
                    output += line + "<br>"

        self.__output = output

    def get_output(self):
        return self.__output