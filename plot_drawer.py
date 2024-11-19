import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:
    def __init__(self, json_path):
        self.df = pd.read_json(json_path)

    def draw_plots(self):
        plots_dir = 'plots'
        if not os.path.exists(plots_dir):
            os.makedirs(plots_dir)

        plot_paths = []
        plot_path = os.path.join(plots_dir, 'corners_comparison.png')
        self.df[['gt_corners', 'rb_corners']].plot(kind='bar')
        plt.title('Comparison of GT and RB Corners')
        plt.savefig(plot_path)
        plot_paths.append(plot_path)
        plt.clf()

        return plot_paths


def draw_plots(json_file_path):
    drawer = PlotDrawer(json_file_path)

    return drawer.draw_plots()


if __name__ == "__main__":
    import cProfile
    cProfile.run('draw_plots("/Users/Openiuk/DocuSketch_test/deviation.json")')
