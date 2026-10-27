import pandas as pd


def check_duplicate_ids(df, column):
    duplicates = df[column].duplicated().sum()

    if duplicates == 0:
        result = "PASS"
    else:
        result = "FAIL"

    return result, duplicates


def check_missing_values(df, column):
    missing_values = df[column].isna().sum()

    if missing_values == 0:
        result = "PASS"
    elif column == "runtimeMinutes":
        result = "WARNING"
    else:
        result = "FAIL"
        
    return result, missing_values


def check_rating_range(df, column):
    out_of_range = df[(df[column] < 1) | (df[column] > 10)]
    invalid_count = len(out_of_range)

    if invalid_count == 0:
        result = "PASS"
    else:
        result = "FAIL"

    return result, invalid_count


def check_vote_count(df, column, threshold=100):
    below_threshold = df[df[column] < threshold]
    invalid_count = len(below_threshold)

    if invalid_count == 0:
        result = "PASS"
    else:
        result = "FAIL"

    return result, invalid_count



def check_start_year(df, column, year=2000):
    before_year = df[df[column] < year]
    invalid_count = len(before_year)
    
    if invalid_count == 0:
        result = "PASS"
    else:
        result = "FAIL"

    return result, invalid_count


def check_runtime(df, column):
    invalid_runtime = df[df[column] <= 0]
    invalid_count = len(invalid_runtime)

    if invalid_count == 0:
        result = "PASS"
    else:
        result = "FAIL"

    return result, invalid_count