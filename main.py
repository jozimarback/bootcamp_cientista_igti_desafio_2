import pymysql
import requests
import json
import pandas as pd
from repositorio import cidade, cor, estado, pessoa, tipo_sanguineo
import datetime
import numpy as np
from dateutil.relativedelta import relativedelta

url = "https://api-coleta-dados.herokuapp.com/api/pessoas"

df = pd.read_json(requests.get(url).content)
print(df.head())

# tipo_sanguineo.inserir(df['tipo_sanguineo'].unique())
# cor.inserir(df['cor'].unique())
# estado.inserir(df['estado'].unique())
estados = estado.obter()
# cidade.inserir(df.groupby(['estado', 'cidade']), estados)

df.loc[df['idade'].isnull(),'idade'] = round(( datetime.datetime.now() - pd.to_datetime(df.loc[df['idade'].isnull(),'data_nasc'], format='%d/%m/%Y')) / np.timedelta64(1, 'Y'),0)

df.loc[df['data_nasc'].str.len() < 10, 'data_nasc'] = [x[1]+'/'+str((datetime.datetime.today() - relativedelta(years=x[0])).year) for x in df.loc[df['data_nasc'].str.len() < 10, ['idade','data_nasc']].values]
#df.loc[df['data_nasc'].str.len() < 10, 'data_nasc'] = [datetime.datetime.today() - relativedelta(years=50) for ]
df['data_nasc'] = pd.to_datetime(df['data_nasc'], format="%d/%m/%Y", errors='ignore')


tipos_s = tipo_sanguineo.obter()
cores = cor.obter()
cidades = cidade.obter()
df = pd.merge(df,tipos_s,left_on='tipo_sanguineo',right_on='tipo')
df = pd.merge(df,cores,left_on='cor',right_on='cor')
df = pd.merge(df,cidades,left_on='cidade',right_on='nome_cidade')
print(df)
# TODO: converter altura e peso em float
pessoa.inserir(df)
