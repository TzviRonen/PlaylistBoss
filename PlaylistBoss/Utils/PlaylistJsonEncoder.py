from Utils.Playlist import Playlist
import consts
import json


class PlaylistJsonEncoder(json.JSONEncoder):
    def default(self, o: Playlist) -> any:
        if isinstance(o, Playlist):
            return {
                consts.JSON_FORMAT_PLAYLIST.OBJECT_TYPE: consts.JSON_FORMAT_PLAYLIST.PLAYLIST_OBJECT,
                consts.JSON_FORMAT_PLAYLIST.PLAYLIST_INFO: o.get_playlist_info(),
                consts.JSON_FORMAT_PLAYLIST.SONGS_LIST: o.get_songs_list()
            }

        return json.JSONEncoder.default(self, o)



