'''
=================================
Exemplo de herança
class A:
    pass
    
class B(A):
    pass
    
==================================
Exemplo de herança múltipla

class A:
    pass

class B:
    pass


class C(A, B):
    pass
==================================
'''

class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def verificar_carga(self):
        print(f"{'Eu' if self.carregado else 'Não'} estou carregado!")

moto1 = Motocicleta("a", "123a", 2)

carro1 = Carro("b", "123b", 4)

caminhao1 = Caminhao("c", "123c", "8", False)

caminhao1.verificar_carga()