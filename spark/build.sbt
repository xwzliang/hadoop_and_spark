name := "RatingsCounter"

version := "1.0"

organization := "com.my_spark"

scalaVersion := "2.12.10"
// scalaVersion := "2.11.12"
// This scala version won't work, though my scala is indeed 2.11.12

// libraryDependencies += "org.apache.spark" %% "spark-core" % "3.0.0" % "provided"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.0.0" % "provided"
)
// libraryDependencies += "org.apache.logging.log4j" % "log4j-core" % "2.13.3"
