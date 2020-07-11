import requests
import json
import consts
import time
import hashlib

class SpotifyClient:
    def __init__(self):
        headers = {
            "accept": "application/json",
            "accept-language": "he",
            "app-platform": "WebPlayer",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "spotify-app-version": "1593827273",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/83.0.4103.116 Safari/537.36',
        }
        self._session = requests.session()
        self._session.headers.update(headers)
        self._cookie = self._get_cookie()
        self._session.headers.update({'cookie': self._cookie})
        self._token_data = None

    def get_session(self):
        """
            get the headers for the playlist request.
        """
        self._token_data = self._get_token()
        self._session.headers.update({'authorization': 'Bearer ' + self._token_data['accessToken']})
        return self._session

    def _get_token(self):
        """
        cookie must be set first!
        :return: dist
        """
        token = self.get_token_from_caching()
        if token is None:
            token = self._get_token_from_server()
            self._save_token_to_caching(token)
        return token

    def _get_token_from_server(self) -> dict:
        """
        cookie must be set first!
        :return: dist
        """
        result = self._session.get("https://open.spotify.com/get_access_token?reason=transport&productType=web_player")
        return json.loads(result.content)

    @staticmethod
    def _get_cookie() -> str:
        cookie = input('enter cookie:')
        return cookie

    @staticmethod
    def _save_token_to_caching(token):
        with open(consts.SPOTIFY_TOKEN_CACHING_FILE, 'w') as f:
            f.write(json.dumps(token))

    def get_token_from_caching(self):
        """
            if file not found or token expired return None.
        :return:
        """
        try:
            with open(hashlib.md5(self._cookie.encode('utf-8')).digest().hex() + '.json', 'r') as f:
                token = json.loads(f.read())
            if token['accessTokenExpirationTimestampMs'] < time.time()*1000:
                return None
            return token
        except Exception as err:  # no such file
            return None
