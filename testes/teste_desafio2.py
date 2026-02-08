from desafios.desafio2 import eh_palindromo
from testes.utils_teste import run_desafios

CASOS = [
    {"entrada": "Arara", "saida": True}, #caso 1
    {"entrada": "Jacare", "saida": False}, #caso 2
    {"entrada": "Papagaio", "saida": False}, #caso 3
    {"entrada": "A grama e amarga", "saida": True},#caso 4
    {"entrada": "Socorram-me subi no onibus em Marrocos", "saida": True}, #caso 5
    ]

def run_desafio2():
    run_desafios(CASOS, eh_palindromo)

if __name__ == "__main__":
    run_desafio2()