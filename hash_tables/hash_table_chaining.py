class HashTable:
    def __init__(self):
        self.max_size = 10
        self.table = [[] for i in range(self.max_size)]

    def hash_function(self, key):
        index = 0
        for c in str(key):
            index += ord(c)
        return index % self.max_size

    def __setitem__(self, key, value):
        h = self.hash_function(key)

        for index, element in enumerate(self.table[h]):
            if element[0] == key:
                self.table[h][index] = (key, value)
                return
        
        self.table[h].append((key, value))

    def __getitem__(self, key):
        index = self.hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v

        raise KeyError(key)

    def __delitem__(self, key):
        h = self.hash_function(key)
        
        for index, element in enumerate(self.table[h]):
            if element[0] == key:
                del self.table[h][index]
                return
        
        raise KeyError(key)

    def __str__(self):
        result = "{"

        for list in self.table:
            for k, v in list:
                k = f"'{k}'" if type(k) == str else str(k)
                v = f"'{v}'" if type(v) == str else str(v)
                result += k + ": " + v + ', '
        
        return result.strip(', ') + "}"


    def get(self, key, default_value):
        h = self.hash_function(key)

        for k, v in self.table[h]:
            if k == key:
                return v 

        return default_value
    
# t = HashTable()

# t["march 6"] = 130
# t["march 17"] = 200
# t["march 6"] = 270
# t[1] = 'hola'
# t[2] = 'hola'

# print(t)

# del t[2]

# print(t)