class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {}              
        for i in range(len(order)):      
            c = order[i]                 
            order_index[c] = i      
        def compare(word):
            return [order_index[c] for c in word]
        return words == sorted(words, key=compare)