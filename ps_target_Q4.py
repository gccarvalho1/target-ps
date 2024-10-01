fat = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "OUTROS": 19849.53
}
total = 0
estados = [x for x in fat]

for estados in fat:
    total += fat[estados]


for estado, valor in fat.items():
    percentual = valor/total * 100
    print(f'{estado}: {percentual}')