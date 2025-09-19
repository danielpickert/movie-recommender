from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
# Load variables from backend/.env
load_dotenv()
import requests
import os

app = FastAPI()

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TMDB_API_KEY = os.getenv("TMDB_API_KEY")  # Set this in your environment

TMDB_BASE_URL = "https://api.themoviedb.org/3"

@app.get("/trending")
def get_trending_movies():
    url = f"{TMDB_BASE_URL}/trending/movie/week?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    # Return only relevant fields
    movies = [
        {
            "id": m["id"],
            "title": m["title"],
            "overview": m["overview"],
            "poster_path": f"https://image.tmdb.org/t/p/w500{m['poster_path']}" if m.get("poster_path") else None
        }
        for m in data.get("results", [])
    ]
    return {"movies": movies}
