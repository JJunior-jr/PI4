#%% #CARREGANDO AS BIBLIOTECAS

import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# %% CONFIGURAÇÕES PARA EXIBIR TODAS AS COLUNAS DO DATAFRAME
df=pd.read_csv(r'PI4\data\academic Stress level - maintainance 1.csv',sep=',')
df.head()


#%% CÓPIA DE SEGURANÇA DO DATAFRAME ORIGINAL
df_original= df.copy()

# %% CONTAGEM DE VALORES NULOS

print(df.isnull().sum())
#%%   ESTATÍSTICA DESCRITIVA DE COLUNAS NUMÉRICAS
print('\nEstatística Descritiva para colunas numéricas')
display(df.describe())

#%%  ESTATÍSTICA DESCRITIVA DE COLUNAS CATEGÓRICAS

print('\nEstatística Descritiva para colunas categóricas')
display(df.describe(include=['object']))


#%% # CONTAR COLUNAS NUMÉRICAS E CATEGÓRICAS

num_col = df.select_dtypes(include=['number']).columns
print(f'Quantidade de colunas numéricas: {len(num_col)}')


cat_col = df.select_dtypes(include=['object']).columns
print(f'Quantidade de colunas categóricas: {len(cat_col)}')

# %% RENOMEANDO AS COLUNAS PARA PORTUGUÊS
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
df['Ambiente_Estudo'].fillna(df['Ambiente_Estudo'].mode()[0], inplace=True)

categoria_col = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

print('Análise Descritiva de Variáveis Categóricas:\n')
for col in categorical_cols:
    print(f'--- {col} ---')
    counts = df[col].value_counts()
    percentages = df[col].value_counts(normalize=True) * 100
    summary = pd.DataFrame({'Contagem': counts, 'Porcentagem': percentages.round(2)})
    print(summary.to_markdown())
    print('\n')




# %% 


df['Ambiente_Estudo'].value_counts().plot(kind='bar')
plt.title('Distribuição do Ambiente de Estudo')
# %%
