from abc import ABC, abstractmethod #Biblioteca para criação de classes abstratas

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass