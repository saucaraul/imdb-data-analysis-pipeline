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

final_movies = movies_100_votes[["tconst", "primaryTitle", "startYear", "runtimeMinutes",
 "genres", "averageRating", "numVotes"]]

final_movies.to_csv("data/processed/final_movies.csv", index =False)

check = pd.read_csv("data/processed/final_movies.csv")

print(check.shape)
print(check.columns.tolist())
# Checks done in order to clean the unnecessary data from the dataset
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
#print(movies_100_votes["runtimeMinutes"].isna().sum())
#print(movies_100_votes["runtimeMinutes"].notna().sum())
#print(basics[["startYear", "runtimeMinutes"]].dtypes)
#print(movies_100_votes["runtimeMinutes"].describe())
#print(movies_100_votes[movies_100_votes["runtimeMinutes"] > 1000][["tconst", "primaryTitle", "runtimeMinutes", "averageRating", "numVotes"]])
#print((movies_100_votes["runtimeMinutes"] >= 1000).sum())
#print((movies_100_votes["runtimeMinutes"] >= 180).sum())
#print(movies_100_votes["tconst"].duplicated().sum())
#print(((movies_100_votes["averageRating"] < 0) | (movies_100_votes["averageRating"]>10)).sum())
#print((movies_100_votes["numVotes"] < 0).sum())
#print(movies_100_votes.columns.tolist())
#print(final_movies.columns.tolist())
#print(final_movies.shape)
#print(final_movies.info())
#print(final_movies["startYear"].isna().sum())
#print(final_movies["numVotes"].isna().sum())