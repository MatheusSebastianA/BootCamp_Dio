class Animal:
    def __init__(self, num_patas) -> None:
        self.num_patas = num_patas
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join(f'{chave} = {valor}' for chave, valor in self.__dict__.items())}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

    def __str__(self) -> str:
        return "Mamífero "

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

    def __str__(self) -> str:
        return "Ave "

class Cachorro(Mamifero):
    pass

class Ornintorrinco(Mamifero, Ave):
    pass
    

car = Cachorro(cor_pelo="marrom", num_patas=4)
print(car)

orn = Ornintorrinco(num_patas=4,  cor_pelo="verde", cor_bico="marrom")
print(orn) #Irá printar o método de mamífero primero