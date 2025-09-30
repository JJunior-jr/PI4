#%%
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder



# %%
##pd.read_csv('C:\Users\Junior\documents\03-Univesp\01-PI4\PI4\data\academic Stress level - maintainance 1.csv')

df=pd.read_csv(r'PI4\data\academic Stress level - maintainance 1.csv',sep=',')
df.head()
# %%
df
# %%
