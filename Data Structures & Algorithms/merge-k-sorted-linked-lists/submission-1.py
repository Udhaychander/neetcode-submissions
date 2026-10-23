class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        store = []
        for lst in lists:
            while lst:
                store.append(lst.val)
                lst = lst.next
        store.sort()
        res = ListNode(0)
        cur = res
        for n in store:
            cur.next = ListNode(n)
            cur = cur.next
        return res.next