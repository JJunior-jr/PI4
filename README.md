# PI4


# Análise Exploratória de Dados: Estresse Acadêmico

## Visão Geral

Este projeto realiza uma Análise Exploratória de Dados (EDA) em um conjunto de dados sobre o estresse acadêmico entre estudantes. O objetivo é identificar padrões, tendências e relações entre as variáveis que contribuem para o estresse, utilizando as bibliotecas Python `pandas`, `matplotlib` e `seaborn`.

## Conjunto de Dados

O conjunto de dados, `academicStresslevel-maintainance1.csv`, foi coletado através de um formulário Google e contém informações sobre os níveis de estresse acadêmico de alunos do ensino médio, graduação e pós-graduação. Ele possui 140 entradas e 9 colunas, abrangendo aspectos como pressão de colegas, pressão acadêmica familiar, ambiente de estudo, estratégias de enfrentamento, maus hábitos, competição acadêmica e um índice de estresse autorrelatado.

## Ações Realizadas e Códigos Python

### 1. Carregamento e Exploração Inicial dos Dados

Nesta etapa, o conjunto de dados foi carregado e uma visão geral inicial foi obtida para entender sua estrutura, tipos de dados e identificar valores ausentes.

**Código Python:**

```python
import pandas as pd

data = pd.read_csv("/home/ubuntu/upload/academicStresslevel-maintainance1.csv")

print("Primeiras 5 linhas do dataset:")
print(data.head())

print("\nInformações do dataset:")
data.info()

print("\nValores ausentes por coluna:")
print(data.isnull().sum())

print("\nEstatísticas descritivas para colunas numéricas:")
print(data.describe())

print("\nEstatísticas descritivas para colunas categóricas:")
print(data.describe(include="object"))
```

**Resultados Chave:**
*   140 entradas e 9 colunas.
*   Identificado um valor ausente na coluna `Study Environment`.
*   Colunas renomeadas para facilitar a análise (`Estagio_Academico`, `Pressao_Colegas`, `Pressao_Academica_Casa`, `Ambiente_Estudo`, `Estrategia_Enfrentamento`, `Maus_Habitos`, `Competicao_Academica`, `Indice_Estresse`).
*   O valor ausente em `Ambiente_Estudo` foi preenchido com a moda da coluna.

### 2. Análise Descritiva das Variáveis Categóricas

Foi realizada uma análise de frequência e porcentagem para as variáveis categóricas, fornecendo insights sobre a distribuição dos estudantes em diferentes categorias.

**Código Python:**

```python
import pandas as pd

data = pd.read_csv("/home/ubuntu/upload/academicStresslevel-maintainance1.csv")

# Renomear colunas para facilitar o uso
data.rename(columns={
    'Your Academic Stage': 'Estagio_Academico',
    'Peer pressure': 'Pressao_Colegas',
    'Academic pressure from your home': 'Pressao_Academica_Casa',
    'Study Environment': 'Ambiente_Estudo',
    'What coping strategy you use as a student?': 'Estrategia_Enfrentamento',
    'Do you have any bad habits like smoking, drinking on a daily basis?': 'Maus_Habitos',
    'What would you rate the academic  competition in your student life': 'Competicao_Academica',
    'Rate your academic stress index ': 'Indice_Estresse'
}, inplace=True)

# Preencher valores ausentes na coluna 'Ambiente_Estudo' com a moda
data['Ambiente_Estudo'].fillna(data['Ambiente_Estudo'].mode()[0], inplace=True)

categorical_cols = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

print('Análise Descritiva de Variáveis Categóricas:\n')
for col in categorical_cols:
    print(f'--- {col} ---')
    counts = data[col].value_counts()
    percentages = data[col].value_counts(normalize=True) * 100
    summary = pd.DataFrame({'Contagem': counts, 'Porcentagem': percentages.round(2)})
    print(summary.to_markdown())
    print('\n')
```

**Resultados Chave:**
*   A maioria dos participantes são estudantes de graduação (71.43%).
*   50% dos estudantes possuem um ambiente de estudo tranquilo (`Peaceful`).
*   A estratégia de enfrentamento mais comum é a análise intelectual da situação (62.14%).
*   87.86% dos estudantes não possuem maus hábitos.

