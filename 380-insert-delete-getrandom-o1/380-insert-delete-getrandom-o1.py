from random import randint

class RandomizedSet:
    def __init__(self):
        self.li = []
        self.set = {}

    def insert(self, val: int) -> bool:
        if val not in self.set :
            self.li.append(val)
            self.set[val] = len(self.li)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set :
            idx = self.set[val]
            self.li[idx] = self.li[-1]
            self.set[self.li[-1]] = idx
            self.li.pop()
            del self.set[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.li[randint(0, len(self.li)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()