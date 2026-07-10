# Spotify GCP Data Pipeline

## Project Overview

This project demonstrates a simple end-to-end data engineering pipeline using Python, SQL, the Spotify Web API, and Google Cloud Platform.

The pipeline extracts Spotify track data, saves it as a CSV file, uploads it to Google Cloud Storage, loads it into BigQuery, and analyzes the data using SQL.

## Architecture

```
Spotify Web API
        │
        ▼
Python
        │
        ▼
CSV
        │
        ▼
Google Cloud Storage
        │
        ▼
BigQuery
        │
        ▼
SQL
```

## Technologies

- Python
- Spotipy
- Pandas
- Spotify Web API
- Google Cloud Storage
- BigQuery
- SQL

## Project Structure

```
spotify-gcp-data-pipeline/
│
├── data/
│   └── spotify_tracks.csv
│
├── sql/
│   └── analysis.sql
│
├── src/
│   └── extract_spotify.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Run the pipeline:

```bash
python src/extract_spotify.py
```

## SQL Analysis

The project includes SQL queries demonstrating:

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- COUNT
- AVG
- DISTINCT

The queries are available in:

```text
sql/analysis.sql
```
<img width="1818" height="637" alt="BigQuerySQL1" src="https://github.com/user-attachments/assets/eb3c282d-891c-4ebf-9f48-551f5be3878b" />

See other screenshots of queries made in BigQuery under docs/bigquery 
