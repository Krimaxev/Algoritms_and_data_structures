import unittest
from lab_5.task5.src.main import job_scheduler
import resource
import time


class TestJobScheduler(unittest.TestCase):
    def test_single_thread(self):
        # Input data
        num_threads = 1
        job_durations = [2, 4, 6]
        expected_result = [(0, 0), (0, 2), (0, 6)]

        # Given:
        result = job_scheduler(num_threads, job_durations)

        # Then:
        self.assertEqual(result, expected_result)

    def test_multiple_threads(self):
        # Input data
        num_threads = 2
        job_durations = [1, 2, 3, 4]
        expected_result = [(0, 0), (1, 0), (0, 1), (1, 2)]

        # Given:
        result = job_scheduler(num_threads, job_durations)

        # Then:
        self.assertEqual(result, expected_result)

    def test_zero_duration_jobs(self):
        # Input data
        num_threads = 3
        job_durations = [0, 0, 0, 0]
        expected_result = [(0, 0), (0, 0), (0, 0), (0, 0)]

        # Given:
        result = job_scheduler(num_threads, job_durations)

        # Then:
        self.assertEqual(result, expected_result)

    def test_large_jobs(self):
        # Input data
        num_threads = 2
        job_durations = [10, 1, 2, 5]
        expected_result = [(0, 0), (1, 0), (1, 1), (1, 3)]

        # Given:
        result = job_scheduler(num_threads, job_durations)

        # Then:
        self.assertEqual(result, expected_result)

    def test_performance(self):
        # Input data
        num_threads = 10000
        job_durations = [1] * 10000


        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Given:
        result = job_scheduler(num_threads, job_durations)

        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # Then:
        self.assertEqual(len(result), len(job_durations))
        print(f"Execution Time: {end_time - start_time} seconds")
        print(f"Memory Usage: {end_memory - start_memory} KB")


if __name__ == "__main__":
    unittest.main()