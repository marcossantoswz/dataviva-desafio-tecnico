'''
Retorna true se a string for valida e false se for invalida
Usa uma pilha no estilo LIFO para empilhar e desempilhar os caracteres
o ultimo caracterer a entrar deve ser o primeiro a sair
'''

def valida_parenteses(caracteres):
    pilha = []

    pares = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for c in caracteres:
        if c in '([{':
            pilha.append(c)
        elif c in ')]}':
            if not pilha or pilha[-1] != pares[c]:
                return False
            pilha.pop()
        
    return True if not pilha else False