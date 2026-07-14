# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while True:
            if current:
                current.val = 1001
                if current.next:
                    if current.next.val == 1001:
                        return True
                    else:
                        current = current.next
                else:
                    return False
            else:
                return False

            
