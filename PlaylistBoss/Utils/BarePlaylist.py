import consts

class BarePlaylist:
    def __init__(self, p_type):
        self._set_type(p_type)
        self._meta_data = None
        self._data = None

    def _set_type(self, p_type):
        if p_type not in consts.PLAYLIST_TYPES:
            raise Exception('p_type {} not in PlaylistType'.format(p_type))
        self._type = p_type

    def get_type(self):
        return self._type

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_meta_data(self, p_meta_data):
        self._meta_data = p_meta_data

    def get_meta_data(self):
        return self._meta_data