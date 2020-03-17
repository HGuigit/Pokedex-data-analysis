import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import operator

df = pd.read_csv("Pandas/pokemon_data.csv")
#print(df.head(n=6))
#print(df.columns)

##Ler cada coluna
#print(df[['Name','Type 1','HP']][0:45])

##Ler cada linha
#print(df.iloc[1:6])
#print(df.iloc[2])

##Ler uma localização específica
#Venusaur = df[df['Name'] == 'Venusaur']
#print(df.iloc[2,1])#row,collum
#new_df = df.loc[df["Type 1"] == "Fire"]

#print(new_df.sort_values( ['Attack'], ascending = [0]))#Localizar nome na coluna
#print(df.loc[df['Name'] == 'Talonflame'])
#print(df.loc[df['Name'] == 'Ash-Greninja'])
#print(df.loc[df['Name'] == 'Absol'])
#print(df.loc[df["Type 1"] == 'Grass'])
#print(df.loc[df["HP"].idxmin()])
#print(df.loc[df["HP"].idxmax()])
#print(df.sort_values('Name', ascending = 'False'))
#print(df.sort_values(['Type 2','HP'], ascending = [0,1]))
#print(df.sort_values(['Type 1','HP'], ascending = [1,0])[0:60])#Tipo em ordem alfabética e hp decrescente
#print(df.sort_values(['Name'], ascending = True)[0:50])



#Ler tudo
#for index, row in df.iterrows():
    #print(index, row)
    #print(index, row['Name'])
    #if row['Name'] == 'Charmander':
        #print(index)
    
#Nova Coluna

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df.sort_values('Total', ascending = False)[0:60])
#df = df.drop(columns='Total')#Tirar coluna
df['Total'] = df.iloc[:, 4:10].sum(axis=1)#iloc > [rows , columns]  axis> 0 = row, 1 = column
cols = list(df.columns.values)
#print(cols)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]#Troca a coluna Total de lugar
#print(df.sort_values('Total', ascending = False)[0:60])
#rint(df)
#df.to_csv('Modified_poke.csv', index = False)#Index tira numeração do pandas
#df.to_excel('Modified_poke.xlsx', index = False)
#df.to_csv('Modified_poke.txt', index = False, sep = '\t')

#new_df = df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Psychic') & (df['HP'] > 50)]
#new_df = df.loc[(df['Type 1'] == 'Ghost') & (df['Type 2'] == 'Poison') & (df['HP'] > 50)]
#new_df = df.loc[(df['Type 1'] == 'Water') & (df['Type 2'] == 'Rock') & (df['HP'] > 50)]
#new_df = new_df.reset_index(drop = True)#Resetar numeração, drop n salver index antiga
#new_df = df.loc[df['Name'].str.contains('Mega')]#Achar todos os pokemons com a str "mega"
#new_df = df.loc[~df['Name'].str.contains('Mega')]#Achar todos os pokemons sem a str 'mega'~< negação
#new_df = df.loc[df['Type 1'].str.contains('Fire|Grass', flags = re.I, regex = True)]#Flag tira o case sensitive da letra maiuscula
#new_df = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex = True)]
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'#acha os fire na coluna type 1 e modifica para flamer
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True #acha os Fire na coluna type 1 e modifica seu legendary para True
df['Good'] = False
df['Average'] = False
df['Fantastic'] = False
df['Ok'] = False
cols2 = list(df.columns.values)
df = df[cols2[0:13] + [cols2[-1]] + [cols2[-3]] + [cols2[-4]] + [cols2[-2]]]
df.loc[(df['Total'] > 500) & (df['Total'] < 600), 'Good'] = True
df.loc[df['Total'] >= 600, 'Fantastic'] = 'True'
df.loc[(df['Total'] > 300) & (df['Total'] <= 500), 'Average'] = 'True'
df.loc[(df['Total'] >= 0) & (df['Total'] <= 300), 'Ok'] = 'True'

#print(df.sort_values('Total', ascending = False).head(n=50))
#Groupby
new_df = df.groupby(['Type 1']).mean()
#print(new_df)

new_df = new_df.sort_values('Attack', ascending=True)

#types = pd.unique(df['Type 1']) #Retorna uma lista com cada tipo sem repetição.
types = list(new_df.index.values)
#Attack = dict(new_df['Attack'])#não funciona para meu propósito

Attack = list(new_df['Attack'])

#print(new_df)

#sorted_attack = sorted(Attack.items(), key=operator.itemgetter(1)) #lista de tuplas

#print(Attack)
#print(types)

plt.bar(types, Attack)
plt.title('Pokemon Attack, Type sorted.')
plt.show()