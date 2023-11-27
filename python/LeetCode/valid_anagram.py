"""
242. Valid Anagram
Easy
11K
345
Companies

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        s1, s2 = set(s), set(t)
        
        for i in s1:
            if s.count(i) != t.count(i): return False
        if l1 == l2 and s1 == s2: return True
        else: return False

# solved in 7 mins, with 2 failed runs, 1 bc of of typo & other bc of unhanlded exception
