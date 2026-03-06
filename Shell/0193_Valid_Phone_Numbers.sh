#!/bin/bash
# Given a text file file.txt that contains a list of phone numbers (one per line),
# write a one-liner bash script to print all valid phone numbers.
# A valid phone number must be in one of the following two formats:
# (xxx) xxx-xxxx or xxx-xxx-xxxx
# where x means a digit.

# Example:
# Input: file.txt = "987-123-4567\n123 456-7890\n(123) 456-7890"
# Output: "987-123-4567\n(123) 456-7890"

# Author: Kaustav Ghosh

grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
