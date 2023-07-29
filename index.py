import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

from statsbombpy import sb


def clear(): return os.system('cls')


clear()

# Code as it goes

data = {
    'x': [2010, 2015, 2020, 2025, 2030],
    'y': [1, 2, 5, 4, 5]
}

competitions = sb.competitions()

print(competitions)
