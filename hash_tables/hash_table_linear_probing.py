class HashTable:
    def __init__(self):
        self.max_size = 10
        self.table = [None for i in range(self.max_size)]

    def get_positions(self, index):
        return [i for i in range(index, self.max_size)] + [i for i in range(index)]

    def hash_function(self, key):
        index = 0
        for c in str(key):
            index += ord(c)
        return index % self.max_size

    def __setitem__(self, key, value):
        h = self.hash_function(key)

        positions = self.get_positions(h)
        for position in positions:
            if self.table[position] is None:
                self.table[position] = (key, value)
                return
            
            if self.table[position][0] == key:
                self.table[position] = (key, value)
                return

        raise Exception('Full hash table!')



    def __getitem__(self, key):
        index = self.hash_function(key)

        positions = self.get_positions(index)

        for position in positions:
            if self.table[position] is None:
                break

            if self.table[position][0] == key:
                return self.table[position][1]
            
        raise KeyError(key)

    def __delitem__(self, key):
        h = self.hash_function(key)

        positions = self.get_positions(h)

        for position in positions: 
            if self.table[position] is None:
                break

            if self.table[position][0] == key:
                self.table[position] = None
                return

        raise KeyError(key)

    def __str__(self):
        result = "{"

        for element in self.table:
            if element is None:
                continue

            k, v = element
            k = f"'{k}'" if type(k) == str else str(k)
            v = f"'{v}'" if type(v) == str else str(v)
            result += k + ": " + v + ', '
        
        return result.strip(', ') + "}"


    def get(self, key, default_value):
        h = self.hash_function(key)

        positions = self.get_positions(h)

        for position in positions:
            if self.table[position] is None:
                break

            if self.table[position][0] == key:
                return self.table[position][1]
            
        return default_value


# t = HashTable()

# print(t.hash_function("march 6"))
# print(t.hash_function("march 17"))

# t["march 6"] = 320
# t["march 17"] = 100
# t["march 1"] = 1
# t["march 2"] = 2
# t["march 8"] = 8
# t["march 9"] = 9
# 
# print(t.get("march 17", "no existe"))