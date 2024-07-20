# google-api-python-client

import googleapiclient.discovery


def get_songs_from_youtube_playlist(playlist_id, api_key):
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    songs = []

    try:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50  # You can adjust the number of results as needed
        )

        while request:
            response = request.execute()

            for item in response["items"]:
                snippet = item["snippet"]
                song = {
                    "title": snippet["title"],
                    "artist": snippet["videoOwnerChannelTitle"]
                }
                songs.append(song)

            request = youtube.playlistItems().list_next(request, response)

    except Exception as e:
        print(f"An error occurred: {e}")

    return songs


# Example usage of the function:
playlist_id = "YOUR_YOUTUBE_PLAYLIST_ID_HERE"
api_key = "YOUR_YOUTUBE_API_KEY_HERE"

songs = get_songs_from_youtube_playlist(playlist_id, api_key)

for song in songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")


""" THE SAME BUT FOR SPOTIFY



import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_songs_from_spotify_playlist(username, playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-read-private"))

    songs = []

    try:
        playlist = sp.user_playlist_tracks(username, playlist_id)
        
        for item in playlist['items']:
            track = item['track']
            song = {
                "title": track['name'],
                "artist": track['artists'][0]['name']
            }
            songs.append(song)

    except Exception as e:
        print(f"An error occurred: {e}")

    return songs

# Example usage of the function:
username = "YOUR_SPOTIFY_USERNAME"
playlist_id = "YOUR_SPOTIFY_PLAYLIST_ID"

songs = get_songs_from_spotify_playlist(username, playlist_id)

for song in songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")

"""
