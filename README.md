# Leetcode
 Solutions to leetcode problems.

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0001_Two_Sum.py)  | 1. Put in hash map<br>2. check for compliment in the hashmap with traget - itterator |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0002_Add_Two_Numbers.py) | 1. Itterate through both lists to add the two numbers and sum|
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0003_Longest_Substring_Without_Repeating_Characters.py) | 1. Use a set for chars<br>2. Use left and right vraibles to itterate and check(kinda like bubble sort in a way)|
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0004_Median_of_Two_Sorted_Arrays.py) | 1. Merge the 2 lists<br>2.Figure out if its an even or odd list<br>3.If even output middle most element else avg of the len/2 and len/2 +1|
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0005_Longest_Palindromic_Substring.py) | 1. Use left and right pointers to to expand from the center and check for palindromes |
| 6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0006_Zigzag_Conversion.py) | 1. Create empty array for each row<br> 2. Use direction flag to flip|
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0007_Reverse_Integer.py) | 1. Check sign then put in while loop with mod and divison by 10 operators|
| 8 | [String to Integer_ATOI](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0008_String_To_Integer(atoi).py) | Overflow, Space, and negative number |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0009_Palindrome_Number.py) | Use divison and mod by 10 |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0010_Regular_Expression_Matching.py) | Using a table to figure out the extire regression possibilities|
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0011_Container_With_Most_Water.py) | Use two pointers left and right and calculate max area and keep itterating towards teh middle|
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0012_Integer_to_Roman.py) | Create set and subract and itterate |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0013_Roman_to_Integer.py) | Create Sets and add and subtact based on postioning of roman numerals |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0014_Longest_Common_Prefix.py) | 1.Use the shortest string and check letters for teh other strings |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0015_3Sum.py) | 1. Sort the list<br>2. For every element use 2 pointers left(i+1) and right(len-1) amd check sum |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0016_3Sum_Closest.py) | Same logic as 3 some only with lowest difference |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0017_Letter_Combinations_of_a_Phone_Number.py) | Simple mapping and backtrack |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0018_4Sum.py) | Same as 3Sum but we merge pairs |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0019_Remove_Nth_Node_From_End_of_List.py) | We basically recreate the linked list with a seperate list |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0020_Valid_Parentheses.py) | Basic push pop functionality |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0021_Merge_Two_Sorted_Lists.py) | Merge sort kinda thing with stack architecture |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0022_Generate_Parantheses.py) | Backtracking and function recursion used |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0023_Merge_k_Sorted_list.py) | 1. Initailise a Min-Heap 2. Extract and Build the Result |
| 24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0024_Swap_Nodes_in_Pairs.py) | 1. Initialize Pointers 2. Traverse the list 3. Return New head |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0025_Reverse_Nodes_in_k-Group.py) | 1. use a function for the the kth node 2. strat sorting till kth node 3. Koin the rest of it after the grouping |
| 26 | []() | [Python]() | |
| 27 | []() | [Python]() | |
| 28 | []() | [Python]() | |
| 29 | []() | [Python]() | |
| 30 | []() | [Python]() | |
| 31 | []() | [Python]() | |
| 32 | []() | [Python]() | |
| 33 | []() | [Python]() | |

