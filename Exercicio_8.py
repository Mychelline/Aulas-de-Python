import pandas as pd
import numpy as np

df = pd.read_csv("Notas_alunos.csv")

#Calculo da média 
df["Media"] = (df["Nota_1"] + df["Nota_2"])/2

print(df.head()) 



df.to_csv('alunos_situacao.csv')

numeroFaltas = df['Faltas'].max()
print("Maior número faltas: " +str(numeroFaltas))
mediaGeral = df['Media'].median()
print("Média geral das notas: " +str(mediaGeral))
maiorMedia = df['Media'].max()
print("Maior média: " + str(maiorMedia))