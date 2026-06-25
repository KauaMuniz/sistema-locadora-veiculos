import os

def title(): 
    title =("\033[1;32m"'''   
██╗      ██████╗  ██████╗ █████╗ ██████╗  ██████╗ ██████╗  █████╗     ██████╗ ███████╗     ██████╗ █████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║     ██╔═══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║    ██║  ██║█████╗      ██║     ███████║██████╔╝██████╔╝██║   ██║███████╗
██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║    ██║  ██║██╔══╝      ██║     ██╔══██║██╔══██╗██╔══██╗██║   ██║╚════██║
███████╗╚██████╔╝╚██████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║    ██████╔╝███████╗    ╚██████╗██║  ██║██║  ██║██║  ██║╚██████╔╝███████║
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
 ''' "\033[0m")
    return title

def menu (): 
    menu = ("\033[1;33m"'''
            [1] CADASTRAR CARROS
            [2] LISTAR CARROS
            [3] EXCLUIR CARROS
            [4] GERAR RELATÓRIO DO CARRO
            [5] PESQUISA POR VALOR DO CARRO
            [6] ALTERAR DADO DE UM CARRO
            [7] FECHAR O PROGRAMA
           '''"\033[0m")
    return menu

def excluir_Carro():
    excluindo_carro = input("\033[0;31m""Digite o ID do carro que deseja excluir: ""\033[0m")
    linhas_novas = []
    encontrado = False

    try:
        with open("carros.txt", "r", encoding="utf-8") as arquivo:
            bloco_atual = []
            apagar_bloco = False

            for linha in arquivo:
               
                if linha.startswith("ID:"):
                   
                    if bloco_atual and not apagar_bloco:
                        linhas_novas.extend(bloco_atual)
                
                    bloco_atual = [linha]
                    apagar_bloco = linha.strip().replace(" ", "") == "ID:" + excluindo_carro
                else:
                    bloco_atual.append(linha)

            if bloco_atual and not apagar_bloco:
                linhas_novas.extend(bloco_atual)

        with open("carros.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas_novas:
                arquivo.write(linha)

        if apagar_bloco:
            print("\033[0;32m"f"✅ Carro {excluindo_carro} foi excluído com sucesso!""\033[0m")
        else:
            print("\033[0;31m""❌ Carro não encontrado.""\033[0m")

    except FileNotFoundError:
        print("\033[1;31m""Arquivo 'carros.txt' não encontrado. Verifique o caminho do arquivo.""\033[0m")


def listar_carros():
    try:
        with open("carros.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == "":
                print("\033[0;33m""⚠️ Nenhum carro cadastrado ainda.""\033[0m")
            else:
                print("\033[1;34m""\n=== LISTA DE CARROS CADASTRADOS ===\n""\033[0m")
                print(conteudo)
    except FileNotFoundError:
        print( "\033[0;31m""❌ Arquivo 'carros.txt' não encontrado. Cadastre um carro primeiro.""\033[0m")


def cadastrar_carros(opcao):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(title())

        id = input("Digite o ID único do carro: ")

        while True:
            try:
                id_verificado = int(id)
                if id_verificado < 0:
                    print("\033[0;31m""ID inválido! Não pode conter números negativos""\033[0m")
                    id = input("Digite o ID único do carro: ")
                    continue

                id_existente = False
                try:
                    with open("carros.txt", "r", encoding="utf-8") as arquivo:
                        for linha in arquivo:
                            if linha.startswith(f"ID:{id}"):
                                id_existente = True
                                break
                except FileNotFoundError:
                    pass

                if id_existente:
                    print("\033[0;31m"f"❌ O ID {id} já está cadastrado. Por favor, escolha outro ID.""\033[0m")
                    id = input("Digite o ID único do carro: ")
                    continue
                break

            except ValueError:
                print("\033[0;31m""ID inválido! Digite apenas números""\033[0m")
                id = input("Digite o ID único do carro: ")
                continue

        while True:
            try:
                modelo_car = input("Digite o modelo do carro: ")
                modelo_car_limpo = modelo_car.strip()

                if modelo_car_limpo == "":
                    raise ValueError("\033[0;33m""O campo não pode estar vazio!""\033[0m")

                if not modelo_car_limpo.replace(" ", "").isalpha():
                    raise ValueError("\033[0;33m""O modelo deve conter apenas letras!""\033[0m")

                break
            except ValueError as erro:
                print(erro)

        while True:
            try: 
                marca_car = input("Digite a marca do carro: ")
                marca_car_limpo = marca_car.strip()
                if marca_car_limpo =="":
                    raise ValueError("\033[0;33m""O campo não pode estar vazio!""\033[0m")
                
                if not marca_car_limpo.replace(" ","").isalpha():
                    raise ValueError("\033[0;33m""A marca deve conter apenas letras!""\033[0m")
                
                break
            except ValueError as erro:
                print(erro)

        while True:
            try:
                quant_dispo = input("Digite a quantidade disponível do veículo: ")
                quant_limpo = quant_dispo.strip()

                if quant_limpo == "":
                    raise ValueError("\033[0;33m""O campo não pode estar vazio!""\033[0m")

                if not quant_limpo.isdigit():
                    raise ValueError("\033[0;33m""Digite apenas números inteiros!""\033[0m")

                quant_dispo = int(quant_limpo)
                break

            except ValueError as erro:
                print(erro)
        
        while True:
            try:
                preco_hora = input("Digite o preço da hora do veículo: ")
                preco_limpo = preco_hora.strip()

                if preco_limpo == "":
                    raise ValueError("\033[0;33m""O campo não pode estar vazio!""\033[0m")
                preco_convertido = float(preco_limpo)

                if preco_convertido < 0:
                    raise ValueError("\033[0;33m""O preço não pode ser negativo!""\033[0m")
                preco_hora = preco_convertido
                break
            except ValueError:
                print("\033[0;33m""Valor inválido! Digite apenas números positivos (ex: 150 ou 150.50).""\033[0;33m")

        carro = {
            "ID":id,
            "Modelo do carro":modelo_car,
            "Marca do carro":marca_car,
            "Quantidade disponível":quant_dispo,
            "Preço da hora":preco_hora
        }

        with open("carros.txt", "a", encoding="utf-8") as arquivo:
            for chave, valor in carro.items():
                if chave == "ID":
                    arquivo.write(f"ID:{valor}\n")
                else:
                    arquivo.write(f"{chave}: {valor}\n")

            arquivo.write("-" * 40 + "\n")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[0;32m""\nCarro registrado com sucesso!\n""\033[0;33m")

        continuar = input("\033[0;33m""Deseja cadastrar outro carro? (SIM/NÃO): " "\033[0;33m").upper()
        if continuar != "SIM":
            break


def relatorio():
    id_busca = input("Digite o ID do carro: ")

    try:
        with open("carros.txt", "r", encoding="utf-8") as arquivo:
            bloco_atual = []      
            carro_encontrado = False

            for linha in arquivo:
               
                if linha.startswith("ID:"):
                    
                    if bloco_atual and bloco_atual[0].strip().replace(" ", "") == f"ID:{id_busca}":
                        carro_encontrado = True
                        break  

                    bloco_atual = [linha]
                else:
                    bloco_atual.append(linha)

            if bloco_atual and bloco_atual[0].strip().replace(" ", "") == f"ID:{id_busca}":
                carro_encontrado = True

        if carro_encontrado:
            print("\033[0;34m""\n======= RELATÓRIO DO CARRO =======\n""\033[0;33m")
            for linha in bloco_atual:
                print(linha, end="")
            print("\033[0;34m""\n==================================\n""\033[0;33m")
        else:
            print("\033[0;31m""❌ ID não encontrado.""\033[0;33m")

    except FileNotFoundError:
        print("\033[0;31m""❌ Arquivo 'carros.txt' não encontrado.""\033[0;33m")


def pesquisa_valor():
    while True:
        preco_pesquisado = input("Digite o valor exato do carro que deseja pesquisar: ").strip()
        preco_pesquisado = preco_pesquisado.replace(" ", "")

        with open("carros.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().split("-"*40)

        achou = False

        for bloco in conteudo:
            linhas = bloco.strip().split("\n")
            preco_atual = None
            for linha in linhas:
                if "Preço da hora" in linha:
                    preco_atual = linha.split(":", 1)[1].strip().replace(" ", "")
            if preco_atual == preco_pesquisado:
                achou = True
                print("\033[0;34m""\nCarro encontrado!\n""\033[0;33m")
                print(bloco.strip())
                print("\033[0;34m""----------------------------------------""\033[0;33m")

        if not achou:
            print("\033[0;33m""\nNenhum carro encontrado com esse valor!""\033[0;33m")

        continuar = input("\nDeseja pesquisar outro valor? (SIM/NÃO): ").upper()
        if continuar != "SIM":
            print("Voltando ao menu...")
            break


def alterar_carro():
    while True:
        id_alterar = input("Digite o ID do carro que deseja alterar: ").strip()

        try:
            with open("carros.txt", "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read().strip()

            if not conteudo:
                print("\033[0;33m⚠️ Nenhum carro cadastrado ainda.\033[0m")
                break

            blocos = conteudo.split("-"*40)
            blocos = [b.strip() for b in blocos if b.strip()]
            novos_blocos = []
            encontrado = False

            for bloco in blocos:
                linhas = bloco.split("\n")
                if linhas[0].strip().replace(" ", "") == f"ID:{id_alterar}":
                    encontrado = True
                    print("\n\033[0;34m=== Dados atuais do carro ===\033[0m")
                    for l in linhas:
                        print(l)
                    print("\033[0;34m=============================\033[0m\n")

                    novo_bloco = []
                    for l in linhas:
                        if l.startswith("ID:"):
                            novo_bloco.append(l)
                            continue
                        chave, valor = l.split(":", 1)
                        valor_atual = valor.strip()
                        novo_valor = input(f"{chave} (atual: {valor_atual}) → ").strip()
                        if novo_valor == "":
                            novo_bloco.append(f"{chave}: {valor_atual}")
                        else:
                            novo_bloco.append(f"{chave}: {novo_valor}")
                    novos_blocos.append("\n".join(novo_bloco))
                else:
                    novos_blocos.append(bloco)

            if not encontrado:
                print("\033[0;31m❌ ID não encontrado.\033[0m")
                resp = input("Deseja tentar outro ID? (SIM/NÃO): ").upper()
                if resp != "SIM":
                    break
                else:
                    continue

            with open("carros.txt", "w", encoding="utf-8") as arquivo:
                for b in novos_blocos:
                    arquivo.write(b + "\n" + "-"*40 + "\n")

            print("\033[0;32m✅ Carro alterado com sucesso!\033[0m\n")
            resp = input("Deseja alterar outro carro? (SIM/NÃO): ").upper()
            if resp != "SIM":
                break

        except FileNotFoundError:
            print("\033[0;31m❌ Arquivo 'carros.txt' não encontrado.\033[0m")
            break