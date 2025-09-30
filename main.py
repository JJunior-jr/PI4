#%% #CARREGANDO AS BIBLIOTECAS

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# %% Configurações para exibir todas as colunas do DataFrame
df=pd.read_csv(r'PI4\data\academic Stress level - maintainance 1.csv',sep=',')
df.head()


#%%
df_original= df.copy()

# %%

print(df.isnull().sum())
# %%
print('\nEstatística Descritiva para colunas numéricas')
display(df.describe())
# %%
df.rename(columns={
    'Your Academic Stage': 'Estagio_Academico',
    'Peer pressure': 'Pressao_Colegas',
    'Academic pressure from your home': 'Pressao_Academica_Casa',
    'Study Environment': 'Ambiente_Estudo',
    'What coping strategy you use as a student?': 'Estrategia_Enfrentamento',
    'Do you have any bad habits like smoking, drinking on a daily basis?': 'Maus_Habitos',
    'What would you rate the academic  competition in your student life': 'Competicao_Academica',
    'Rate your academic stress index ': 'Indice_Estresse'
}, inplace=True)

#%%

print('\nEstatística Descritiva para colunas categóricas')
display(df.describe(include=['object']))

# %%


df['Ambiente_Estudo'].value_counts().plot(kind='bar')
plt.title('Distribuição do Ambiente de Estudo')
# %%
