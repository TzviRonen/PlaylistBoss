from Builders import FilesPlaylistBuilder, SpotifyPlaylistBuilder
from PlaylistInterfaces import FilesPlaylistInterface, SpotifyPlaylistInterface
from PlaylistInterfaces.Clients.SpotifyClient import SpotifyClient
import consts


def main():
    spotify_client = SpotifyClient()
    f = FilesPlaylistInterface(FilesPlaylistBuilder())
    s = SpotifyPlaylistInterface(SpotifyPlaylistBuilder(), spotify_client)
    src_playlist_id = ''
    dst_playlist_id = ''

    spotify_playlist = s.get_playlist({
        consts.SPOTIFY_PLAYLIST_PROPS.PLAYLIST_ID: src_playlist_id
    })

    f.put_playlist(spotify_playlist, {consts.FILE_PLAYLIST_PROPS.FILE_NAME: src_playlist_id+'.json'})
    playlist = f.get_playlist({consts.FILE_PLAYLIST_PROPS.FILE_NAME: src_playlist_id+'.json'})
    print(playlist.get_songs_list())
    print(playlist.get_playlist_info())
    print('{} songs.'.format(len(playlist.get_songs_list())))

    s.put_playlist(playlist, {
        consts.SPOTIFY_PLAYLIST_PROPS.PLAYLIST_ID: dst_playlist_id
    })


if __name__ == '__main__':
    main()
