import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add the project root to sys.path to allow importing the utils module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# IMPORT MODULES
from utils.dataset import get_data_set, print_pretty_df

def print_chart():
    # LOAD DATA
    df = get_data_set("nba_player_stats_2026.csv")

    print_pretty_df(df.head(10))

    # make data
    x = df['MIN']
    y = df['FGM']

    # plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    m, b = np.polyfit(x, y, 1)

    # draw line
    ax.plot(x, m*x + b, color='green')
    plt.show()

class SimpleLinearRegressionModel:
    def __init__(self):
        self.m = None
        self.b = None

    def train(self, x, y):
        self.m, self.b = np.polyfit(x, y, 1)
    
    def predict(self, x):
        if self.m is None or self.b is None:
            raise ValueError("The model must be trained before calling predict.")
        
        return self.m * x + self.b

def build_sample_model(isSimple: bool = True):
    df = get_data_set("nba_player_stats_2026.csv")
    x = df['MIN']
    y = df['FGM']
    if isSimple:
        slrm = SimpleLinearRegressionModel()
        slrm.train(x, y)

        prediction = slrm.predict(x=300)
        print(f"Predicted FGM for 300 MIN: {prediction:.2f}")

if __name__ == '__main__':
    build_sample_model()