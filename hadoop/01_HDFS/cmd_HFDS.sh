#!/usr/bin/env bash

# Append unix cmd to hadoop fs -cmd to use HDFS

# list files and directory, mkdir, cat, etc.
hadoop fs -ls

# Copy from local files to HDFS
hadoop fs -copyFromLocal localfile HDFS_file

# Copy from HDFS to local
hadoop fs -copyToLocal HDFS_file localfile
