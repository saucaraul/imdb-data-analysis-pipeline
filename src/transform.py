import pandas as pd
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
#print(movies_with_ratings.shape)
#print(movies_with_ratings["averageRating"].isna().sum())
#print(movies_with_ratings["numVotes"].isna().sum())
#print(rated_movies.shape)
#print(movies_100_votes.shape)
#print(movies_100_votes["numVotes"].min())
#print(movies_100_votes["averageRating"].min())
#print(movies_100_votes["averageRating"].max())
#print(movies_100_votes.head())
#print(movies_100_votes.dtypes)
print(basics[["startYear", "runtimeMinutes"]].dtypes)