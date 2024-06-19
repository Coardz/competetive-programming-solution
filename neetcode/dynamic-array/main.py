class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Soft Deletion
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

    def printArray(self) -> None:
        print(self.arr[:self.size])
            

da = DynamicArray(2)   # Initialize with capacity 2 = [0, 0]

# so what push back does is it adds number to the list for example on previous array it's
# [0, 0] the pushback(1) make it [1, 0]
da.pushback(1)         # [1, 0], size = 1
da.pushback(2)         # [1, 2], size = 2
da.pushback(3)         # Resize to [1, 2, 0, 0], then [1, 2, 3, 0], size = 3
da.pushback(4)         # [1, 2, 3, 4] size = 4
da.pushback(5)         # Resize to [1, 2, 3, 4, 0, 0 ,0, 0] then [1, 2, 3, 4, 5, 0, 0, 0] size = 5

print("GET:",da.get(4))       # Output: 5
da.set(4, 10)           # [1, 2 3, 4, 5] to [1, 2, 3, 4, 10]
print("GET:", da.get(4))       # Output: 10
print("POPBACK:", da.popback())    # Output: 3, array [1, 4, 3, 0], size = 2
print("SIZE:",da.getSize())    # Output: 2
print("CAPACITY:", da.getCapacity())# Output: 4
print(da.printArray())