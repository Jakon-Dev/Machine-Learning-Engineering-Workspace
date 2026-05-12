import sys
import os
# Add the project root to sys.path to allow importing the utils module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# IMPORT MODULES
from utils.dataset import get_data_set, print_pretty_df


import numpy as np
import matplotlib.pyplot as plt

# LOAD DATA
df = get_data_set(r"nba_player_stats_2026.csv")

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