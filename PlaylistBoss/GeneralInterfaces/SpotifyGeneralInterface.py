from PlaylistInterfaces.Clients.SpotifyClient import SpotifyClient


class SpotifyGeneralInterface:
    def __init__(self, spotify_client: SpotifyClient):
        self._spotify_client = spotify_client

    def chose_playlists_id(self):
        # https://developer.spotify.com/documentation/web-api/reference/playlists/get-a-list-of-current-users-playlists/
        pass
