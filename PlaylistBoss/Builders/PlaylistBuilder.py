import abc
from Utils import BarePlaylist, Playlist


class PlaylistBuilder(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def build_playlist(bare_playlist: BarePlaylist) -> Playlist:
        pass
