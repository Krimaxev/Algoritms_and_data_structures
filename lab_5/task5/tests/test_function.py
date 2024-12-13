import unittest
from lab_5.task5.src.main import job_scheduler

class TestJobScheduler(unittest.TestCase):
    def test_single_thread(self):
        self.assertEqual(job_scheduler(1, [2, 4, 6]), [(0, 0), (0, 2), (0, 6)])

    def test_multiple_threads(self):
        self.assertEqual(job_scheduler(2, [1, 2, 3, 4]), [(0, 0), (1, 0), (0, 1), (1, 2)])

    def test_zero_duration_jobs(self):
        self.assertEqual(job_scheduler(3, [0, 0, 0, 0]), [(0, 0), (0, 0), (0, 0), (0, 0)])

    def test_large_jobs(self):
        self.assertEqual(job_scheduler(2, [10, 1, 2, 5]), [(0, 0), (1, 0), (1, 1), (1, 3)])

if __name__ == "__main__":
    unittest.main()