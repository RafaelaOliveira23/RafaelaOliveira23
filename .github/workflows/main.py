menu = '''


[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opção = input(menu)

    if opção == "1": # Colocar na lista extrato todo o valor informado no deposito.
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor informado é inválido, favor tente novamente.")

           
    
    if opção == "2": # Preciso verificar se o numero_saque é menor de 3, verificar se tem saldo suficiente para a operação e 
        valor = float(input("Informe o valor desejado de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação inválida, saldo insuficiente.")
        elif excedeu_limite:
            print("Operação inválida, o limite foi excedido.")
        elif excedeu_saque:
            print("Operação inválida, número de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação inválida, valor informado é inválido!")

    elif opção == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")


    elif opção == "4":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
