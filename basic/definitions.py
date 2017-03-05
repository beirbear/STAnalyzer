class Definitions(object):

    @staticmethod
    def get_meta_environ_path():
        return "/home/beir/Desktop/STStream_DataSpace/meta/"

    @staticmethod
    def get_stock_data_path():
        return Definitions.get_meta_environ_path() + "stock.dat"

    @staticmethod
    def get_consensus_data_path():
        return Definitions.get_meta_environ_path() + "consensus.dat"
