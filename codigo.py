from os import rename
import matplotlib.pyplot as mat
import pandas as p

t = p.read_csv('./prova.csv')

#a) Mostre as 10 primeiras entradas

print (t.head(10))

#b) Organize a base de dados em ordem alfabética por nome

t.sort_values(by=["Name"], ascending=True, inplace=True)

#c) Crie uma nova série(no mesmo dataframe) com o nome "Sobrevivente", o conteúdo deve ser "Sim" caso a coluna Survived for 1 e "Não" caso a coluna Survived for 0

t["Sobrevivente"] = t["Survived"].map({1:"sim", 0:"não"})

#d) Remova as colunas "SibSp", "Parch" e "Ticket"

t = t.drop(columns=["SibSp"])
t = t.drop(columns=["Parch"])
t = t.drop(columns=["Ticket"])

#e) Renomeie as colunas restantes para sua tradução em português

t = t.rename({"PassengerId":"Id do passageiro"}, axis="columns")
t = t.rename({"Survived":"Sobrevivent"}, axis="columns")
t = t.rename({"Pclass":"Classe do passageiro"}, axis="columns")
t = t.rename({"Name":"Nome"}, axis="columns")
t = t.rename({"Sex":"Sexo"}, axis="columns")
t = t.rename({"Age":"Idade"}, axis="columns")
t = t.rename({"Fare":"Tarifa"}, axis="columns")
t = t.rename({"Cabin":"Cabine"}, axis="columns")
t = t.rename({"Embarked":"Ebarcou"}, axis="columns")


#f) Altere os valores da coluna Sexo para: male = "masculino"(minúsculas) e female = "FEMININO"(maiúsculas)

t["Sexo"] = t["Sexo"].replace(["male"],["masculino"])
t["Sexo"] = t["Sexo"].replace(["female"],["FEMININO"])

#g) Apresente o número de sobreviventes por classe

numero_Sclasse = t.groupby(["Classe do passageiro","Sobrevivente"])["Sobrevivente"].count()
print (numero_Sclasse)

#h) Apresente o número de mortos por sexo

mortos_por_sexo = t.groupby (["Sexo","Sobrevivente"])["Sexo"].count()
print (mortos_por_sexo)

#i) Monte um gráfico(formato a sua escolha) que mostre o número de sobreviventes por classe

numero_Sclasse.plot(kind="pie")
mat.show()

#j) Exporte seu dataframe para um arquivo com extensão XLSX

t.to_excel("Prova Luiz Gabriel.xlsx", index=False, header=True)
