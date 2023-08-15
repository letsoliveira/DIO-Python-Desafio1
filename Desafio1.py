boas_vindas = "Seja Bem-vindo(a)! Escolha a opção desejada:"
menu = f"""
## {boas_vindas} ##
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""
saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Digite o valor do depósito:")
        valor = float(input())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == 2:
        print("Digite o valor do saque:")
        valor = float(input())
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente. Tente novamente.")

        elif excedeu_limite:
            print("Limite do valor de saque excedido. Tente novamente.")

        elif excedeu_saques:
            print("Limite de saque diário excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == 3:
        print("## EXTRATO ##\n")
        print("Extrato vazio." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
