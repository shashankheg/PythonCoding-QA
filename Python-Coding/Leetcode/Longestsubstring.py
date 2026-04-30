''''Given a string s, find the length of the longest

without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

''' This is a typical sliding window problem with a srting s

     Initialize both pointers l and r in the position 0.
     create a hashset to store non repeating chars
     
     increament r and if the char is found  remove the s[l] and increment l'''


class solution :
    def longestsubstring(self, s :str)-> int :
        l , r = 0, 0  # left 
        longest = 0 #longest substring (int) 
        sett = set()  #hashset to store the chars 
        n = len(s)
        for r in range(n):
            while s[r] in sett :
                sett.remove(s[l])
                l += 1
            w = (r -l) + 1    
            longest = max(longest, w)
            sett.add(s[r])
             
        return longest 

sol = solution()
num = sol.longestsubstring('abcabcbb')     
print(num)