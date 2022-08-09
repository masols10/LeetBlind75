class Solution:    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''products=sorted(products)
        ans=[]
        s=searchWord[0]
        i=0
        while s in searchWord:
            a=[]
            for j in products:
                if j.startswith(s) and len(a)<3:
                    a.append(j)
            ans.append(a)
            i+=1
            if i<len(searchWord):
                s+=searchWord[i]
            else:
                break
            
        return ans '''
        products.sort() 
        trie = Trie() 
        trie.insert(searchWord) 
        node = trie.root 
         
        n = len(searchWord) 
        res = [[] for _ in range(n)] 
         
        for product in products: 
            node = trie.root 
            for idx, w in enumerate(product): 
                if w not in node: 
                    break 
                if w in node: 
                    node = node[w] 
                    if len(res[idx])<3: 
                        res[idx].append(product) 
                 
        return res 
         
class Trie: 
    def __init__(self): 
        self.root = {} 
     
    def insert(self,word): 
        node = self.root 
        for w in word: 
            if w not in node: 
                node[w] = {} 
            node = node[w] 
        node['#'] = '#'