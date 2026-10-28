# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        store=[]
        cur=head
        while cur:
            store.append(cur)
            cur=cur.next
        cur=head
        l,r=0,len(store)-1
        while l<r:
            store[l].next=store[r]
            l+=1
            store[r].next=store[l]
            r-=1
        store[l].next=None
