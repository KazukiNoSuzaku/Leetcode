#!/bin/bash
# Given a text file file.txt, transpose its content.
# You may assume that each row has the same number of columns,
# and each field is separated by the ' ' character.

# Example:
# Input: file.txt = "name age\nalice 21\nryan 30"
# Output: "name alice ryan\nage 21 30"

# Author: Kaustav Ghosh

awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            col[i] = $i
        } else {
            col[i] = col[i] " " $i
        }
    }
    maxcol = NF
}
END {
    for (i = 1; i <= maxcol; i++) {
        print col[i]
    }
}
' file.txt
