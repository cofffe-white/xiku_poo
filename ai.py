'''def o():
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
        return f'{self.nome} faz som'
    def andar(self):
        return f'{self.nome} está andando'
cão = Animal('Rex')

print(cão.falar())
print(cão.andar())'''
def a():
    class veiculo:
        def __init__(self, nome):
            self.nome = nome

        def acelerar(self):
            return f"{self.nome} está acelerando"

    class carro(veiculo):
        def acelerar(self):
            return f"{self.nome} está acelerando como um carro"

    class moto(veiculo):
        def acelerar(self):
            return f"{self.nome} está acelerando como uma moto"

    class aviao(veiculo):
        def acelerar(self):
            return f"{self.nome} está acelerando como um avião"

    def ato(runrun):
        runrun.acelerar()

    fusca = carro("Fusca")
    honda = moto('honda')
    azul = aviao('azul')

    ato(fusca)
    ato(honda)
    ato(azul)
a()