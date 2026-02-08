from desafios.desafio3 import encontrar_duplicatas
from testes.utils_teste import run_desafios

CASOS = [
    {"entrada": [1, 2, 3, 4, 2, 5], "saida": 2},
    {"entrada": [7, 7, 1, 2, 3], "saida": 7},
    {"entrada": [-1, -2, -3, -1], "saida": -1},
    {"entrada": [5, 5], "saida": 5},
    {"entrada": [1, 2, 3, 4], "saida": None},
    {"entrada": [9, 9, 9, 9], "saida": 9},
    {"entrada": [], "saida": None},
    ]

def run_desafio3():
    run_desafios(CASOS, encontrar_duplicatas)

if __name__ == "__main__":
    run_desafio3()