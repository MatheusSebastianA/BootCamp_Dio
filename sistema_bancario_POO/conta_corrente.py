from conta import Conta

class ContaCorrente(Conta):
    def __init__(self,  numero, cliente, limite=1500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])

        if valor > self.limite:
            print("Você ultrapassou o limite do valor de saque. ")
            return False

        elif numero_saques >= self.limite_saques:
            print("Você ultrapassou a quantidade limite de saques diários. ")
            return False
        
        else:
            return super().sacar(valor)
        
    def __str__(self):
        return f"""\
Agência:    {self.agencia}
C/C:        {self.numero}
Titular     {self.cliente.nome}
        """
         