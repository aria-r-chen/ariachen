"""Regression checks for the illustrative weighted-scoring portfolio model.

Run with:
    python -m unittest discover -s analysis -p "test_*.py"

From the parent case-study directory.
These assertions verify model arithmetic; they do not validate real-world
carrier performance or represent non-public Temu data.
"""

import unittest

from weighted_scoring import (
    management_action,
    risk_categories,
    risk_level,
    selection_scores,
    selection_weights,
    weighted_score,
)


class WeightedScoringTests(unittest.TestCase):
    def test_selection_weights_sum_to_one(self):
        self.assertAlmostEqual(sum(selection_weights.values()), 1.0)

    def test_selection_scores_are_reproducible(self):
        self.assertAlmostEqual(
            weighted_score(selection_scores["cross_border_group"], selection_weights),
            3.90,
        )
        self.assertAlmostEqual(
            weighted_score(selection_scores["us_last_mile_group"], selection_weights),
            4.30,
        )

    def test_risk_weights_sum_to_one(self):
        self.assertAlmostEqual(
            sum(weight for weight, _ in risk_categories.values()),
            1.0,
        )

    def test_independent_risk_model_score(self):
        overall = sum(weight * score for weight, score in risk_categories.values())
        self.assertAlmostEqual(overall, 1.90)
        self.assertEqual(risk_level(overall), "Medium")
        self.assertEqual(
            management_action(overall),
            "Conditional approval + remediation plan",
        )

    def test_risk_band_boundaries(self):
        self.assertEqual(risk_level(1.50), "Low")
        self.assertEqual(risk_level(1.51), "Medium")
        self.assertEqual(risk_level(2.30), "Medium")
        self.assertEqual(risk_level(2.31), "High")


if __name__ == "__main__":
    unittest.main()
