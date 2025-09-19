import React, { useEffect, useState } from "react";

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/trending")
      .then((res) => res.json())
      .then((data) => setMovies(data.movies))
      .catch((err) => console.error("Error fetching movies:", err));
  }, []);

  return (
    <div style={{ display: "flex", flexWrap: "wrap" }}>
      {movies.map((movie) => (
        <div key={movie.id} style={{ margin: 10, width: 200 }}>
          {movie.poster_path && (
            <img
              src={movie.poster_path}
              alt={movie.title}
              style={{ width: "100%", borderRadius: "8px" }}
            />
          )}
          <h4>{movie.title}</h4>
          <p>{movie.overview ? movie.overview.substring(0, 100) + "..." : ""}</p>
        </div>
      ))}
    </div>
  );
};

export default MovieList;
