import pandas as pd
import seaborn as sns

#%%

dat1 = pd.read_csv('trees.csv')

#%%

sns.boxplot(dat1.Volume).set_title('Árvore')

#%%

sns.boxplot(data = dat1)

#%%
