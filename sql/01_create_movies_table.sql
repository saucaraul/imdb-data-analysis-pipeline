CREATE TABLE movies (
    tconst VARCHAR(20) PRIMARY KEY,
    primaryTitle TEXT NOT NULL,
    startYear INTEGER,
    runtimeMinutes INTEGER,
    genres TEXT,
    averageRating NUMERIC(3,1) NOT NULL,
    numVotes INTEGER NOT NULL
);


SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_name = 'movies'
ORDER BY ordinal_position;
