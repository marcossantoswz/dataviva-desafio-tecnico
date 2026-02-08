from desafios.desafio5 import manip_dados
from testes.utils_teste import run_desafios

CASOS = [
    {"entrada": [ {"categoria": "Alimentação", "valor": 10}, {"categoria": "Transporte", "valor": 5}, {"categoria": "Alimentação", "valor": 20}, {"categoria": "Lazer", "valor": 50},],
    "saida": { "Alimentação": 30, "Transporte": 5, "Lazer": 50,}},

    {"entrada": [{"categoria": "Saúde", "valor": 100},{"categoria": "Saúde", "valor": 50},],
    "saida": {"Saúde": 150,}},

    {"entrada": [{"categoria": "A", "valor": 1},{"categoria": "B", "valor": 2},{"categoria": "C", "valor": 3},],
    "saida": {"A": 1,"B": 2,"C": 3,}},

    {"entrada": [{"categoria": "Alimentação", "valor": 0},{"categoria": "Lazer", "valor": 0},],
    "saida": {"Alimentação": 0,"Lazer": 0,}},

    {"entrada": [],
    "saida": {}},
]

def run_desafio5():
    run_desafios(CASOS, manip_dados, 50)

if __name__ == "__main__":
    run_desafio5()