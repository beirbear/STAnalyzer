class Services(object):
    @staticmethod
    def is_file_exists(input):
        import os.path
        return os.path.isfile(input)