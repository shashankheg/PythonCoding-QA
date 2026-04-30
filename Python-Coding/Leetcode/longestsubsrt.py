'''
Given a string s, find the length of the longest

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


'''
        Solution is to use sliding window approach 

        Keep l and r pointers both positioning at 0.

        initialize a hashset for non repreating chars

        for the srting s if s[r] is seen in hashset , increament l , remove the s[l]
        else add the s[r]

        find the width and longest 
'''

class solution: 
    def longestsubstring(self, s:str) -> int :
        l = 0
        longest = 0
        n = len(s)

        sett =set()

        for r in range(n) :
            while s[r] in sett :
                sett.remove(s[l])
                l +=1
            w = (r-l)+1
            sett.add(s[r])
            longest = max(longest,w)
        return longest
    
sol = solution()

res = sol.longestsubstring('abcabcbb')
print(res)