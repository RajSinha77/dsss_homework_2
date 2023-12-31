import unittest
from math_quiz import Generate_Random_Integer, Generate_Random_Operator, Evaluate_Mathematical_Expression

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Generate_Random_Integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # T
        for _ in range(1000):  # Test a large number of random operators
            rand_operator = Generate_Random_Operator()
            self.assertTrue(rand_operator in operator)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3,2,'-','3-2',1),
                (4,3,'*','4*3',12)
            ]

            for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = Evaluate_Mathematical_Expression(num_1, num_2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
