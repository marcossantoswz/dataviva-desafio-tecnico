
"""
Imprime os numeros de 1 a 100
Para multiplos de 3 imprime 'Fizz' e multiplos de 5 imprime 'Buzz'
E para multiplos de 15 (multiplos de 3 e 5 ao mesmo tempo) imprime 'FizzBuzz' evitando comparações desnecessarias
"""
def FizzBuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    FizzBuzz()