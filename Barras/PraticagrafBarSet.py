import pandas as pd

dat1 = pd.read_csv('insect.csv')

#%%

agrupado = dat1.groupby(['spray'])['count'].sum()

#%%

agrupado.plot.bar(color = 'gray' , legend = True)

#%%

agrupado.plot.bar(color = ['blue', 'yellow', 'green', 'pink', 'orange', 'black'], legend = True)

#%%

agrupado.plot.pie(legend = True)
