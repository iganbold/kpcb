

class HashMap:

    CAPACITY_SIZE = 0
    __map_table = []
    __count = 0

    def __init__(self, size):
        """Return an instance of the class with pre-allocated space for the given number of objects.

        :param size:  initial size for the hashmap and size must be int
        """

        # it violates duck_type principle
        if size <= 0:
            raise ValueError("size cannot be less then zero");

        self.CAPACITY_SIZE = size
        self.__map_table = [None for x in range(self.CAPACITY_SIZE)]  # need to check size is number

        # self.__empty is pre-allocated space for the given number of objects
        self.__empty = last = self.Entity()

        # create empty entities
        for x in range(self.CAPACITY_SIZE):
            last.next = self.Entity()
            last = last.next

    def __len__(self):
        return self.__count

    def set(self, key, value):
        """Stores the given key/value pair in the hash map.
        If the key exists in the hashmap, the old value is replaced with new value.

        :param key:  key associated to specific value and key must be string type
        :param value:  value associated to specific key
        :return:  returns a boolean value indicating success / failure of the operation.
        """

        if self.__count == self.CAPACITY_SIZE:
            return False

        # it violates duck_type principle
        if not isinstance(key, str):
            raise TypeError("key must be an string")

        # get bucket list index
        index = self.__get_index(key)

        # get next available empty entity from pre-allocated space
        new_entity = self.__empty

        if self.__map_table[index] is None:
            self.__map_table[index] = new_entity
        else:
            for entity in self.__map_table[index]:
                if entity.hash == key.__hash__() and entity.key == key:
                    entity.value = value
                    return True
                elif entity.next is None:
                    entity.next = new_entity
                    break

        # set hash , key , value
        new_entity.hash = key.__hash__()
        new_entity.key = key
        new_entity.value = value

        # set next available entity
        self.__empty = self.__empty.next

        self.__count += 1
        return True

    def get(self, key):
        """Return the value associated with the given key, or null if no value is set.

        :param key:  key associated to specific value
        :return:  returns the associated value indicating success, None otherwise
        """

        # it violates duck_type principle
        if not isinstance(key, str):
            raise TypeError("key must be an string")

        index = self.__get_index(key)

        if self.__map_table[index] is None:
            return None

        for entity in self.__map_table[index]:
            if entity.hash == key.__hash__() and entity.key == key:
                return entity.value

        return None

    def delete(self, key):
        """Delete the value associated with the given key

        :param key:  key associated to specific value
        :return:  returns the value on success or None if the key has no value.
        """

        # it violates duck_type principle
        if not isinstance(key, str):
            raise TypeError("key must be an string")

        index = self.__get_index(key)

        if self.__map_table[index] is None:
            return None

        for entity in self.__map_table[index]:
            if entity.hash == key.__hash__() and entity.key == key:
                if entity.value is not None:
                    result = entity.value
                    entity.value = None
                    return result
                else:
                    return None

        return None

    def load(self):
        """Return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure

        :return: returns a float value representing the load factor of the hashmap
        """

        return self.__count/self.CAPACITY_SIZE

    def __get_index(self, key):
        builtin_hash = key.__hash__()
        return builtin_hash & (self.CAPACITY_SIZE - 1)

    class Entity:
        def __init__(self, hash=None, key=None, value=None, next=None):
            self.hash = hash
            self.key = key
            self.value = value
            self.next = next

        def __iter__(self):
            entity = self
            while entity is not None:
                yield entity
                entity = entity.next


if __name__ == '__main__':
    map = HashMap(20)

    map.set("k1", "v1")
    map.set("k2", "v2")
    map.set("k3", "v3")
    map.set("k4", "v4")

    print(map.get("k4"))
    map.delete("k4")
    print(map.get("k4"))
    print(len(map))
    print(map.load())
