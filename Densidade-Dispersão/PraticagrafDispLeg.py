import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

dat1 = pd.read_csv('co2.csv')

#%%

x = dat1.conc
y = dat1.uptake

#%%

tratamentos = list(set(dat1.Treatment))

#%%

for i in range(len(tratamentos)):
    indice = dat1.Treatment == tratamentos[i]
    plt.scatter(x[indice], y[indice], label = tratamentos[i])
plt.legend(loc = 'lower right')
plt.xlabel('Conc')
plt.ylabel('Uptake')

#%%

for i in range(len(tratamentos)):
    indice = dat1.Treatment == tratamentos[i]
    sns.regplot(x[indice], y[indice], label = tratamentos[i], x_jitter = 0.5, fit_reg = True)
plt.legend(loc = 'lower right')
plt.xlabel('Conc')
plt.ylabel('Uptake')
