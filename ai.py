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


class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        return f"{self.nome} está acelerando"


class Carro(Veiculo):
    def acelerar(self):
        return f"{self.nome} está acelerando como um carro"


class Moto(Veiculo):
    def acelerar(self):
        return f"{self.nome} está acelerando como uma moto"


class Aviao(Veiculo):
    def acelerar(self):
        return f"{self.nome} está acelerando como um avião"

def executar(veiculo):
    return veiculo.acelerar()

fusca = Carro("Fusca")
honda = Moto("Honda")
azul = Aviao("Azul")  
     
class comida:
    def __init__(self,nome):
            self.nome = nome
    def comer(self):
            return f"{self.nome} está sendo devorada"

class pera(comida):
    def comer(self):
            return f"{self.nome} está sendo devorada como uma pera"
class maca(comida):
    def comer(self):
            return f"{self.nome} está sendo devorada como uma maçã"
class banana(comida):
    def comer(self):
            return f"{self.nome} está sendo devorada como uma banana"
        
def ato(fruta):
        return fruta.comer()
maca = maca("Maçã")
banana = banana("Banana")
pera = pera("Pera")
    
print(f"{ato(maca)},\n {ato(banana)},\n {ato(pera)}")
