import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%

# Carregamento da base de dados

dat1 = pd.read_csv('co2.csv')

#%%

# Gráfico de dispersão utilizando os atributos conc e uptake, agrupando pelo type

sns.scatterplot(dat1.conc, dat1.uptake, hue = dat1.Type)

#%%

# Gráfico de dispersão utilizando os atributos conc e uptake, agrupando pelo Treatment

sns.scatterplot(dat1.conc, dat1.uptake, hue = dat1.Treatment)

#%%

# Seleção de registros específicos da base de dados (Quebec e Mississippi)

q = dat1.loc[dat1['Type'] == 'Quebec']
m = dat1.loc[dat1['Type'] == 'Mississippi']

#%%

plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(1,2,2)
sns.scatterplot(m.conc, m.uptake, color = 'red').set_title('Mississippi')
plt.tight_layout()

#%%

ch = dat1.loc[dat1['Treatment'] == 'chilled']
nc = dat1.loc[dat1['Treatment'] == 'nonchilled']

#%%

plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(ch.conc, ch.uptake).set_title('Chilled')
plt.subplot(1,2,2)
sns.scatterplot(nc.conc, nc.uptake, color = 'red').set_title('Nonchilled')
plt.tight_layout()

#%%

qc = q.loc[q['Treatment'] == 'nonchilled']

#%%

sns.scatterplot(q.conc, q.uptake).set_title('Quebec')
sns.scatterplot(qc.conc, qc.uptake, color = 'red').set_title('Chilled')
plt.legend(labels = ['Quebec total', 'Quebec Chilled'])
plt.tight_layout()

#%%

dat2 = pd.read_csv('esoph.csv')

#%%

sns.catplot(x = 'alcgp', y = 'ncontrols', data = dat2, jitter = False)

#%%

# Dividindo os dados anteriores em relação auma terceira variável

sns.catplot(x = 'alcgp', y = 'ncontrols', data = dat2, col = 'tobgp')

#%%

sns.catplot(x = 'conc', y = 'uptake', data = dat1, col = 'Type')

#%%
sns.catplot(x = 'conc', y = 'uptake', data = q, col = 'Treatment', jitter = False)
