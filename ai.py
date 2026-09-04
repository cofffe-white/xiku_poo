def o():
    class clt:
        def __init__(self, nome):
            self.nome = nome
        def trabalhar(self):
            print(f"{self.nome} está trabalhando.")

    class dev:
        def __init__(self, nome):
            self.nome = nome
        def trabalhar(self):
            print(f'{self.nome} está desenvolvendo.')

    def ato(people):
        people.trabalhar()

    gusta = clt("Gustavo")
    edi = dev("Edi")

    ato(edi)
    ato(gusta)

#polimorfismo built-ins e operadores

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        return f'{self,nome} faz som'
class 
cão = Animal('Rex')