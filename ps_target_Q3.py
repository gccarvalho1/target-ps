import json

#EM STRING

json_string = """
[
{
    "dia" : "01/10/2024",
    "valor": 40600
},
{
    "dia" : "02/10/2024",
    "valor": 35600
},
{
    "dia" : "03/10/2024",
    "valor": 38630
},
{
    "dia" : "04/10/2024",
    "valor": 35000
},
{
    "dia" : "05/10/2024",
    "valor": 0
}
]
"""
dados_json_string = json.loads(json_string)


#abrindo caminho

with open('dados.json') as jss:
    dados_json_normal = json.load(jss)

#Utilizarei o json_string


def calcula_media(dados):
    menor_fat = 0
    maior_fat = 0
    faturamento = 0
    dias_fat = 0
    for x in dados:
        valor = x['valor']

        if valor > 0:
            if menor_fat == 0 or valor < menor_fat:
                menor_fat = valor
            if maior_fat == 0 or valor > maior_fat:
                maior_fat = valor
            faturamento += valor
            dias_fat += 1
    calcula_med = faturamento/dias_fat

    dia_acima = 0
    for x in dados:
        valor = x['valor']
        if valor > 0 and valor > calcula_med:
            dia_acima += 1
    
    return menor_fat, maior_fat, dia_acima

    

menor, maior, dias = calcula_media(dados_json_string)

print(f'Menor faturamento: {menor}')
print(f'Maior faturamento: {maior}')
print(f'Dias acima da media: {dias}')