import json
import pandas as pd
import os
from src.get_bronze_data import api_request


config_path = "config/config.json"

with open(config_path, 'r') as f:
    config = json.load(f)

os.environ["SPOTIPY_CLIENT_ID"] = config["api_credentials"]["spotipy_client_id"]
os.environ["SPOTIPY_CLIENT_SECRET"] = config["api_credentials"]["spotipy_client_secret"]
os.environ["SPOTIPY_REDIRECT_URI"] = config["api_credentials"]["spotipy_redirect_uri"]

def main():
    user = api_request.connection()

    # Get all user saved (favorite) tracks
    fav_df = api_request.get_all_saved_tracks(user)
    fav_df['added_at'] = fav_df['added_at'].apply(pd.to_datetime)
    fav_df['release_date'] = fav_df['release_date'].str[:4]
    fav_df.to_csv(r'data/test1.csv', encoding='utf-8-sig')
    print(fav_df.head())
    print(fav_df.dtypes)

    rpl_df = pd.DataFrame(columns=["track_id", "track_name", "duration_ms", "explicit", "played_at"])
    rpl_df = api_request.get_recently_played(rpl_df, user)
    rpl_df.to_csv(r'data/test2.csv', encoding='utf-8-sig')


if __name__ == "__main__":
    main()