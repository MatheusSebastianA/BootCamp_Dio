from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nas, cpf, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nas = data_nas