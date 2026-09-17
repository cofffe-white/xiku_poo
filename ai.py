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
     
#restaurante
import time

class restaurante:
    def __init__(self,nome):
        
        self.nome = nome
        
    def pedir(self):
        print("seu pedido está a caminho")
        
    def time(self):
        time.sleep(10)
        print("seu pedido chegou. Aproveite!")
        
class cafeteria(restaurante):
    
    def pedir(self):
            print("seu pedido está a caminho")
            
    def time(self):
        time.sleep(10)
        print("seu pedido chegou. Aproveite!")
            
    def cardapio(self):
        e = input('bem-vindo ao cardápio da cafeteria:\n1-expresso\n2-capuccino\n3-café com leite\n4-café gelado\n5-americano. \nDigite o que deseja:\n ')
            
class acaiteria(restaurante):
    
    def pedir(self):
        print("seu pedido está a caminho")
        
    def time(self):
        time.sleep(10)
        print("seu pedido chegou. Aproveite!")
        
    def cardapio(self):
        s = input('bem-vindo ao cardápio da acaiteria,:\n1-acai com granola\n2-acai com banana\n3-acai com morango\n4-acai com leite condensado\n5-acai com chocolate. \nDigite o que deseja:\n ')
                
class quiosque(restaurante):
    
    def pedir(self):
        print("seu pedido está a caminho")
    
    def time(self):    
        time.sleep(10)
        print("seu pedido chegou. Aproveite!")
    
    def cardapio(self):
        c = input('bem-vindo ao cardápio do quiosque,:\n1-sorvete\n2-picolé\n3-batata frita\n4-cachorro quente\n5-hamburguer. \nDigite o que deseja:\n')
                
        
def ato(pedido):
        return pedido.pedir()
    
def acao(esc):
    return esc.cardapio()

def car(dapio):
    return dapio.time()
    
cafe1 = cafeteria('thalita paes')
acai1 = acaiteria('lemania')
quio1 = quiosque('comebem')

p = input('bem-vindo ao restaurante, qual deseja ir?\n1-cafeteria\n2-acaiteria\n3-quiosque\nDigite o que deseja:\n')
p = int(p)

if p == 1:
    print(acao(cafe1))
    print(ato(cafe1))
    print(car(cafe1))
elif p == 2:
    print(acao(acai1))
    print(ato(acai1))
    print(car(acai1))
elif p ==3:
    print(acao(quio1))
    print(ato(quio1))
    print(car(quio1))
else:
    print('opção inválida')