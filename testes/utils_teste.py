VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_AZUL = "\033[44m"

def run_desafios(CASOS, nome_funcao, s1=20):
    print(f"{FUNDO_AZUL}{'Teste':^10}{'Esperado':^{s1}}{'Resultado':^{s1}}{'Status':^10}{RESET}")
    for i, caso in enumerate(CASOS, start=1): # Percorre todos os casos
        resultado = nome_funcao(caso["entrada"])
        status = "OK" if resultado == caso["saida"] else "FAIL" # Verifica se a saida do programa é igual a saida esperada
        status_colorido = ( VERDE + status + RESET if status == "OK" else VERMELHO + status + RESET )
        print(f"{i:^10}|{str(caso['saida']):^{s1}}|{str(resultado):^{s1}}|{status_colorido}")#imprime a string formatada com cor