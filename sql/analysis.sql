--Show all tracks and columns
SELECT *
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`;


--Count the total number of tracks
SELECT
    COUNT(*) AS total_tracks
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`;


--Show the longest tracks in minutes
SELECT
    track_name,
    artist_name,
    ROUND(duration_ms / 60000, 2) AS duration_minutes
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`
ORDER BY duration_minutes DESC;


--Calculate the average track duration in minutes
SELECT
    ROUND(AVG(duration_ms) / 60000, 2) AS average_duration_minutes
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`;


--Show all unique albums
SELECT DISTINCT
    album_name
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`
ORDER BY album_name;


--Count the number of tracks per artist
SELECT
    artist_name,
    COUNT(*) AS total_tracks
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`
GROUP BY artist_name
ORDER BY total_tracks DESC, artist_name;


--Show tracks released most recently
SELECT
    track_name,
    artist_name,
    release_date
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`
ORDER BY release_date DESC;


--Show tracks longer than three minutes
SELECT
    track_name,
    artist_name,
    ROUND(duration_ms / 60000, 2) AS duration_minutes
FROM `spotify-gcp-data-pipeline.spotify_dataset.spotify_tracks`
WHERE duration_ms > 180000
ORDER BY duration_minutes DESC;