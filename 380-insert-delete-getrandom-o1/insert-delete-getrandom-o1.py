import random
class RandomizedSet:

    def __init__(self):
        
        self.box = set()
        # self.arr = list(self.box)

    def insert(self, val: int) -> bool:
        if val not in self.box:
            self.box.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.box:
            self.box.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(tuple(self.box))


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()