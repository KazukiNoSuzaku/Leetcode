#!/bin/bash
# Given a text file file.txt, print just the 10th line of the file.
# If the file contains less than 10 lines, output nothing.

# Example:
# Input: file.txt = "Line 1\nLine 2\n...\nLine 10\n..."
# Output: "Line 10"

# Author: Kaustav Ghosh

sed -n '10p' file.txt
