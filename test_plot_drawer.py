import unittest
import os
import shutil
from plot_drawer import draw_plots, PlotDrawer
import json


class TestPlotDrawer(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        self.json_path = os.path.join(self.test_dir, 'deviation.json')
        data = {
            'gt_corners': [1, 2, 3],
            'rb_corners': [4, 5, 6]
        }
        with open(self.json_path, 'w') as f:
            json.dump(data, f)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists('plots'):
            shutil.rmtree('plots')

    def test_draw_plots_success(self):
        plot_paths = draw_plots(self.json_path)
        self.assertTrue(len(plot_paths) > 0)
        self.assertTrue(os.path.exists(plot_paths[0]))

    def test_invalid_json(self):
        invalid_json_path = os.path.join(self.test_dir, 'invalid.json')
        with open(invalid_json_path, 'w') as f:
            f.write("invalid json content")

        with self.assertRaises(ValueError):
            draw_plots(invalid_json_path)

    def test_create_plots_directory(self):
        drawer = PlotDrawer(self.json_path)
        drawer.draw_plots()
        self.assertTrue(os.path.exists('plots'))

    def test_empty_json(self):
        empty_json_path = os.path.join(self.test_dir, 'empty.json')
        with open(empty_json_path, 'w') as f:
            json.dump({}, f)

        with self.assertRaises(KeyError):
            draw_plots(empty_json_path)


if __name__ == '__main__':
    unittest.main()
