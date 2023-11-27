"""
5. Longest Palindromic Substring
Medium
28.1K
1.7K
Companies

Given a string s, return the longest
palindromic
substring
in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.


"""




class Solution:
    def longestPalindrome(self, s: str) -> str:
      # Technically works but reaches the time limit on larger problems lol
        if len(s) < 2 or len(set(s)) == 1 or list(s) == list(s)[::-1]: return s
        def isPalindromic(word):
            return list(word) == list(word)[::-1]
        def findPalindromic(string_passed, current_max):
            for i in range(len(string_passed)):
                for j in range(i,len(string_passed)+1):
                    word = string_passed[i:j]
                    if isPalindromic(word) and len(word) > len(current_max): 
                        current_max = word
                        #if len(current_max) > len(string_passed) / 2: return  current_max
            return current_max
        return findPalindromic(s, "")
        """
        sset = set(s)
        countarr = []
        max = ""
        for i in sset:
            count = s.count(i)
            countarr.append(count)
            if min(countarr) == count: continue
            splt = s.split(i)
            for j in splt:
                if len(j) < len(max): continue
                max = findPalindromic(j, max)
        return max
"""

        
"""
        sset = list(sset)
        max = 0
        for i in range(len(countarr)):
            if countarr[i] > max: 
                max = countarr[i]
"""
        





"""
        arr = []
        threshold = 600
        seg = int(threshold / 2)
        rtrn = ""
        if len(s) > threshold:
            while len(s) > 1:
                
                if len(s) < seg:
                    append_length = len(s)
                    arr.append(s)
                    s = ""
                else: 
                    append_length = seg
                    arr.append(s[:seg])
                    s = s[seg:]
        else:
            return findPalindromic(s, "")
        
        for a in arr:
            s = a
        
            for i in range(len(s)):
                for j in range(i,len(s)+1):
                    word = s[i:j]
                    if isPalindromic(word) and len(word) > len(rtrn): rtrn = word
"""







"""
Valid solution:


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
"""
