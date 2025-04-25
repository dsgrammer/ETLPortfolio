import json
import logging.handlers
import pandas as pd
import os
import logging
from src.get_bronze_data import api_request
from datetime import datetime
logger = logging.getLogger(__name__)

config_path = "config/config.json"

# load configs
with open(config_path, 'r') as f:
    config = json.load(f)

# Config logger
rfh = logging.handlers.RotatingFileHandler(
    filename=config["logging"]["file_path"],
    maxBytes=config["logging"]["maxBytes"],
    backupCount=config["logging"]["backupCount"]
    )

logging.basicConfig(
    level=config["logging"]["level"],
    format="%(asctime)s %(name)-5s %(levelname)-5s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[rfh]
    )

# load spotify credentials
os.environ["SPOTIPY_CLIENT_ID"] = config["api_credentials"]["spotipy_client_id"]
os.environ["SPOTIPY_CLIENT_SECRET"] = config["api_credentials"]["spotipy_client_secret"]
os.environ["SPOTIPY_REDIRECT_URI"] = config["api_credentials"]["spotipy_redirect_uri"]

# get data
def main():
    logger.info(f"Getting api credentials.")
    user = api_request.connection()

    # Get all user saved (favorite) tracks
    logger.info(f"Getting user saved tracks.")
    fav_df = api_request.get_all_saved_tracks(user)
    fav_df['added_at'] = fav_df['added_at'].apply(pd.to_datetime)
    fav_df['release_date'] = fav_df['release_date'].str[:4]
    fav_df.to_csv(r'data/test1.csv', encoding='utf-8-sig')

    # get user's recently played tracks
    logger.info(f"Getting user's recently played tracks.")
    rpl_df = pd.DataFrame(columns=["track_id", "track_name", "duration_ms", "explicit", "played_at"])
    rpl_df = api_request.get_recently_played(rpl_df, user)
    rpl_df.to_csv(r'data/test2.csv', encoding='utf-8-sig')


if __name__ == "__main__":
    main()