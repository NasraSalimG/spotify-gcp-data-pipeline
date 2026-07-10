import os
from pathlib import Path

import pandas
import spotipy
from dotenv import load_dotenv
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials


#Get the root folder of the project
project_folder = Path(__file__).resolve().parent.parent

#Define the project file paths
environment_file = project_folder / ".env"
output_file = project_folder / "data" / "spotify_tracks.csv"


#Read the Spotify credentials from the .env file
def read_spotify_credentials() -> tuple[str, str]:
    load_dotenv(environment_file)

    spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
    spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    #Validate that both credentials are available
    if not spotify_client_id or not spotify_client_secret:
        raise ValueError(
            "Spotify credentials are missing. "
            "Check SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in the .env file."
        )

    return spotify_client_id, spotify_client_secret


#Create an authenticated Spotify API connection
def create_spotify_api() -> spotipy.Spotify:
    spotify_client_id, spotify_client_secret = read_spotify_credentials()

    #Create the authentication object required by the Spotify API
    spotify_authentication = SpotifyClientCredentials(
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
    )

    return spotipy.Spotify(
        auth_manager=spotify_authentication,
    )


#Request tracks from the Spotify catalogue
def search_spotify_tracks(
    spotify_api: spotipy.Spotify,
) -> list[dict[str, object]]:
    try:
        spotify_search_results = spotify_api.search(
            q="year:2025",
            type="track",
            limit=10,
        )
    except SpotifyException as error:
        raise RuntimeError(
            f"Spotify API request failed: {error}"
        ) from error

    #Store the extracted track records
    spotify_tracks: list[dict[str, object]] = []

    #Extract the required fields from each track
    for track in spotify_search_results["tracks"]["items"]:
        spotify_tracks.append(
            {
                "track_id": track["id"],
                "track_name": track["name"],
                "artist_name": track["artists"][0]["name"],
                "album_name": track["album"]["name"],
                "duration_ms": track["duration_ms"],
                "release_date": track["album"]["release_date"],
            }
        )

    return spotify_tracks


#Save the extracted data as a CSV file
def save_tracks_as_csv(
    spotify_tracks: list[dict[str, object]],
) -> None:
    spotify_data = pandas.DataFrame(spotify_tracks)

    spotify_data.to_csv(
        output_file,
        index=False,
    )

    print(f"Spotify data saved to {output_file}")


#Run the Spotify data pipeline
spotify_api = create_spotify_api()
spotify_tracks = search_spotify_tracks(spotify_api)
save_tracks_as_csv(spotify_tracks)