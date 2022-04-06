import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

dat1 = pd.read_csv('trees.csv')

#%%
#GxV
plt.scatter(dat1.Girth, dat1.Volume)

#%%

plt.scatter(dat1.Girth, dat1.Height)

#%%

plt.scatter(dat1.Height, dat1.Volume, marker = 'o')

#%%

plt.hist(dat1.Volume, bins = 7)

#%%

plt.figure(1)
plt.subplot(2,2,1)
plt.scatter(dat1.Girth, dat1.Volume)
plt.subplot(2,2,2)
plt.scatter(dat1.Girth, dat1.Height)
plt.subplot(2,2,3)
plt.scatter(dat1.Height, dat1.Volume, marker = 'o')
plt.subplot(2,2,4)
plt.hist(dat1.Volume, bins = 7)

#%%