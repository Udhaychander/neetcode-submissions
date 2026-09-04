class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = Counter(), 0
            for j in range(i, len(s2)):
                count2[s2[j]] += 1
                if count1[s2[j]] < count2[s2[j]]:
                    break
                if count1[s2[j]] == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False