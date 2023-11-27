"""
234. Palindrome Linked List
Easy
15.5K
834
Companies

Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #1:38-1:44, 3 L's b/c didn't know how to call next variable & 1 b/c forgot to head = head.next
        arr =[]
        while head is not None:
            var = head.val
            arr.append(var)
            head = head.next
            
        
        if arr == arr[::-1]: return True
        else: return False
        
