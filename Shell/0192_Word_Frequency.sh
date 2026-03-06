#!/bin/bash
# Write a bash script to count the frequency of each word in a text file words.txt.
# For simplicity, assume words.txt contains only lowercase characters and space characters.
# Each word must be printed on a new line with a count, the pairs sorted by frequency from highest to lowest.

# Example:
# Input: words.txt = "the day is sunny the the the sunny is is"
# Output:
# the 4
# is 3
# sunny 2
# day 1

# Author: Kaustav Ghosh

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'
