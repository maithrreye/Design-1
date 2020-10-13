#Time Complexity: O(1) for get, put and remove
#Space Complexity O(n) where n is number of values in Hashmap

#The solution is accepted in leetcode however the Runtime shows 328ms which I couldn't reduce. 


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        Declared the size based on given input as list and initialized value to -1.
        """
        self.size=1000000
        self.arr=[-1]*1000000 
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        Calculate hashfunction for the Index and store value in that index.
        """

        self.arr[key%self.size]=value 
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.arr[key%self.size] == -1:
            return -1
        else:
            return self.arr[key%self.size]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.arr[key%self.size] != -1: 
            self.arr[key%self.size]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)