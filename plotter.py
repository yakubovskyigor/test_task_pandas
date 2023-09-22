import pandas as pd
import matplotlib.pyplot as plt
import requests

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
response = requests.get(url)
data = pd.read_json(response.text)


class Plotter:
    def __init__(self):
        self.saved_paths = []

    def draw_plots(self, data, column1, column2, title, output_file):
        mean_column1 = data[column1].mean()
        mean_column2 = data[column2].mean()

        plt.bar([column1, column2], [mean_column1, mean_column2])
        plt.xlabel("Columns")
        plt.ylabel("Average values")
        plt.title(title)

        plt.savefig(output_file)
        plt.close()

        self.saved_paths.append(output_file)

    def save_plot(self, file_name):
        plt.savefig(file_name)
        self.saved_paths[-1] = file_name
        plt.close()

    def get_saved_paths(self):
        return self.saved_paths


plotter = Plotter()

# Compare the average values of the two columns and save the graph
plotter.draw_plots(data,
                   "floor_min",
                   "ceiling_min",
                   "Comparison of averages",
                   "C:\\Users")  # path
plotter.draw_plots(data,
                   "floor_max",
                   "ceiling_max",
                   "Comparison of averages",
                   "C:\\Users")  # path
plotter.draw_plots(data,
                   "min",
                   "max",
                   "Comparison of averages",
                   "C:\\Users")  # path

saved_paths = plotter.get_saved_paths()
print(saved_paths)
print(data.head())
print(data.info())
print(data.shape)
print(data.isnull().sum())
