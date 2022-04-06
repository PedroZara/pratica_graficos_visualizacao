import pandas as pd
import matplotlib.pyplot as plt

#%%

dat1 = pd.read_csv('trees.csv')

#%%

plt.boxplot(dat1.Volume, vert = False, showfliers = False, notch = True, patch_artist = True)
plt.title('Arvores')
plt.xlabel('Volume')

#%%

plt.boxplot(dat1, showfliers=False)
plt.title('Arvores')
plt.xlabel('Dados')

#%%

plt.boxplot(dat1.Girth, showfliers=False, vert = False, patch_artist = True)
plt.boxplot(dat1.Volume, showfliers=False, vert = False, patch_artist = True)
plt.boxplot(dat1.Height, showfliers=False, vert = False)
plt.tight_layout
plt.title('Arvores')
plt.xlabel('Dados')

#%%
