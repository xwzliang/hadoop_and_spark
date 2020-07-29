package com.my_spark.spark

import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.log4j._

object RatingsCounter {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val sc = new SparkContext("local[*]", "RatingsCounter")

    val lines = sc.textFile("../data/MovieLens_data_100k/u.data")

    val ratings = lines.map(x => x.toString().split("\t")(2))

    val results = ratings.countByValue()

    val sortedResults = results.toSeq.sortBy(_._1)

    sortedResults.foreach(println)
  }
}
