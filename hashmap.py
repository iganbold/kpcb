#!/usr/bin/env python3
"""This is hashmap module

    Usage:
        import hashmap

"""

class HashMap:
    """This class is implementation of basic HashMap. It uses only primitive types to implement a fixed-size hash map
    that associates string keys with arbitrary data object references.

    Usage:
        from hashmap import HashMap

    """

    __bucket_list = []      # Bucket List
    __count = 0             # Items in hash map

    def __init__(self, size):
        """Return an instance of the class with PRE-ALLOCATED space for the given number of objects.

        :param size:  initial size for the hashmap and size must be int
        """

        # it violates duck_type principle
        if size <= 0:
            raise ValueError("size cannot be less then zero")

        # Size of hash map
        self.capacity = size
        self.__bucket_list = [None for x in range(self.capacity)]

        # self.__empty is pre-allocated space for the given number of objects
        self.__empty = last = self.Entry()

        # create empty entities
        for x in range(self.capacity - 1):
            last.next = self.Entry()
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

        if self.__count == self.capacity:
            return False

        self.__check_key(key)

        # get bucket list index
        index = self.__get_index(key)

        # get available empty entry from pre-allocated space
        new_entity = self.__empty

        if self.__bucket_list[index] is None:
            self.__bucket_list[index] = new_entity
        else:
            for entry in self.__bucket_list[index]:
                if entry.hash == key.__hash__() and entry.key == key:
                    # update old value with new value
                    entry.value = value
                    return True
                elif entry.next is None:
                    # if collision happens it add new_entity to the linked list
                    entry.next = new_entity
                    break

        # set next available entry
        self.__empty = self.__empty.next

        # set hash , key , value
        new_entity.hash = key.__hash__()
        new_entity.key = key
        new_entity.value = value
        new_entity.next = None

        self.__count += 1
        return True

    def get(self, key):
        """Return the value associated with the given key, or null if no value is set.

        :param key:  key associated to specific value
        :return:  returns the associated value indicating success, None otherwise
        """

        self.__check_key(key)

        # get bucket list index
        index = self.__get_index(key)

        if self.__bucket_list[index] is None:
            return None

        for entry in self.__bucket_list[index]:
            if entry.hash == key.__hash__() and entry.key == key:
                return entry.value

        return None

    def delete(self, key):
        """Delete the value associated with the given key

        :param key:  key associated to specific value
        :return:  returns the value on success or None if the key has no value.
        """

        self.__check_key(key)

        index = self.__get_index(key)

        if self.__bucket_list[index] is None:
            return None

        # previous entry is used for changing references
        previous_entity = None

        # return value after delete
        value = None

        for entry in self.__bucket_list[index]:
            if entry.hash == key.__hash__() and entry.key == key:

                value = entry.value

                # delete from the bucket list
                if previous_entity is not None:
                    previous_entity.next = entry.next
                else:
                    self.__bucket_list[index] = entry.next

                # clear the entry's properties in order to make entry available for reuse
                entry.hash = None
                entry.key = None
                entry.value = None

                # put back entry to __empty list for reuse
                if self.__empty is None:
                    entry.next = None
                    self.__empty = entry
                else:
                    # swap empty reference
                    entry.next = self.__empty
                    self.__empty = entry

                break
            previous = entry

        self.__count -= 1
        return value

    def load(self):
        """Return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure

        :return: returns a float value representing the load factor of the hashmap
        """

        return self.__count/self.capacity

    def __get_index(self, key):
        """Generate the bucket list index

        :param key: key associated to specific value
        :return: bucket list index
        """

        return key.__hash__() & (self.capacity - 1)

    def __check_key(self, key):

        # it violates duck_type principle
        if not isinstance(key, str):
            raise TypeError("key must be an string")


    class Entry:

        def __init__(self, hash=None, key=None, value=None, next=None):
            """Return an instance of the Entry

            :param hash:  hashcode
            :param key:  key associated to specific value
            :param value:  value associated to specific key
            :param next:  reference to next entry which is used for collision
            """

            self.hash = hash
            self.key = key
            self.value = value
            self.next = next

        def __iter__(self):
            """Make Entry iterable

            :return: returns entry for each iteration
            """

            entry = self
            while entry is not None:
                yield entry
                entry = entry.next


if __name__ == '__main__':
    pass
