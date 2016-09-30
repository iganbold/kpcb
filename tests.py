from hashmap import HashMap
import unittest


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.map = HashMap(10)

    def test_set_entry_to_hashmap(self):
        result = self.map.set("hello", "world")
        self.assertTrue(True, result)

    def test_set_with_existing_key_and_new_value(self):
        self.map.set("k1", "val1")
        self.map.set("k2", "val2")
        self.map.set("k3", "val3")
        self.map.set("k2", "new value")
        self.assertEqual("new value", self.map.get("k2"))

    def test_set_not_str_key_raises_TypeError(self):
        with self.assertRaises(TypeError):
            self.map.set(99, "val1")

    def test_set_entry_to_full_hashmap(self):
        for x in range(10):
            self.map.set("k"+str(x), "val"+str(x))
        self.assertEqual(False, self.map.set("k11", "val11"))

    def test_set_with_10000_entries_and_get_1000th(self):
        mymap = HashMap(10000)
        for x in range(10000):
            mymap.set("k"+str(x), "val"+str(x))
        self.assertEqual('val1000', mymap.get("k1000"))

    def test_get_lookup_entry_by_key(self):
        self.map.set("k1", "val1")
        self.assertEqual("val1", self.map.get("k1"))

    def test_get_not_str_key_raises_TypeError(self):
        with self.assertRaises(TypeError):
            self.map.get(99)

    def test_get_with_not_existing_key(self):
        self.assertEqual(None, self.map.get("v1"))

    def test_delete_entry_from_hashmap(self):
        for x in range(5):
            self.map.set("k"+str(x), "val"+str(x))
        self.assertEqual("val4", self.map.delete("k4"))

    def test_delete_with_not_existing_key(self):
        self.assertEqual(None, self.map.delete('v1'))

    def test_delete_not_str_key_raises_TypeError(self):
        with self.assertRaises(TypeError):
            self.map.delete(99)

    def test_load_hashmap(self):
        for x in range(5):
            self.map.set("k"+str(x), "val"+str(x))
        self.assertEqual(0.5, self.map.load())

    def test_length_hashmap(self):
        for x in range(10):
            self.map.set("k"+str(x), "val"+str(x))
        self.assertEqual(10, len(self.map))
