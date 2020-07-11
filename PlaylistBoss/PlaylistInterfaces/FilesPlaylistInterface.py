from PlaylistInterfaces import PlaylistInterface
from Builders import FilesPlaylistBuilder
from Utils.Playlist import Playlist
from Utils.PlaylistJsonEncoder import PlaylistJsonEncoder
import consts
import json


class FilesPlaylistInterface(PlaylistInterface):
    def __init__(self, builder: FilesPlaylistBuilder):
        super(PlaylistInterface, self).__init__()
        self._builder = builder

    def get_playlist(self, playlist_props: dict) -> Playlist:
        if consts.FILE_PLAYLIST_PROPS.FILE_NAME not in playlist_props:
            raise Exception('FilesPlaylistInterface_get_playlist: no file name in playlist_props')

        with open(playlist_props[consts.FILE_PLAYLIST_PROPS.FILE_NAME], 'r') as f:
            playlist = self._builder.build_playlist(json.loads(f.read()))
        return playlist

    def put_playlist(self, playlist: Playlist, playlist_props: dict) -> None:
        if consts.FILE_PLAYLIST_PROPS.FILE_NAME not in playlist_props:
            raise Exception('FilesPlaylistInterface_put_playlist: no file name in playlist_props')

        with open(playlist_props[consts.FILE_PLAYLIST_PROPS.FILE_NAME], 'w') as f:
            f.write(json.dumps(playlist, cls=PlaylistJsonEncoder))
