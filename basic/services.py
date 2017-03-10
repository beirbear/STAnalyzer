class Services(object):
    @staticmethod
    def is_file_exists(input):
        import os.path
        return os.path.isfile(input)

    @staticmethod
    def disk_usage(path='/'):
        import os
        from collections import namedtuple

        _ntuple_diskusage = namedtuple('usage', 'total used free')

        """Return disk usage statistics about the given path.

        Returned valus is a named tuple with attributes 'total', 'used' and
        'free', which are the amount of total, used and free space, in bytes.
        """
        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize / 1024 / 1024 / 1024
        total = st.f_blocks * st.f_frsize / 1024 / 1024 / 1024
        used = (st.f_blocks - st.f_bfree) * st.f_frsize / 1024 / 1024 / 1024
        return _ntuple_diskusage(total, used, free)

    @staticmethod
    def get_available_resource():
        total, used, free = Services.disk_usage()
        return '<h3>Disk Resource: {0} GB <em>({1}/{2} GB)</em></h3>'.format( int(free), int(used), int(total))
