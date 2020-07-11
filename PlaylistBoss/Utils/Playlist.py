import consts


class Playlist:
    _songs_list = []
    _playlist_info = None

    def add_song(self, song_id: str, name: str):
        self._songs_list.append({
            consts.PLAYLIST_OBJECT.SONG_ID: song_id,
            consts.PLAYLIST_OBJECT.SONG_NAME: name
        })

    def set_playlist_info(self, meta_data: dict):
        self._playlist_info = meta_data

    def get_songs_list(self) -> list:
        return self._songs_list

    def get_playlist_info(self):
        return self._playlist_info

    def set_songs_list(self, songs_list: list):
        self._songs_list = songs_list


