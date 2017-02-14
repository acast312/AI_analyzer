import numpy as np
import matplotlib.pyplot as plt
from data_converter import grab_data

#grab data can have a filename represented as a string
scores, epochs, deviation = grab_data()


plt.errorbar(epochs, scores, deviation, linestyle='-', marker='o')
plt.grid()

plt.show()