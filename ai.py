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

import time
class Restaurante:
    def __init__(self, nome, itens):
        self.nome = nome
        self.itens = itens

    def cardapio(self):
        print(f"\nCardápio do {self.nome}:")
        for numero, item in enumerate(self.itens, start=1):
            print(f"{numero} - {item}")

        while True:
            try:
                escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print("Digite apenas um número.")
                continue

            if 1 <= escolha <= len(self.itens):
                return self.itens[escolha - 1]
            print("Opção inválida. Tente novamente.")
            
    def pedir(self, item):
        print(f"Pedido recebido: {item}.")
        time.sleep(5)
        print("Seu pedido está a caminho. Aproveite!")


class Cafeteria(Restaurante):
    def __init__(self):
        super().__init__("cafeteria", [
            "expresso", "capuccino", "café com leite", "café gelado", "americano"
        ])


class Acaiteria(Restaurante):
    def __init__(self):
        super().__init__("açaíteria", [
            "açaí com granola", "açaí com banana", "açaí com morango",
            "açaí com leite condensado", "açaí com chocolate"
        ])


class Quiosque(Restaurante):
    def __init__(self):
        super().__init__("quiosque", [
            "sorvete", "picolé", "batata frita", "cachorro-quente", "hambúrguer"
        ])


def escolher_restaurante():
    restaurantes = {
        "1": Cafeteria(),
        "2": Acaiteria(),
        "3": Quiosque(),
    }

    print("Bem-vindo ao restaurante!")
    print("1 - Cafeteria\n2 - Açaíteria\n3 - Quiosque")
    while True:
        escolha = input("Escolha onde deseja ir: ").strip()
        if escolha in restaurantes:
            return restaurantes[escolha]
        print("Opção inválida. Escolha 1, 2 ou 3.")



restaurante = escolher_restaurante()
item = restaurante.cardapio()
restaurante.pedir(item)