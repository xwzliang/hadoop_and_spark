CREATE VIEW topMoviesIDs AS
SELECT movieID, count(movieID) AS ratingCount
FROM ratings
GROUP BY movieID
ORDER BY ratingCount DESC;

SELECT n.title, ratingCount
FROM topMoviesIDs t JOIN names n ON t.movieID = n.movieID;