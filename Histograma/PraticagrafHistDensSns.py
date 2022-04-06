import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%

dat1 = pd.read_csv('trees.csv')

#%%

# Histograma com 10 divisoes (bins)

sns.distplot(dat1.Volume, bins = 10, axlabel = 'Volume').set_title('Árvores')

#%%

dat2 = pd.read_csv('chicken.csv')

#%%

# Criando novo dataframe agrupando o atributo 'feed'

agrupado = dat2.groupby(['feed'])['weight'].sum()

#%%

# Novo dataframe para testar os filtros do pandas

teste = dat2.loc[dat2['feed'] == 'horsebean']

#%%

# Histograma considerando somente o valor 'horsebean'

horsebean = sns.distplot(dat2.loc[dat2['feed'] == 'horsebean'].weight, hist = False).set_title('horsebean')

#%%

casein = sns.distplot(dat2.loc[dat2['feed'] == 'casein'].weight, hist = False).set_title('casein')

#%%

linseed = sns.distplot(dat2.loc[dat2['feed'] == 'linseed'].weight, hist = False).set_title('linseed')

#%%

meatmeal = sns.distplot(dat2.loc[dat2['feed'] == 'meatmeal'].weight, hist = False).set_title('meatmeal')

#%%

soybean = sns.distplot(dat2.loc[dat2['feed'] == 'soybean'].weight, hist = False).set_title('soybean')

#%%

sunflower = sns.distplot(dat2.loc[dat2['feed'] == 'sunflower'].weight, hist = True, bins = 4).set_title('sunflower')

#%%

# Impressão em 2x3

plt.figure()
plt.subplot(3,2,1)
sns.distplot(dat2.loc[dat2['feed'] == 'horsebean'].weight).set_title('horsebean')
plt.subplot(3,2,2)
sns.distplot(dat2.loc[dat2['feed'] == 'casein'].weight).set_title('casein')
plt.subplot(3,2,3)
sns.distplot(dat2.loc[dat2['feed'] == 'linseed'].weight, bins = 8).set_title('linseed')
plt.subplot(3,2,4)
sns.distplot(dat2.loc[dat2['feed'] == 'meatmeal'].weight).set_title('meatmeal')
plt.subplot(3,2,5)
sns.distplot(dat2.loc[dat2['feed'] == 'soybean'].weight).set_title('soybean')
plt.subplot(3,2,6)
sns.distplot(dat2.loc[dat2['feed'] == 'sunflower'].weight, bins = 4).set_title('sunflower')
plt.tight_layout()
