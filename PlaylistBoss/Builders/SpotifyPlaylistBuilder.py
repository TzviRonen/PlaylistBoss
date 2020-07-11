from Builders import PlaylistBuilder
from Utils.Playlist import Playlist
from Utils.BarePlaylist import BarePlaylist
import consts


class SpotifyPlaylistBuilder(PlaylistBuilder):
    @staticmethod
    def build_playlist(bare_playlist: BarePlaylist) -> Playlist:
        if bare_playlist.get_type() is not consts.SPOTIFY_PLAYLIST_TYPE:
            raise Exception('SpotifyPlaylistBuilder: bare_playlist is not spotify!')

        data = bare_playlist.get_data()
        real_playlist = Playlist()
        for song in data:
            real_playlist.add_song(song['track']['uri'], song['track']['name'])
        real_playlist.set_playlist_info(bare_playlist.get_meta_data())
        return real_playlist

