import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%

# Importando base de dados

dat1 = pd.read_csv('trees.csv')
#sh = dat1.shape
#d1 = dat1.head

#%%

#Criando um histograma considerando segundo atributo da base de dados e com duas divisões (bins)
#A variável 'h' armazena as faixas de valores de Height

h = np.histogram(dat1.iloc[:,1], bins = 6)

#%%

# Visualizando o histograma

plt.hist(dat1.iloc[:,1], bins = 6)
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')
plt.tight_layout

#%%