### 3. Análise Descritiva das Variáveis Numéricas

Estatísticas descritivas (média, desvio padrão, mínimo, máximo, quartis) foram calculadas para as variáveis numéricas, todas em uma escala de 1 a 5.

**Código Python:**

```python
import pandas as pd

data = pd.read_csv("/home/ubuntu/upload/academicStresslevel-maintainance1.csv")

# Renomear colunas para facilitar o uso
data.rename(columns={
    'Your Academic Stage': 'Estagio_Academico',
    'Peer pressure': 'Pressao_Colegas',
    'Academic pressure from your home': 'Pressao_Academica_Casa',
    'Study Environment': 'Ambiente_Estudo',
    'What coping strategy you use as a student?': 'Estrategia_Enfrentamento',
    'Do you have any bad habits like smoking, drinking on a daily basis?': 'Maus_Habitos',
    'What would you rate the academic  competition in your student life': 'Competicao_Academica',
    'Rate your academic stress index ': 'Indice_Estresse'
}, inplace=True)

# Preencher valores ausentes na coluna 'Ambiente_Estudo' com a moda
data['Ambiente_Estudo'].fillna(data['Ambiente_Estudo'].mode()[0], inplace=True)

numerical_cols = ['Pressao_Colegas', 'Pressao_Academica_Casa', 'Competicao_Academica', 'Indice_Estresse']

print('Análise Descritiva de Variáveis Numéricas:\n')
print(data[numerical_cols].describe().to_markdown())
```

**Resultados Chave:**
*   O `Indice_Estresse` médio é de aproximadamente 3.72, indicando um nível de estresse moderado a alto.
*   Todas as variáveis de pressão (`Pressao_Colegas`, `Pressao_Academica_Casa`, `Competicao_Academica`) têm médias em torno de 3 a 3.5.

### 4. Análise de Correlações e Relações entre Variáveis

Foi calculada a matriz de correlação de Pearson para as variáveis numéricas e a média do `Indice_Estresse` foi analisada em relação a cada categoria das variáveis categóricas.

**Código Python:**

```python
import pandas as pd

data = pd.read_csv("/home/ubuntu/upload/academicStresslevel-maintainance1.csv")

# Renomear colunas para facilitar o uso
data.rename(columns={
    'Your Academic Stage': 'Estagio_Academico',
    'Peer pressure': 'Pressao_Colegas',
    'Academic pressure from your home': 'Pressao_Academica_Casa',
    'Study Environment': 'Ambiente_Estudo',
    'What coping strategy you use as a student?': 'Estrategia_Enfrentamento',
    'Do you have any bad habits like smoking, drinking on a daily basis?': 'Maus_Habitos',
    'What would you rate the academic  competition in your student life': 'Competicao_Academica',
    'Rate your academic stress index ': 'Indice_Estresse'
}, inplace=True)

# Preencher valores ausentes na coluna 'Ambiente_Estudo' com a moda
data['Ambiente_Estudo'].fillna(data['Ambiente_Estudo'].mode()[0], inplace=True)

numerical_cols = ['Pressao_Colegas', 'Pressao_Academica_Casa', 'Competicao_Academica', 'Indice_Estresse']
categorical_cols = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

print('Matriz de Correlação para Variáveis Numéricas:\n')
print(data[numerical_cols].corr().to_markdown())

print('\n\nMédia do Índice de Estresse por Categoria:\n')
for col in categorical_cols:
    print(f'--- {col} ---\n')
    print(data.groupby(col)['Indice_Estresse'].mean().sort_values(ascending=False).to_markdown())
    print('\n')
```

**Resultados Chave:**
*   Correlações positivas moderadas entre as variáveis de pressão e o `Indice_Estresse`.
*   Alunos do ensino médio e aqueles em ambientes de estudo `disrupted` ou `Noisy` tendem a ter índices de estresse mais altos.
*   `Emotional breakdown` como estratégia de enfrentamento e a presença de `Maus_Habitos` estão associados a maiores níveis de estresse.

