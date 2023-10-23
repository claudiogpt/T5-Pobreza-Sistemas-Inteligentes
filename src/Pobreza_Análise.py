#!/usr/bin/env python
# coding: utf-8

# # Análise Multivariada - Pobreza  
# ##### Censo (IDH) - 2010
# - Carregando o arquivo, separando as planilhas do Excel e preparando o ambiente

# In[2]:


import pandas as pd
#Plottagem de gráficos
import seaborn as sns 
import matplotlib.pyplot as plt
#Matemática
import numpy as np

#Configurando Pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

#Arquivo Excel
df = pd.read_excel(r'C:\Users\claud\OneDrive\Área de Trabalho\Trabalho Interdisciplinar\Trabalho semestral documentos\Pobreza no Brasil\Dados para competição_V1_PauloFernando\Agregações GR.xlsx')

#Planilhas do Excel
municipios = 'Municipios'

#DataFrame por Planilha
df_mun = pd.read_excel(r'C:\Users\claud\OneDrive\Área de Trabalho\Trabalho Interdisciplinar\Trabalho semestral documentos\Pobreza no Brasil\Dados para competição_V1_PauloFernando\Agregações GR.xlsx',
                         sheet_name = municipios)


# ### Análises
# - Entendendo as variáveis alvo:
#     - qtd_0a11    
#     - qtd_0a11_pobres    
#     - qtd_0a11_vulneraveis    

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


from autoviz.AutoViz_Class import AutoViz_Class

# Inicializa o objeto AutoViz
AV = AutoViz_Class()

# Definindo as variáveis target
target_vars = ['qtd_0a11', 'qtd_0a11_pobres', 'qtd_0a11_vulneraveis']

# Loop para criar visualizações para cada variável target
for target in target_vars:
    report = AV.AutoViz(
        filename='', 
        sep=',', 
        depVar=target, 
        dfte=df_mun, 
        header=0, 
        verbose=0, 
        lowess=False, 
        chart_format='svg', 
        max_rows_analyzed=150000, 
        max_cols_analyzed=30
    )


# 
