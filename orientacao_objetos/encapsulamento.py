class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo #_ significa que o atributo é privado, mas ainda sim pode ser manipulado publicamente, o que seria errado

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def exibir_saldo(self):
        print(f"Valor do saldo: {self._saldo}")

conta = Conta(100)
#conta._saldo += 1000000 -> Não dará erro, mas não é corretor manipular esse atributo fora da classe
conta.depositar(100)
conta.sacar(50)
conta.exibir_saldo()
        