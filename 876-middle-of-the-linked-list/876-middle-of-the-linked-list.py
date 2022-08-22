# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        pointer = head
        while pointer.next != None:
            pointer = pointer.next
            length += 1
        
        num_of_steps = length // 2
        for step in range(num_of_steps):
            head = head.next
            
        return head
