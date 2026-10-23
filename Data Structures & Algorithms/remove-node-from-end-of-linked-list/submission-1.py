# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        store=[]
        cur=head
        while cur:
            store.append(cur)
            cur=cur.next
        remove=len(store)-n
        if remove==0:
            return head.next
        store[remove-1].next=store[remove].next
        return head
        