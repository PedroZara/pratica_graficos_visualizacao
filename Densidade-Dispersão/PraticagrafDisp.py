import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

dat1 = pd.read_csv('trees.csv')

#%%

plt.scatter(dat1.Girth, dat1.Volume, color = 'blue', facecolors = 'none', marker = 'o')
plt.title('Árvores')
plt.ylabel('Circunferência')
plt.xlabel('Volume')
plt.tight_layout

#%%

plt.plot(dat1.Girth, dat1.Volume)
plt.title('Árvores')
plt.ylabel('Circunferência')
plt.xlabel('Volume')
plt.tight_layout

#%%

sns.regplot(dat1.Girth, dat1.Volume, data = dat1, x_jitter = 0.2, fit_reg = False)

#%%