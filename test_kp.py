import unittest
from kp import solve_kp

class TestKPSolver(unittest.TestCase):
    def test_simple_kp(self):
        result = solve_kp()
        self.assertEqual(result["objective"], 10)
        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b"], 1)
        self.assertEqual(result["c"], 1)

if __name__ == "__main__":
    unittest.main()