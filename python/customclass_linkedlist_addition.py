# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Spent an hour trying to work with the custom class, ended up just looking up the solution
To still make this a learning experience I'll just add clarifying components. 
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Declare the custom class to store the result
        head = ListNode() #dummy variable
        current = head  # Initialize a pointer to the head of the result list
        carry = 0  # Initialize a carry variable to handle digit overflow

        # Continue processing until both input lists are empty and there's no carry left
        while (l1 is not None or l2 is not None or carry != 0):
            # Extract the values of the current nodes (or use 0 if the node is None)
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            # Calculate the total sum for the current digit position
            total = l1_value + l2_value + carry

            # Create a new node with the least significant digit of the total
            current.next = ListNode(total % 10)

            # Update the carry for the next iteration (if any)
            carry = total // 10

            # Move the list pointers forward (if nodes exist) to process the next digits
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next  # Move the result list pointer to the next position

        # Return the result list (excluding the initial dummy node)
        return head.next



"""
My solution (that did not work lmao)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        bolRun = True
        return_array = []
        carry = 0
        counter = 10
        while bolRun:
            val1 = l1.val
            val2 = l2.val
            print(val1,val2)
            if counter == 0 or (val1 == None and val2 == None):
                bolRun = False
                continue
            elif val1 == None: val1 = 0
            elif val2 == None: val2 = 0
            result = carry
            carry = 0
            result += val1 + val2
            return_array.append(result)
            l1.next
            l2.next
            counter -= 1
        return return_array
"""
