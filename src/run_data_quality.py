import pandas as pd

from data_quality import check_missing_values, check_duplicate_ids, check_rating_range, check_vote_count, check_start_year, check_runtime

file_path = "data/processed/final_movies.csv"
movies_df = pd.read_csv(file_path)

columns_to_check = [
    "primaryTitle",
    "tconst",
    "startYear",
    "runtimeMinutes",
    "averageRating",
    "numVotes"
]

results = {}

status, duplicate_count = check_duplicate_ids(movies_df, "tconst")
results["duplicate_ids"] = {
    "status": status,
    "affected_rows": duplicate_count
}


for column in columns_to_check:
    status, missing_count = check_missing_values(movies_df, column)

    results[column] = {
        "status": status,
        "affected_rows": missing_count
    }


status, invalid_count = check_rating_range(movies_df, "averageRating")
results["rating_range"] = {
    "status": status,
    "affected_rows": invalid_count
}


status, below_threshold_count = check_vote_count(movies_df, "numVotes", threshold=100)
results["vote_count"] = {
    "status": status,
    "affected_rows": below_threshold_count
}


status, before_year_count = check_start_year(movies_df, "startYear", year=2000)
results["start_year"] = {
    "status": status,
    "affected_rows": before_year_count
}


status, invalid_runtime_count = check_runtime(movies_df, "runtimeMinutes")
results["runtime"] = {
    "status": status,
    "affected_rows": invalid_runtime_count
}


print("\n=== IMDb DATA QUALITY REPORT ===\n")

for check_name, details in results.items():
    status = details["status"]
    affected_rows = details["affected_rows"]

    if check_name == "duplicate_ids":
        description = "duplicate IDs"
    elif check_name in columns_to_check:
        description = "missing values"
    elif check_name == "rating_range":
        description = "invalid ratings"
    elif check_name == "vote_count":
        description = "movies below the minimum vote count"
    elif check_name == "start_year":
        description = "movies before the minimum start year"
    elif check_name == "runtime":
        description = "movies with invalid runtimes"
    else:
        description = "rows affected"

    print(
        f"{check_name}: {status} — "
        f"{affected_rows} {description}"
    )
