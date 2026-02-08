from desafios.desafio4 import valida_parenteses
from testes.utils_teste import run_desafios

CASOS = [
    {"entrada": "{[()]}", "saida": True},
    {"entrada": "()", "saida": True}, #true
    {"entrada": "", "saida": True},
    {"entrada": "{[(])}", "saida": False},
    {"entrada": "(]", "saida": False},
    {"entrada": "{{[[(]]}}", "saida": False},
    {"entrada": "())", "saida": False},
]

def run_desafio4():
    run_desafios(CASOS, valida_parenteses)

if __name__ == "__main__":
    run_desafio4()