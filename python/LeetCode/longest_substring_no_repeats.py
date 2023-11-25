"""
3. Longest Substring Without Repeating Characters
Medium
37.9K
1.7K
Companies

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)): return len(s)
        
        max = 0
        #Solved in 15 mins, took 40 mins to optimize lol (too many mf reruns)
        """
        for i in range(len(s)):
            sub = []
            counter = 0
            for i in list(s[i:]):
                if i not in sub:
                    sub.append(i)
                    counter += 1
                else:
                    sub = []
                    if max < counter: max = counter
                    counter = 0
        """
        if len(s) < 200:
            checked = []
            sset = set(s)
            for i1 in range(len(s)):
                
                for i2 in range(len(s)):
                    var = s[i1:i2+1]
                    if len(var) == len(set(var)): 

                        print(var)
                        if len(var) > max: max = len(var)
        else:
            checked = []
            sset = set(s)
            for s1 in sset:
                s2 = s.split(s1)
                for s3 in s2:
                    
                    if (max < len(set(s3)) and len(set(s3)) == len(s3)): max = len(s3)   
            max += 1
        return max



"""
actual solution: 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength

"""

            

            
