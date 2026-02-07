"""
Retorna o primeiro elemento duplicado da lista e none se não tiver nenhum
A função percorre a lista e utiliza um conjunto set para registrar os valores ja vistos
"""
def encontrar_duplicatas(lista):
    vistos=set()
    for x in lista:
        if x in vistos:
            return x
        vistos.add(x)