### 5. Visualizações Exploratórias Avançadas

Foram geradas diversas visualizações para explorar a distribuição das variáveis e as relações entre elas, incluindo histogramas, gráficos de barras, mapas de calor de correlação e pair plots.

**Código Python:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações para melhor visualização
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

data = pd.read_csv("/home/ubuntu/upload/academicStresslevel-maintainance1.csv")

# Renomear colunas para facilitar o uso
data.rename(columns={
    'Your Academic Stage': 'Estagio_Academico',
    'Peer pressure': 'Pressao_Colegas',
    'Academic pressure from your home': 'Pressao_Academica_Casa',
    'Study Environment': 'Ambiente_Estudo',
    'What coping strategy you use as a student?': 'Estrategia_Enfrentamento',
    'Do you have any bad habits like smoking, drinking on a daily basis?': 'Maus_Habitos',
    'What would you rate the academic  competition in your student life': 'Competicao_Academica',
    'Rate your academic stress index ': 'Indice_Estresse'
}, inplace=True)

# Preencher valores ausentes na coluna 'Ambiente_Estudo' com a moda
data['Ambiente_Estudo'].fillna(data['Ambiente_Estudo'].mode()[0], inplace=True)

# 1. Histograma do Índice de Estresse
plt.figure(figsize=(8, 5))
sns.histplot(data['Indice_Estresse'], bins=5, kde=True)
plt.title('Distribuição do Índice de Estresse')
plt.xlabel('Índice de Estresse')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('indice_estresse_histogram.png')
plt.close()

# 2. Gráficos de Barras para Variáveis Categóricas vs. Índice de Estresse
categorical_cols = ['Estagio_Academico', 'Ambiente_Estudo', 'Estrategia_Enfrentamento', 'Maus_Habitos']

for col in categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=col, y='Indice_Estresse', data=data, palette='viridis', errorbar=None)
    plt.title(f'Média do Índice de Estresse por {col.replace("_", " ")}')
    plt.xlabel(col.replace("_", " "))
    plt.ylabel('Média do Índice de Estresse')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{col}_estresse_barplot.png')
    plt.close()

# 3. Mapa de Calor da Correlação
numerical_cols = ['Pressao_Colegas', 'Pressao_Academica_Casa', 'Competicao_Academica', 'Indice_Estresse']
plt.figure(figsize=(8, 7))
sns.heatmap(data[numerical_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor da Correlação entre Variáveis Numéricas')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# 4. Pair Plot para Variáveis Numéricas
sns.pairplot(data[numerical_cols])
plt.suptitle('Pair Plot das Variáveis Numéricas', y=1.02)
plt.tight_layout()
plt.savefig('numerical_pairplot.png')
plt.close()

print("Visualizações geradas e salvas como arquivos PNG.")
```

**Visualizações Geradas:**
*   `indice_estresse_histogram.png`: Histograma da distribuição do Índice de Estresse.
*   `Estagio_Academico_estresse_barplot.png`: Média do Índice de Estresse por Estágio Acadêmico.
*   `Ambiente_Estudo_estresse_barplot.png`: Média do Índice de Estresse por Ambiente de Estudo.
*   `Estrategia_Enfrentamento_estresse_barplot.png`: Média do Índice de Estresse por Estratégia de Enfrentamento.
*   `Maus_Habitos_estresse_barplot.png`: Média do Índice de Estresse por Maus Hábitos.
*   `correlation_heatmap.png`: Mapa de Calor da Correlação entre Variáveis Numéricas.
*   `numerical_pairplot.png`: Pair Plot das Variáveis Numéricas.

## Conclusão

Esta análise exploratória forneceu uma compreensão inicial dos fatores que influenciam o estresse acadêmico. As pressões externas (colegas, família, competição), o ambiente de estudo, as estratégias de enfrentamento e a presença de maus hábitos foram identificados como elementos importantes relacionados ao nível de estresse dos estudantes. Alunos do ensino médio demonstraram ser o grupo com maior vulnerabilidade ao estresse acadêmico nesta amostra.

