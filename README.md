# Leetcode
 Solutions to leetcode problems.

 | # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |

| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0001_Two_Sum.py)  | 1. Put in hash map<br>2. check for compliment in the hashmap with traget - itterator |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/002_Add_Two_Numbers.py) | Take care of the carry from lower digit. |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/003_Longest_Substring_Without_Repeating_Characters.py) |1. Check every possible substring O(n^2) <br>2. Remember the character index and current check pos, if character index >= current pos, then there is duplicate |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/004_Median_of_Two_Sorted_Arrays.py)  | 1. Merge two sorted lists and compute median, O(m + n) and O(m + n)<br>2. An extension of median of two sorted arrays of equal size problem|
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/005_Longest_Palindromic_Substring.py) <br>1. DP if s[i]==s[j] and P[i+1, j-1] then P[i,j]<br>2. A palindrome can be expanded from its center<br>3. Manacher algorithm|
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/007_Reverse_Integer.py) | Overflow when the result is greater than 2147483647 or less than -2147483648.
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/008_String_to_Integer(atoi).py)  | Overflow, Space, and negative number |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/009_Palindrome_Number.py)  | Get the len and check left and right with 10^len, 10 |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/011_Container_With_Most_Water.py)  | 1. Brute Force, O(n^2) and O(1)<br>2. Two points, O(n) and O(1)  |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/012_Integer_to_Roman.py) | [Background knowledge](http://www.rapidtables.com/convert/number/how-number-to-roman-numerals.htm) Just like 10-digit number, divide and minus |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/013_Roman_to_Integer.py) | Add all curr, if curr > prev, then need to subtract 2 * prev |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/015_3Sum.py) | 1. Sort and O(n^2) search with three points <br>2. Multiple Two Sum (Problem 1) |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/016_3Sum_Closest.py) | Sort and Multiple Two Sum check abs|
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/018_4Sum.py) | The same as 3Sum, but we can merge pairs with the same sum |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/019_Remove_Nth_Node_From_End_of_List.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/019_Remove_Nth_Node_From_End_of_List.java) | 1. Go through list and get length, then remove length-n, O(n) and O(n)<br>2. Two pointers, first pointer goes to 
 

