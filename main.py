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
def renomear_colunas(df):
    """
    Renomeia colunas específicas do DataFrame para nomes mais curtos e padronizados.
    """
    novos_nomes = {
        'Your Academic Stage': 'Estagio_Academico',
        'Peer pressure': 'Pressao_Colegas',
        'Academic pressure from your home': 'Pressao_Academica_Casa',
        'Study Environment': 'Ambiente_Estudo',
        'What coping strategy you use as a student?': 'Estrategia_Enfrentamento',
        'Do you have any bad habits like smoking, drinking on a daily basis?': 'Maus_Habitos',
        'What would you rate the academic  competition in your student life': 'Competicao_Academica',
        'Rate your academic stress index ': 'Indice_Estresse'
    }
    df.rename(columns=novos_nomes, inplace=True)


#%% # ANÁLISE DESCRITIVA DE VARIÁVEIS CATEGÓRICAS
df['Ambiente_Estudo'].fillna(df['Ambiente_Estudo'].mode()[0], inplace=True)

categoria_col = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

print('Análise Descritiva de Variáveis Categóricas:\n')
for col in categoria_col:
    print(f'--- {col} ---')
    counts = df[col].value_counts()
    percentages = df[col].value_counts(normalize=True) * 100
    summary = pd.DataFrame({'Contagem': counts, 'Porcentagem': percentages.round(2)})
    print(summary.to_markdown())
    print('\n')



# %%  # ANÁLISE DESCRITIVA DE VARIÁVEIS NUMÉRICAS


df['Ambiente_Estudo'].fillna(df['Ambiente_Estudo'].mode()[0], inplace=True)

numericas_col = ['Pressao_Colegas', 'Pressao_Academica_Casa', 'Competicao_Academica', 'Indice_Estresse']

print('Análise Descritiva de Variáveis Numéricas:\n')
print(df[numericas_col].describe().to_markdown())


# %% # ANÁLISE EXPLORATÓRIA DE DADOS (EDA) - CORRELAÇÃO

# Preencher valores ausentes na coluna 'Ambiente_Estudo' com a moda
df['Ambiente_Estudo'].fillna(df['Ambiente_Estudo'].mode()[0], inplace=True)

numericas_col = ['Pressao_Colegas', 'Pressao_Academica_Casa', 'Competicao_Academica', 'Indice_Estresse']
categoria_col = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

print('Matriz de Correlação para Variáveis Numéricas:\n')
print(df[numericas_col].corr().to_markdown())

print('\n\nMédia do Índice de Estresse por Categoria:\n')
for col in categoria_col:
    print(f'--- {col} ---\n')
    print(df.groupby(col)['Indice_Estresse'].mean().sort_values(ascending=False).to_markdown())
    print('\n')

# %% DATAVIZ

# Config de visualização
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)




# 1. Histograma do Índice de Estresse
plt.figure(figsize=(8, 5))
sns.histplot(df['Indice_Estresse'], bins=5, kde=True)
plt.title('Distribuição do Índice de Estresse')
plt.xlabel('Índice de Estresse')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('indice_estresse_histogram.png')
plt. show()#plt.close()


# 2. Gráficos de Barras para Variáveis Categóricas vs. Índice de Estresse
categoria_col = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

for col in categoria_col:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=col, y='Indice_Estresse', data=df, palette='viridis', errorbar=None)
    plt.title(f'Média do Índice de Estresse por {col.replace("_", " ")}')
    plt.xlabel(col.replace("_", " "))
    plt.ylabel('Média do Índice de Estresse')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{col}_estresse_barplot.png')
    plt. show()#plt.close()


# 3. Mapa de Calor da Correlação
numericas_col = ['Pressao_Colegas', 'Pressao_Academica_Casa', 'Competicao_Academica', 'Indice_Estresse']
plt.figure(figsize=(8, 7))
sns.heatmap(df[numericas_col].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor da Correlação entre Variáveis Numéricas')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt. show()#plt.close()


# 4. Pair Plot para Variáveis Numéricas
sns.pairplot(df[numericas_col])
plt.suptitle('Pair Plot das Variáveis Numéricas', y=1.02) # Ajusta o título para não sobrepor
plt.tight_layout()
plt.savefig('numerical_pairplot.png')
plt. show()#plt.close()

#print("Visualizações geradas e salvas como arquivos PNG.")


# %%
