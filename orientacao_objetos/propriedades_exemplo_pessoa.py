class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        # Lógica para modificar o nome
        pass

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("A", 2004)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")