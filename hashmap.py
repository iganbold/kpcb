
class HashMap:

    CAPACITY_SIZE = 16
    __map_table = []
    __count = 0

    class Entity:
        def __init__(self, hash, key, value, entity=None):
            self.hash = hash
            self.key = key
            self.value = value
            self.entity = entity

    def __init__(self, size):
        self.CAPACITY_SIZE = size
        try:
            self.__map_table = [None for x in range(size)]
        except TypeError as ex:
            print('{} size must be integer'.format(size))

    def __len__(self):
        return self.__count

    def set(self, key, value):

        return False

    def get(self, key):

        return

    def delete(self, key):
        print("delete")

    def load(self):
        print("load")

class Dog:

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    map = HashMap(20)
