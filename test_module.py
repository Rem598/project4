import unittest
from time_series_visualizer import load_data, clean_data

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_load_data(self):
        df = load_data()
        self.assertEqual(df.shape[0], 1000)  # Update with the actual number of rows in your dataset

    def test_clean_data(self):
        df = load_data()
        cleaned_df = clean_data(df)
        self.assertTrue(cleaned_df['value'].min() >= df['value'].quantile(0.025))
        self.assertTrue(cleaned_df['value'].max() <= df['value'].quantile(0.975))

if __name__ == '__main__':
    unittest.main()
