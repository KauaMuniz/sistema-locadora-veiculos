import os
from funcoes import *

while True:  # Loop principal
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title())
    print(menu())

    condicao = input("\033[1;37mDigite a opção desejada: \033[0m")

    if condicao == "1":
        cadastrar_carros(condicao)
    elif condicao == "2":
        listar_carros()
    elif condicao == "3":
        excluir_Carro()
    elif condicao == "4":
        relatorio()
    elif condicao == "5":
        pesquisa_valor()
    elif condicao == "6":
        alterar_carro()
    elif condicao == "7":
        print("Programa finalizado.")
        break
    else:
        print("\033[0;31mOpção inválida.\033[0m")
    recomecar = input("Deseja voltar ao menu? (SIM/NÃO): ").upper()
    if recomecar != "SIM":
        print("Programa finalizado.")
        break