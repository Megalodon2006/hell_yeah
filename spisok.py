class MyDict:

    def __init__(self):
        self.__keys = []
        self.__values = []

    def my_hash(self, key):
        key_str = str(key)
        total = 0
        for i, char in enumerate(key_str):
            total += ord(char) * (i + 1)
        return total % 1024

    def __getitem__(self, key):
        key_hash = self.my_hash(key)
        for i, my_key in enumerate(self.__keys):
            if self.my_hash(my_key) == key_hash:
                return self.__values[i]
        raise KeyError(f"Key '{key}' not found.")

    def __setitem__(self, key, value):
        key_hash = self.my_hash(key)
        for i, my_key in enumerate(self.__keys):
            if self.my_hash(my_key) == key_hash:
                self.__values[i] = value
                return
        self.__keys.append(key)
        self.__values.append(value)

    def __repr__(self):
        if not self.__keys:
            return "{}"
        
        items = []
        for i in range(len(self.__keys)):
            key_str = repr(self.__keys[i])
            value_str = repr(self.__values[i])
            items.append(f"{key_str}: {value_str}")
        
        return "{" + ", ".join(items) + "}"

    def __len__(self):
        return len(self.__keys)

    def clear(self):
        self.__keys = []
        self.__values = []

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self):
        return self.__keys.copy()

    def values(self):
        return self.__values.copy()

    def items(self):
        return list(zip(self.__keys, self.__values))

    def update(self, other):
        if hasattr(other, 'keys'):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value

    def copy(self):
        new_dict = MyDict()
        new_dict.__keys = self.__keys.copy()
        new_dict.__values = self.__values.copy()
        return new_dict

    def pop(self, key, default=None):
        key_hash = self.my_hash(key)
        for i, my_key in enumerate(self.__keys):
            if self.my_hash(my_key) == key_hash:
                value = self.__values[i]
                del self.__keys[i]
                del self.__values[i]
                return value
        if default is not None:
            return default
        raise KeyError(f"Key '{key}' not found.")

    def popitem(self):
        if not self.__keys:
            raise KeyError("Dictionary is empty")
        key = self.__keys[-1]
        value = self.__values[-1]
        del self.__keys[-1]
        del self.__values[-1]
        return (key, value)

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

# Тестирование
if __name__ == "__main__":
    d = MyDict()
    d["name"] = "Artem"  
    d["age"] = 19        
    d[0] = "zero"
    print("Dict:", d)
    
    print("\n--- Testing methods ---")
    print("d.get('name'):", d.get('name'))
    print("d.get('occupation'):", d.get('occupation'))
    print("Keys:", d.keys())
    print("Values:", d.values())
    print("Items:", d.items())
    
    d.update({'city': 'Novosibirsk', 'age': 20}) 
    print("After update:", d)
    
    d_copy = d.copy()
    print("Copy:", d_copy)
    
    print("Popped:", d.pop('city'))
    print("After pop:", d)
    
    print("Setdefault:", d.setdefault('country', 'Russia'))
    print("After setdefault:", d)
    
    print("Popitem:", d.popitem())
    print("After popitem:", d)