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
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0025_Reverse_Nodes_in_k-Group.py) | 1. Use a function for the the kth node 2. strat sorting till kth node 3. Koin the rest of it after the grouping |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0026_Remove_Duplicates_from_Sorted_Array.py) | 1. Using a different counter to reassign the unique elements in the same list |
| 27 | [Remove Elements](https://leetcode.com/problems/remove-element/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0027_Remove_Element.py) | 1. Use k as pointer to track where to place the next non-val element 2. Itterate through the array using a range-based loop 3. non val elements are copied to k's position and k is incremented |
| 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0028_Find_the_Index_of_the_First_Occurrence_in_a_String.py) | 1. Get len of needle 2. Itterate through the list with a substring len of the needle 3. IF found return the index else return -1|
| 29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0029_Divide_Two_Integers.py) | 1. Bit shifts: x << 1 is equivalent to x * 2 2. Avoiding overflow: Clamp result between [-2³¹, 2³¹ - 1] 3. Efficiency: Instead of subtracting divisor one by one, we subtract it in exponentially increasing chunks (doubling each time) |
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0030_Substring_with_Concatenation_of_All_Words.py) | 1. Only consider starting points from 0 to word_len - 1 to cover all alignments 2. Slide the window forward one word at a time (instead of checking each possible start index independently) 3. Maintain a dynamic count of words seen in the current window |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0031_Next_Permutation.py) | 1. Find the first decreasing element from the end 2. Find the element just larger than nums[i] to the right 3. Reverse the subarray nums[i+1:] |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0032_Next_Permutation.py) | Use a stack to push open paranthesis and pop close paranthesis|
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0033_Search_in_Rotated_Sorted_Array.py) | 1. Use left and right pointers to figure out which half is sorted 2. Itterate and adjust left and right accordingly |
| 34 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0034_Find_First_and_Last_Position_of_Element_in_Sorted_Array.py) | 1. Use a bounding function with left and right flags |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0035_Search_Insert_Position.py) | Basic Binary search |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0036_Valid_Sudoku.py) | Basic column and row checks |
| 37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0037_Sudoku_Solver.py) | 1. Using sets to track used numbers in rows, columns, and boxes to avoid scanning the board repeatedly. 2. Preprocessing empty cells to reduce redundant iteration. |
| 38 | [Count and Say](https://leetcode.com/problems/count-and-say/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0038_Count_and_Say.py) | 1. Base case: countAndSay(1) = "1" 2. Recursive rule: countAndSay(n) = RLE of countAndSay(n - 1) 3. RLE rule (modified): We read off digits of the previous string and describe how many of each digit there are consecutively (e.g., "21" → one 2, one 1 → "1211")|
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0039_Combination_Sum.py) | 1. Choose the number 2. Explore further with the same number 3. Un-choose the number|
| 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0040_Combination_Sum_II.py) | 1. Sort to handle duplicates and enable pruning 2. Skip duplicates at the same recursive depth 3. If the current number exceeds the remaining target, break early 4. Include the current number and move to the next  |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0041_First_Missing_Positive.py) | 1. Place each number in its correct position if possible 2. Find the first index i such that nums[i] != i + 1 3. If all numbers are in place |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0042_Trapping_Rain_Water.py) | 1. Use 4 pointers 2. Loop until pointers meet 3. Compare heights  4.continue until left>=right 5.return total water |
| 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0043_Multiply_Strings.py) | Itterate throught each of the digits to multiply like kids in math |
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0044_Wildcard_Matching.py) | Finite automata check|
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0045_Jump_Game_II.py) | Use 3 pointers |
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0046_Permutations.py) | Backtarcking |
| 47 | [Permutations II](https://leetcode.com/problems/permutations-ii/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0047_Permutations_II.py) | Backtracking again |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0048_Rotate_Image.py) | 1.Tanspose the matrix 2.Revese the matrix  |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0049_Group_Anagrams.py) | 1. Sort the strings 2, Group the same |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0050_Pow(x%2Cn).py) | Nearest squaring |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0051_N-Queens.py) | Backtracking and solving |
| 52 | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0052_N-Queens_II.py) | Backtracking and solving |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](https://github.com/KazukiNoSuzaku/Leetcode/blob/main/Python/0053_Maximum_Subarray.py) | Itterate through the digits in num |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python]() | |
| 55 | []() | [Python]() | |
| 56 | []() | [Python]() | |
| 57 | []() | [Python]() | |
| 58 | []() | [Python]() | |
| 59 | []() | [Python]() | |
| 60 | []() | [Python]() | |
| 61 | []() | [Python]() | |
| 62 | []() | [Python]() | |
| 63 | []() | [Python]() | |
| 64 | []() | [Python]() | |
| 65 | []() | [Python]() | |
| 66 | []() | [Python]() | |
| 67 | []() | [Python]() | |
| 68 | []() | [Python]() | |
| 69 | []() | [Python]() | |




