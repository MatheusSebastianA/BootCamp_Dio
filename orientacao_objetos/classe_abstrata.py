from abc import ABC, abstractmethod #Biblioteca para criação de classes abstratas

class ControleRemoto:
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando......")

    def desligar(self):
        print("Desligando")

class ControleAr(ControleRemoto):
    def ligar(self):
        print("Ligando Ar")

    def desligar(self):
        print("Desligando Ar")

controle = ControleTv()
controle.ligar()
controle.desligar()