from PlaylistInterfaces import PlaylistInterface
from Utils import Playlist
from Utils.BarePlaylist import BarePlaylist
from Builders.SpotifyPlaylistBuilder import SpotifyPlaylistBuilder
from PlaylistInterfaces.Clients.SpotifyClient import SpotifyClient
import consts
import json


class SpotifyPlaylistInterface(PlaylistInterface):
    def __init__(self, builder: SpotifyPlaylistBuilder, spotify_client: SpotifyClient):
        super(PlaylistInterface, self).__init__()
        self._builder = builder
        self._session = spotify_client.get_session()

    def get_playlist(self, playlist_props: dict) -> Playlist:
        bare_playlist = BarePlaylist(consts.SPOTIFY_PLAYLIST_TYPE)
        bare_playlist.set_data(self._get_full_playlist_from_server(playlist_props))
        bare_playlist.set_meta_data(playlist_props)
        return self._builder.build_playlist(bare_playlist)

    @staticmethod
    def _build_add_songs_to_playlist_post_requests(playlist: Playlist) -> list:
        songs_list = playlist.get_songs_list()
        data = []
        songs_chunk = {'uris': [], 'position': 0}
        for song, index in zip(songs_list, range(1, 999)):
            songs_chunk['uris'].append(song[consts.PLAYLIST_OBJECT.SONG_ID])
            if index % 100 == 0:
                data.append(songs_chunk)
                songs_chunk = {'uris': [], 'position': index}
        data.append(songs_chunk)
        return data

    def put_playlist(self, playlist, playlist_props: dict) -> None:
        self._session.headers.update({'Content-Type': 'application/json'})
        post_requests_data = self._build_add_songs_to_playlist_post_requests(playlist)
        for insert_songs_chunk in post_requests_data:
            response = self._session.post('https://api.spotify.com/v1/playlists/{playlist_id}/tracks'.format(
                playlist_id=playlist_props[consts.SPOTIFY_PLAYLIST_PROPS.PLAYLIST_ID]
            ), data=json.dumps(insert_songs_chunk))
            print(response)

    def _get_full_playlist_from_server(self, playlist_props: dict) -> list:
        items = []
        playlist_id = playlist_props[consts.SPOTIFY_PLAYLIST_PROPS.PLAYLIST_ID]

        result = self._session.get('https://api.spotify.com/v1/playlists/' + playlist_id +
                                   '/tracks?offset=0&limit=100&market=from_token&type=track')
        result_obj = json.loads(result.content)
        items += result_obj['items']

        while result_obj['next']:
            result = self._session.get(result_obj['next'])
            result_obj = json.loads(result.content)
            items += result_obj['items']

        return items

