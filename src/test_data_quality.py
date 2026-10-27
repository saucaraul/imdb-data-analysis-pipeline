
import pandas as pd

from data_quality import (
    check_duplicate_ids,
    check_missing_values,
    check_rating_range,
    check_vote_count,
    check_start_year,
    check_runtime,
)


def test_duplicate_ids():
    df = pd.DataFrame({
        "tconst": ["tt0000001", "tt0000001", "tt0000002"]
    })

    status, count = check_duplicate_ids(df, "tconst")

    assert status == "FAIL"
    assert count == 1


def test_missing_values():
    df = pd.DataFrame({
        "runtimeMinutes": [120, None, 90]
    })

    status, count = check_missing_values(df, "runtimeMinutes")

    assert status == "WARNING"
    assert count == 1


def test_rating_range():
    df = pd.DataFrame({
        "averageRating": [7.5, 8.0, 11.0]
    })

    status, count = check_rating_range(df, "averageRating")

    assert status == "FAIL"
    assert count == 1


def test_vote_count():
    df = pd.DataFrame({
        "numVotes": [50, 150, 200]
    })

    status, count = check_vote_count(df, "numVotes")

    assert status == "FAIL"
    assert count == 1


def test_start_year():
    df = pd.DataFrame({
        "startYear": [1999, 2000, 2020]
    })

    status, count = check_start_year(df, "startYear")

    assert status == "FAIL"
    assert count == 1


def test_runtime():
    df = pd.DataFrame({
        "runtimeMinutes": [0, 120, 90]
    })

    status, count = check_runtime(df, "runtimeMinutes")

    assert status == "FAIL"
    assert count == 1
