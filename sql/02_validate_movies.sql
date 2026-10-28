-- 1. Check total number of movies
SELECT COUNT(*) AS total_movies
FROM movies;


-- 2. Check for duplicate movie IDs
SELECT tconst, COUNT(*) AS occurrences
FROM movies
GROUP BY tconst
HAVING COUNT(*) > 1;


-- 3. Check for invalid ratings
SELECT COUNT(*) AS invalid_ratings
FROM movies
WHERE averagerating < 1 OR averagerating > 10;


-- 4. Check vote count threshold
SELECT COUNT(*) AS movies_below_vote_threshold
FROM movies
WHERE numvotes < 100;


-- 5. Check for movies released before 2000
SELECT COUNT(*) AS movies_before_2000
FROM movies
WHERE startyear < 2000;


-- 6. Check missing runtimes
SELECT COUNT(*) AS missing_runtimes
FROM movies
WHERE runtimeminutes IS NULL;


-- 7. Check rating and vote statistics
SELECT
    MIN(averagerating) AS minimum_rating,
    MAX(averagerating) AS maximum_rating,
    MIN(numvotes) AS minimum_votes
FROM movies;