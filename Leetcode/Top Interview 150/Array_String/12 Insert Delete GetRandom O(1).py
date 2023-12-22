from random import choice


class RandomizedSet(object):
    def __init__(self):
        self.randset = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        new_val = False if val in self.randset else True
        if new_val:
            self.randset.append(val)
        return new_val

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        in_set = True if val in self.randset else False

        if in_set:
            self.randset.remove(val)
        return in_set

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.randset)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(10)
param_2 = obj.remove(12)
param_3 = obj.getRandom()
print(param_1, param_2, param_3)
