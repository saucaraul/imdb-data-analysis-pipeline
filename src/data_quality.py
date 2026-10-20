import pandas as pd

def check_duplicate_ids(df, column):
    duplicates = df[column].duplicated().sum()
    return "PASS" if duplicates == 0 else "FAIL"


def check_missing_values(df, column):
    missing_values = df[column].isna().sum()
    return "PASS" if missing_values == 0 else "FAIL"

def check_rating_range(df, column):
    out_of_range = df[(df[column] < 1) | (df[column] > 10)]
    return "PASS" if len(out_of_range) == 0 else "FAIL"

def check_vote_count(df, column, threshold=100):
    below_threshold = df[df[column] < threshold]
    return "PASS" if len(below_threshold) == 0 else "FAIL"

def check_start_year(df, column, year=2000):
    before_year = df[df[column] < year]
    return "PASS" if len(before_year) == 0 else "FAIL"

def check_runtime(df, column):
    invalid_runtime = df[df[column] <= 0]
    return "PASS" if len(invalid_runtime) == 0 else "FAIL"


movies_df = pd.read_csv("data/processed/final_movies.csv")

print("Duplicate IDs Check:", check_duplicate_ids(movies_df, "tconst"))
print("Missing Values Check:", check_missing_values(movies_df, "averageRating"))
print("Rating Range Check:", check_rating_range(movies_df, "averageRating"))
print("Vote Count Check:", check_vote_count(movies_df, "numVotes", threshold=100))
print("Start Year Check:", check_start_year(movies_df, "startYear", year=2000))
print("Runtime Check:", check_runtime(movies_df, "runtimeMinutes"))

