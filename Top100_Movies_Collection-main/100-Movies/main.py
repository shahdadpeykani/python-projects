import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

with open("Top100-movies.txt", mode="a", encoding="utf-8") as file:
    new_movie_list = []

    for movie in all_movies:
        new_movie_list.append(movie.getText(strip=True))

    new_movie_list.reverse()
    for movie in new_movie_list:
        file.write(f"{movie}\n")
