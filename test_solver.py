import unittest
from lp_solver import solve_lp

class TestLPSolver(unittest.TestCase):
    def test_simple_lp(self):
        result = solve_lp()
        self.assertEqual(result["objective"], 35)
        self.assertEqual(result["x"], 5)
        self.assertEqual(result["y"], 5)

if __name__ == "__main__":
    unittest.main()