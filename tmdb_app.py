import argparse
import os
import sys
import requests

BASE_URL = "https://api.themoviedb.org/3/movie"
ENDPOINTS = {
    "playing": "now_playing",
    "popular": "popular",
    "top": "top_rated",
    "upcoming": "upcoming",
}

def fetch_movies(movie_type, token):
    url = f"{BASE_URL}/{ENDPOINTS[movie_type]}"
    headers = {"Authorization": f"Bearer {token}", "accept": "application/json"}
    response = requests.get(url, headers=headers,
                            params={"language": "en-US", "page": 1}, timeout=10)
    response.raise_for_status()
    return response.json().get("results", [])

def print_movies(movies):
    if not movies:
        print("Nema rezultata.")
        return
    for i, m in enumerate(movies, 1):
        title = m.get("title", "N/A")
        date = m.get("release_date") or "nepoznat datum"
        rating = m.get("vote_average", 0)
        print(f"{i:>2}. {title} ({date}) - ocena {rating:.1f}")

def main():
    parser = argparse.ArgumentParser(description="Prikaz filmova sa TMDB-a")
    parser.add_argument("--type", required=True, choices=ENDPOINTS.keys(),
                        help="playing | popular | top | upcoming")
    args = parser.parse_args()

    token = os.getenv("TMDB_TOKEN")
    if not token:
        sys.exit("Greska: nije podesen TMDB_TOKEN.")

    try:
        movies = fetch_movies(args.type, token)
    except requests.exceptions.ConnectionError:
        sys.exit("Greska: nema konekcije sa internetom.")
    except requests.exceptions.Timeout:
        sys.exit("Greska: server nije odgovorio na vreme.")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            sys.exit("Greska: neispravan token.")
        sys.exit(f"Greska: API je vratio status {e.response.status_code}.")

    print_movies(movies)

if __name__ == "__main__":
    main()