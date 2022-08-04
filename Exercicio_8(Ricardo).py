import pandas as pd

x = pd.read_csv("Notas_alunos.csv")
print(x)


# Calculo da média
x['media'] = (x['Nota_1'] + x['Nota_2']) / 2
x['situacao'] = ""
faltas = x['faltas'] 


# Veririficar se média aprova ou reprova
x.loc[x["media"] < 7, "situacao" or x["faltas">3]] = "Reprovado" 

x.loc[x["media"] >= 7, "situacao"] = "Aprovado" 


print(x)


