import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_base = pd.read_csv('data/municipio.csv')

#print(data_base.head())

selecao = data_base['id_municipio'] == 1100015

araraquara = data_base.query('id_municipio == 3503208')
sao_carlos = data_base.query('id_municipio == 3548906')

plt.style.use('seaborn-darkgrid')

plt.figure(figsize=(16, 7))
plt.title('PIB - Araraquara/SP', loc='left', fontsize=18, fontweight=200)
plt.xlabel('Período')
plt.ylabel('Valor (R$ Bi)')
araraquara_grafico = sns.lineplot(araraquara, x='ano', y='pib', color='#008c4a', linewidth=4, alpha=0.7)
plt.show()

plt.figure(figsize=(16, 7))
plt.title('PIB - Sâo Carlos/SP', loc='left', fontsize=18, fontweight=200)
plt.xlabel('Período')
plt.ylabel('Valor (R$ Bi)')
sao_carlos_grafico = sns.lineplot(sao_carlos, x='ano', y='pib', color='#000099', linewidth=4, alpha=0.7)
plt.show()





