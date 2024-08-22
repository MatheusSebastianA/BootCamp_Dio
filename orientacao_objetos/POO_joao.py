#Código para Programação orientada a objetos
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Buzinando")

    def parar(self):
        print("Parando a bicicleta") 

    def correr(self):
        print("Correndo com a bicicleta")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "BMX", 1998, 69.69 )
b1.buzinar()
b1.correr()
b1.parar()
print(b1)