menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a letra correspondente ao que você deseja: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:

    opcao = input(menu)

    if opcao == "d":
        print("""
    ---Deposito---
              """)
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"O valor do seu deposito foi: R$ {valor:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "s":
        print("""
    ---Saque---
              """)
        valor = float(input("Digite o valor do seu saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! Excedeu o limite de R$ 500.")

        elif excedeu_saques:
            print("Operação falhou! Limite de saques atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n################ EXTRATO ################")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:2.f}")
        print("###########################################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")