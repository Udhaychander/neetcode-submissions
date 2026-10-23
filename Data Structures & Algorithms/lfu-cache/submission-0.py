class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq = {}
        self.groups = defaultdict(OrderedDict)
        self.minFreq = 0
    def get(self, key: int) -> int:
        if key not in self.freq:
            return -1
        frequency = self.freq[key]
        value = self.groups[frequency].pop(key)
        if not self.groups[frequency]:
            del self.groups[frequency]
            if self.minFreq == frequency:
                self.minFreq += 1
        self.freq[key] += 1
        newFreq = self.freq[key]
        self.groups[newFreq][key] = value
        return value
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.freq:
            frequency = self.freq[key]
            self.groups[frequency][key] = value
            self.get(key)
            return
        if len(self.freq) >= self.capacity:
            oldKey, _ = self.groups[self.minFreq].popitem(last=False)
            del self.freq[oldKey]
            if not self.groups[self.minFreq]:
                del self.groups[self.minFreq]
        self.freq[key] = 1
        self.groups[1][key] = value
        self.minFreq = 1