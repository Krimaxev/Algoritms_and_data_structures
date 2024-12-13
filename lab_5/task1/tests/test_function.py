import unittest
from lab_5.task1.src.main import heap

class TestHeap(unittest.TestCase):
    def test_heap_valid(self):
        self.assertEqual(heap(5, [1, 3, 2, 5, 4]), "YES")
        self.assertEqual(heap(3, [1, 2, 3]), "YES")

    def test_heap_invalid(self):
        self.assertEqual(heap(5, [1, 0, 1, 2, 0]), "NO")
        self.assertEqual(heap(4, [3, 2, 5, 1]), "NO")

    def test_empty(self):
        self.assertEqual(heap(0, []), "YES")


if __name__ == "__main__":
    unittest.main()