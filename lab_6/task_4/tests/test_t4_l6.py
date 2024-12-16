import unittest
import time
import resource
from lab_6.task_4.src.main import SuffixMap

class TestSuffixMap(unittest.TestCase):

    def test_operations(self):
        suffix_map = SuffixMap()

        # Adding input data: key1 -> value1
        suffix_map.put("key1", "value1")
        self.assertEqual(suffix_map.get("key1"), "value1")

        # Adding input data: key2 -> value2
        suffix_map.put("key2", "value2")
        self.assertEqual(suffix_map.get("key2"), "value2")

        # Checking navigation between keys
        self.assertEqual(suffix_map.prev("key2"), "value1")
        self.assertEqual(suffix_map.next("key1"), "value2")

        # Deleting key1 and verifying fallback behavior
        suffix_map.delete("key1")
        self.assertEqual(suffix_map.get("key1"), "<none>")
        self.assertEqual(suffix_map.prev("key2"), "<none>")

    def test_performance(self):
        suffix_map = SuffixMap()

        start_time = time.time()
        initial_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Perform bulk operations
        for i in range(100000):
            suffix_map.put(f"key{i}", f"value{i}")

        end_time = time.time()
        final_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        print(f"Execution time: {end_time - start_time} seconds")
        print(f"Memory used: {(final_mem - initial_mem) / 1024} MB")


if __name__ == '__main__':
    unittest.main()