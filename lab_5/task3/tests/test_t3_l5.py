import unittest
import resource
import time
from lab_5.task3.src.main import process_packets


class TestProcessPackets(unittest.TestCase):
    def test_single_packet(self):
        # Input data
        buffer_size = 1
        packets = [(0, 1)]
        expected_result = "0\n"

        # Given:
        result = process_packets(buffer_size, packets)

        # Then:
        self.assertEqual(result, expected_result)

    def test_dropped_packet(self):
        # Input data
        buffer_size = 1
        packets = [(0, 1), (0, 1)]
        expected_result = "0\n-1\n"

        # Given:
        result = process_packets(buffer_size, packets)

        # Then:
        self.assertEqual(result, expected_result)

    def test_multiple_packets(self):
        # Input data
        buffer_size = 2
        packets = [(0, 1), (0, 1), (1, 1)]
        expected_result = "0\n1\n2\n"

        # Given:
        result = process_packets(buffer_size, packets)

        # Then:
        self.assertEqual(result, expected_result)

    def test_buffer_full(self):
        # Input data
        buffer_size = 1
        packets = [(0, 2), (1, 1), (2, 1)]
        expected_result = "0\n-1\n2\n"

        # Given:
        result = process_packets(buffer_size, packets)

        # Then:
        self.assertEqual(result, expected_result)

    def test_empty_input(self):
        # Input data
        buffer_size = 1
        packets = []
        expected_result = ""

        # Given:
        result = process_packets(buffer_size, packets)

        # Then:
        self.assertEqual(result, expected_result)

    def test_performance(self):
        # Input data
        buffer_size = 10000
        packets = [(i, 1) for i in range(20000)]

        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = process_packets(buffer_size, packets)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {end_memory - start_memory} KB")
        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()