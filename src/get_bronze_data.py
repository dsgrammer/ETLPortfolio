import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class api_request:
    def connection():
        # Set token and login credentials
        # URL to all scopes available
        # https://developer.spotify.com/documentation/web-api/concepts/scopes
        scope = ['user-library-read', 'user-read-recently-played']
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        user = sp

        return user

    # Function for getting all the user's saved (favorite) tracks
    def get_all_saved_tracks(user, limit_step=50):

        song_list = []

        for offset in range(0, 2000, limit_step):
            r = user.current_user_saved_tracks(
                limit=limit_step,
                offset=offset,
            )
            for idx, item in enumerate(r['items']):
                d = item['track']
                track_info = dict(band_id = d['artists'][0]['id'],
                                band_name = d['artists'][0]['name'],
                                album_name = d['album']['name'],
                                release_date = d['album']['release_date'],
                                total_tracks = d['album']['total_tracks'],
                                album_id = d['album']['id'],
                                track_id = d['id'],
                                track_name = d['name'],
                                duration_ms = d['duration_ms'],
                                explicit = d['explicit'],
                                added_at = item['added_at']
                                )   

                song_list.append(track_info)

            if offset > int(r['total']):
                break

        return pd.DataFrame(song_list)