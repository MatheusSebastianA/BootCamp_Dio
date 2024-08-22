class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("Latindo...")

    #Sempre será executado na destruição da classe
    def __del__(self):
        print(f"Removendo o cachorro {self.nome} da classe {self.__class__.__name__}")

c1 = Cachorro("Husky", "branco")
c2 = Cachorro("Salsicha", "marrom")
del c1
print("Objeto c1 já foi deletado de forma forçada")
c2.falar()