'''
cria um dicionario vazio do resultado final, itera
sobre a lista de dicionarios e soma os valores por categoria
Retorna o dicionario com o resultado final
'''

def manip_dados(dados):
    resultado = {}
    for dicionario in dados:
        if dicionario["categoria"] not in resultado:
            resultado[dicionario["categoria"]] = dicionario["valor"]
        else:
            resultado[dicionario["categoria"]] += dicionario["valor"]
    return resultado