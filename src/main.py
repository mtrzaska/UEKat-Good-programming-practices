from pydantic import BaseModel
from typing import Union, List
from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Movie(BaseModel):
    movieId: int
    title: str
    genres: str
def load_movies(file_path: str):
    movies = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = Movie(
                movieId=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"]
            )
            movies.append(movie)
    return movies

class Links(BaseModel):
    movieId: int
    imdbId: str
    tmdbId: str
def load_links(file_path: str):
    links = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            link = Links(
                movieId=int(row["movieId"]),
                imdbId=row["imdbId"],
                tmdbId=row["tmdbId"]
            )
            links.append(link)
    return links


class Ratings(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: str
def load_ratings(file_path: str):
    ratings = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rating = Ratings(
                userId=int(row["userId"]),
                movieId=row["movieId"],
                rating=row["rating"],
                timestamp=row["timestamp"]
            )
            ratings.append(rating)
    return ratings

class Tags(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: str
def load_tags(file_path: str):
    tags = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tag = Tags(
                userId=int(row["userId"]),
                movieId=row["movieId"],
                tag=row["tag"],
                timestamp=row["timestamp"]
            )
            tags.append(tag)
    return tags

@app.get("/movies", response_model=List[Movie])
async def get_movies():
    file_path = "../databases/movies.csv"
    movies = load_movies(file_path)
    return movies

@app.get("/links", response_model=List[Links])
async def get_links():
    file_path = "../databases/links.csv"
    links = load_links(file_path)
    return links

@app.get("/ratings", response_model=List[Ratings])
async def get_ratings():
    file_path = "../databases/ratings.csv"
    ratings = load_ratings(file_path)
    return ratings

@app.get("/tags", response_model=List[Tags])
async def get_tags():
    file_path = "../databases/tags.csv"
    tags = load_tags(file_path)
    return tags


