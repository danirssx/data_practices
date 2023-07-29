import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


def clear(): return os.system('cls')


clear()

# Code as it goes

data = {
    'x': [2010, 2015, 2020, 2025, 2030],
    'y': [1, 2, 3, 4, 5]
}

plt.plot(data['x'], data['y'], color='red')
plt.xlabel('years')
plt.ylabel('seasons')

plt.show()
