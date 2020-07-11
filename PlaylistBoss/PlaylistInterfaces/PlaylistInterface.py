import abc
from Builders import PlaylistBuilder
from Utils import Playlist


class PlaylistInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self,  builder: PlaylistBuilder):
        pass

    @abc.abstractmethod
    def get_playlist(self, playlist_props: dict) -> Playlist:
        pass

    @abc.abstractmethod
    def put_playlist(self, playlist: Playlist, playlist_props: dict) -> None:
        pass

