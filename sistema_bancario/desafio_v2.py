from datetime import datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_transacoes = 0
LIMITE_TRANSACOES = 10
mascara_hora_dia = "%d/%m/%Y %H:%M"

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor de depósito depositar: "))
        
        if numero_transacoes >= 10:
            print("Número máximo de transações excedido.")

        elif valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime(mascara_hora_dia)
            extrato += f"Deposito de R${valor:.2f} - {data_hora}  \n"
            numero_transacoes += 1

        else:
            print("O valor de depósito passado não é válido, escolha a operação novamente")
            

    elif opcao == "s":
        
        valor_saque = float(input("Digite o valor do saque: "))
        
        if valor_saque > limite:
            print("O valor do saque excede o limite.")
        
        elif numero_transacoes >= 10:
            print("Número máximo de transações excedido.")

        elif valor_saque > saldo:
            print("Você não tem saldo suficiente.")

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_transacoes += 1
            data_hora = datetime.now().strftime(mascara_hora_dia)
            extrato += f"Saque de R${valor_saque:.2f} - {data_hora}  \n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "e": 
        print("EXTRATO".center(40, "-"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(40, "-"))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")