from testes.teste_desafio2 import run_desafio2
from testes.teste_desafio3 import run_desafio3
from testes.teste_desafio4 import run_desafio4
from testes.teste_desafio5 import run_desafio5

def main_testes():

    print("Resultado dos testes do desafio 2".center(60, "="))
    run_desafio2()
    print("\n")
    print("Resultado dos testes do desafio 3".center(60, "="))
    run_desafio3()
    print("\n")
    print("Resultado dos testes do desafio 4".center(60, "="))
    run_desafio4()
    print("\n")
    print("Resultado dos testes do desafio 5".center(120, "="))
    run_desafio5()


if __name__ == "__main__":
    main_testes()