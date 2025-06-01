import unittest
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicDataAnalyzer(unittest.TestCase):

    def test_race_count(self):
        results = calculate_demographic_data()
        race_count = results['race_count']
        # Example expected races in your test dataset
        self.assertIn('White', race_count.index)
        self.assertIn('Black', race_count.index)
        self.assertTrue(race_count['White'] > 0)

    def test_average_age_men(self):
        results = calculate_demographic_data()
        avg_age = results['average_age_men']
        self.assertIsInstance(avg_age, float)
        self.assertGreater(avg_age, 0)

    def test_percentage_bachelors(self):
        results = calculate_demographic_data()
        percent_bachelors = results['percentage_bachelors']
        self.assertTrue(0 <= percent_bachelors <= 100)

    def test_min_work_hours(self):
        results = calculate_demographic_data()
        min_hours = results['min_work_hours']
        self.assertIsInstance(min_hours, int)
        self.assertGreaterEqual(min_hours, 0)

    # Add more tests for other results as needed...

if __name__ == '__main__':
    unittest.main()