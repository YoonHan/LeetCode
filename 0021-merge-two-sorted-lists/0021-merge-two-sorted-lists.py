# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 != None:
            return list2
        if list1 != None and list2 == None:
            return list1
        if list1 == None and list2 == None:
            return None
        
        h_merged = t_merged = ListNode()
            
        while True:
            # if one of list is at the end
            # and the other is not
            if list1 == None and list2 != None:
                t_merged.next = list2
                t_merged = t_merged.next
                break
            if list1 != None and list2 == None:
                t_merged.next = list1
                t_merged = t_merged.next
                break
                 
            # two pointer implementation
            if list1.val <= list2.val:
                t_merged.next = list1
                t_merged = t_merged.next
                list1 = list1.next
            else:
                t_merged.next = list2
                t_merged = t_merged.next
                list2 = list2.next
                
        return h_merged.next