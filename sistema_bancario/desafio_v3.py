def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta
    [l] Listar contas
    [q] Sair

    => """
    return input(menu)
    
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de R${valor:.2f}\n"

    else:
        print("O valor de depósito passado não é válido, escolha a operação novamente")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
            print("O valor do saque excede o limite.")
        
    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido.")

    elif valor > saldo:
        print("Você não tem saldo suficiente.")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque de R${valor:.2f}\n"

    else:
        print("O valor informado é inválido.")
        
    return saldo, extrato

def mostra_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(40, "-"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(40, "-"))

    return 

def filtar_usuario(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe apenas os números do CPF:")
    usuario = filtar_usuario(usuarios, cpf)

    if usuario:
        print("Esse usuário já existe")
        return
    
    nome = input("Informe o nome completo: ")
    data_nas = input("Informe a data de nascimento no formato dd--mm--aaaa: ")
    end = input("Informe o endereço no formato logadoura, numero, bairro, cidade/estado: ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nas,
        "cpf": cpf,
        "endereço": end,
    })
    print("Usuário criado com sucesso")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe apenas os números do CPF do usuário:")
    usuario = filtar_usuario(usuarios, cpf)

    if usuario:
        print("Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    
    print("Usuário não encontrado, a conta não pôde ser criada")

def listar_contas(contas):
    if not contas:
        print("Não há contas criadas até o momento, seja o primeiro a criá-la") 
    for conta in contas:
        linha = f"""
Agência:         {conta["agencia"]}
Número da conta: {conta["numero_conta"]}
Titular:         {conta["usuario"]["nome"]}
        """
        print("-"*50)
        print(linha)
    ...

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    numero_conta = 1
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor de depósito depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            

        elif opcao == "s":
            valor_saque = float(input("Digite o valor do saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques = numero_saques, limite_saques=LIMITE_SAQUES)
            
        elif opcao == "e":
            mostra_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)
        
        elif opcao == "c":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
                
            

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
    
    
    
    return

if __name__ == '__main__':
    main()