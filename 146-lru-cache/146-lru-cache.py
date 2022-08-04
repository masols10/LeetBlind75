class LRUCache:
    # using dictionary
    def __init__(self, capacity: int):
        self.cap=capacity
        self.data={}

    def get(self, key: int) -> int:
        if key not in self.data: return -1
		#item recently accessed need to be sent at last of dict, pop and reassign 
        self.data[key]=self.data.pop(key)
        return self.data[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
			#item updated recently need to be sent at last of dict, pop and update
            self.data.pop(key)
            self.data[key]=value
            return
		#if capacity is reached, we removed first item of dict. which is always least used
        if self.cap==len(self.data): self.data.pop(next(iter(self.data)))
        self.data[key]=value
        return

    # using an ordered dict
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity or key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            temp = self.cache.popitem(last = False)
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)