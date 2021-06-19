import unittest
import math
from src.utils.math.calculate_average_score import calculate_average_score


class CalculateAverageScoreModuleTest(unittest.TestCase):
    def test_calculate_average_score(self):
        scores = [
            {
                "chapter_number": 1,
                "score": 2,
            },
            {
                "chapter_number": 2,
                "score": 3,
            },
            {
                "chapter_number": 2,
                "score": 3,
            },
            {
                "chapter_number": 2,
                "score": 5,
            },
            {
                "chapter_number": 2,
                "score": 7,
            },
            {
                "chapter_number": 2,
                "score": 10,
            }
        ]
        average = calculate_average_score(scores)
        self.assertEqual(average, 5, "The average must be equal to 5")

    def test_calculate_average_score_PI_value(self):
        scores = [
            {
                "chapter_number": 1,
                "score": math.pi,
            },
            {
                "chapter_number": 2,
                "score": 3,
            }
        ]
        average = calculate_average_score(scores)
        self.assertEqual(average, 3.1, "The average must be equal to 3.1")
