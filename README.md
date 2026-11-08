# TMDB CLI Tool

Preko komandne linije  prikazuje filmove sa The Movie Database (TMDB) API-ja.

Projekat sa roadmap.sh: https://roadmap.sh/projects/tmdb-cli

## Podešavanje tokena

Napraviti nalog na themoviedb.org, idi na Settings → API i kopiraj
"API Read Access Token". Zatim ga sačuvaj kao promenljivu okruženja:

## Upotreba

```
tmdb-app --type playing    # trenutno u bioskopima
tmdb-app --type popular    # popularni filmovi
tmdb-app --type top        # najbolje ocenjeni
tmdb-app --type upcoming   # uskoro u bioskopima
```
