import unittest
from lab_5.task3.src.main import process_packets

class TestProcessPackets(unittest.TestCase):
    def test_single_packet(self):
        self.assertEqual(process_packets(1, [(0, 1)]), "0\n")

    def test_dropped_packet(self):
        self.assertEqual(process_packets(1, [(0, 1), (0, 1)]), "0\n-1\n")

    def test_multiple_packets(self):
        self.assertEqual(process_packets(2, [(0, 1), (0, 1), (1, 1)]), "0\n1\n2\n")

    def test_buffer_full(self):
        self.assertEqual(process_packets(1, [(0, 2), (1, 1), (2, 1)]), "0\n-1\n2\n")

    def test_empty_input(self):
        self.assertEqual(process_packets(1, []), "")

if __name__ == "__main__":
    unittest.main()