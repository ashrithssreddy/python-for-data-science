# import pandas as pd
# df = pd.read_csv(r"C:\Users\Ashrith Reddy\My Drive\02_learning\python\01_datatypes\mtcars.csv")

import numpy as np
data = np.arange(10)

import matplotlib.pyplot as plt
plt.plot(data)

# create a new figure
fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(np.random.randn(50).cumsum(), 'k--')



