import pandas as pd
from pathlib import Path
from load_data import basics, ratings

basics["startYear"] = pd.to_numeric(
    basics["startYear"],
    errors="coerce"
)
basics["runtimeMinutes"] = pd.to_numeric(
    basics["runtimeMinutes"],
    errors="coerce"
)

movies_2000 = basics[
    (basics["titleType"] == "movie") &
    (basics["isAdult"] == 0) &
    (basics["startYear"] >= 2000)
]

movies_with_ratings = pd.merge(
    movies_2000,
    ratings,
    on="tconst",
    how="left"
)

rated_movies = movies_with_ratings[~movies_with_ratings["averageRating"].isna()]
movies_100_votes = rated_movies[rated_movies["numVotes"] >= 100]

final_movies = movies_100_votes[["tconst", "primaryTitle", "startYear", "runtimeMinutes",
 "genres", "averageRating", "numVotes"]]

output_path = Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)

final_movies.to_csv(output_path / "final_movies.csv", index=False)

check = pd.read_csv(output_path / "final_movies.csv")

print(check.shape)
print(check.columns.tolist())