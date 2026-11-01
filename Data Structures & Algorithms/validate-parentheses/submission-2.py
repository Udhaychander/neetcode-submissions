class Solution:
    def isValid(self, s: str) -> bool:
        store=[]
        mapping={'[':']','(':')','{':'}'}
        for c in s:
            if c in mapping:
                store.append(c)
            else:
                if store and mapping[store[-1]]==c:
                    store.pop()
                else:
                    return False
        return True