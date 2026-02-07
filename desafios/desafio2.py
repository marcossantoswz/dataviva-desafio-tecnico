"""
A entrada é padronizada por meio da remoção de espaços e hífens, além da conversão das letras para minúsculas.
A verificação compara somente a primeira metade da palavra
retornando False ao encontrar a primeira discrepância e true caso não encontre nenhuma diferença
"""

def ehPalindromo(palavra):
    palavra = palavra.replace(" ", "").replace("-", "").lower()
    meio = len(palavra) // 2
    for i in range(meio):
        if palavra[i] != palavra[-(i+1)]:
            return False
        
    return True

if __name__ == "__main__":
    ver=ehPalindromo("Araraaaaaaa")
    print(ver)