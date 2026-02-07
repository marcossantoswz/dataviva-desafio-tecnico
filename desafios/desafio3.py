"""
Retorna o primeiro elemento duplicado da lista e none se não tiver nenhum
A função percorre a lista e utiliza um conjunto set para registrar os valores ja vistos
"""
def encontrarDuplicatas(lista):
    vistos=set()
    for x in lista:
        if x in vistos:
            return x
        vistos.add(x)


if __name__ == "__main__":
    ver=encontrarDuplicatas([1, 2, 3, 4, 21, 5, 9])
    print(ver)