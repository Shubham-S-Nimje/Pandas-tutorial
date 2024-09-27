import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

# poke = pd.read_excel('pokemon_data.xlsx')

# poke = pd.read_csv('pokemon_data.txt')

# print(poke.tail(4))

# print(poke.aggregate)

# print(poke.columns)

# print(poke[['Name', 'Type 1']][0:5])

# print(poke.iloc[3,2])

# print(poke.sort_values(['Name']))

# poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']

# poke = poke.drop(columns=['Total'])

# print(poke.head(5))

# poke['Total'] = poke.iloc[:, 4:10].sum(axis=1)

cols = list(poke.columns)
poke = poke[cols[0:4] + [cols[-1]]+cols[4:12]]

print(poke.head(5))