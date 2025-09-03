"""
Design HashSet [Easy]
Pattern: Hash Table (seperate chaining)

Idea: 
- Use an array of bucket. Bucket index = key % SIZE.
- Each bucket stores a list of keys (chaining).
- add(key): insert key if not present in bucket.
- contain(key): check if key is in bucket.
- remove(key): remove key from bucket if it exists.

Time: 
- O(1) - average per operation (expected, with good distribution)
-O(k) - worst case in a bucket

Space:
- O(n) for stored keys + O(SIZE) for bucket

Edge cases:
- Duplicate adds should not create multiple entries.
- Removing absent key should do nothing. 
- Collision (keys mapping to same bucket) handle by chaining. 
"""

class MyHashSet: 
    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size

    def calculate_hash_value(self, key: int) -> int:    
        return key % self.size

    def add(self, key: int) -> None:
        hash_value = self.calculate_hash_value(key)
        
        if self.table[hash_value] == None:
            self.table[hash_value] = [key]
        else:
            self.table[hash_value].append(key)

    def remove(self, key: int) -> None:
        hash_value = self.calculate_hash_value(key)

        if self.table[hash_value] != None:
            while key in self.table[hash_value]:
                self.table[hash_value].remove(key)

    def contains(self, key: int) -> bool:
        hash_value = self.calculate_hash_value(key)

        if self.table[hash_value] != None:
            return key in self.table[hash_value]
        
        return False