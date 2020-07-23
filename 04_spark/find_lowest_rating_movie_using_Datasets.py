from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions


def loadMovieNames():
    movieNames = {}
    with open("MovieLens_data_100k/u.item") as f:
        for line in f:
            fields = line.split("|")
            movieNames[int(fields[0])] = fields[1]
    return movieNames


def parseInput(line):
    fields = line.split()
    return Row(movieID=int(fields[1]), rating=float(fields[2]))


if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder.appName("PopularMovies").getOrCreate()

    # Load up our movie ID -> name dictionary
    movieNames = loadMovieNames()

    # Get the raw data
    lines = spark.sparkContext.textFile(
        "hdfs:///user/maria_dev/MovieLens_data_100k/u.data"
    )
    # Convert it to a RDD of Row objects with (movieID, rating)
    movies = lines.map(parseInput)
    # Convert that to a DataFrame
    movieDataset = spark.createDataFrame(movies)

    # Compute average rating for each movieID
    averageRatings = movieDataset.groupBy("movieID").avg("rating")

    # Compute count of ratings for each movieID
    counts = movieDataset.groupBy("movieID").count()

    # Join the two together (We now have movieID, avg(rating), and count columns)
    averageAndCounts = counts.join(averageRatings, "movieID")

    # Take the top 10 results
    results = averageAndCounts.orderBy("avg(rating)").take(10)

    # Print them out:
    for result in results:
        print(movieNames[result[0]], result[1], result[2])

    # Stop the session
    spark.stop()
