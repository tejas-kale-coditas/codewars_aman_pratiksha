"""
Question Link : https://www.codewars.com/kata/596b8a3fc4cb1de46b000001/train/python
<| 7 kyu |> | 02th Sept '25
Your company MRE Tech has hired a spiritual consultant who advised on a new Balance 
policy: Don't take sides, don't favour, stay in the middle. This policy even applies to the software where all strings should now be centered. You are the poor soul to implement it.

Task
Implement a function center that takes a string strng, an integer width, and an optional character fill (default: ' ') and returns a new string of length width where strng is centered and on the right and left padded with fill.

center(strng, width, fill=' ')
If the left and right padding cannot be of equal length make the padding on the left side one character longer.

If strng is longer than width return strng unchanged.

Examples
center('a', 3)  # returns " a "
center('abc', 10, '_')  # returns "____abc___"
center('abcdefg', 2)  # returns "abcdefg"
"""

# Solution
def center(strng, width, fill=' '):
    n = len(strng)
    if width < n:
        return strng
    
    rem = width - n
    r_center = rem//2
    l_center = width - (r_center + n)
    
    return l_center*fill + strng + r_center*fill