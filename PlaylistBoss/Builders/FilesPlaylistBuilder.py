from Builders import PlaylistBuilder
from Utils.Playlist import Playlist
import consts


class FilesPlaylistBuilder(PlaylistBuilder):
    def __init__(self):
        pass

    def build_playlist(self, json_playlist) -> Playlist:
        return self._json_to_playlist(json_playlist)

    @staticmethod
    def _json_to_playlist(json_playlist: dict) -> Playlist:
        if json_playlist[consts.JSON_FORMAT_PLAYLIST.OBJECT_TYPE] == consts.JSON_FORMAT_PLAYLIST.PLAYLIST_OBJECT:
            playlist = Playlist()
            playlist.set_songs_list(json_playlist[consts.JSON_FORMAT_PLAYLIST.SONGS_LIST])
            playlist.set_playlist_info(json_playlist[consts.JSON_FORMAT_PLAYLIST.PLAYLIST_INFO])
            return playlist
        raise Exception(__name__ + '_json_to_playlist: object type is not Playlist!')