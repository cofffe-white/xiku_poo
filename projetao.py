# sistema de loja

class Login:
    def __init__(self, nome="", email=""):
        self.__nome = nome
        self.__email = email

    def cadastro(self):
        self.__nome = input("Digite seu nome: ").strip()
        self.__email = input("Digite seu email: ").strip()
        print("Cadastro concluido.")
        return self.__nome, self.__email

    def saudacao(self):
        nome = self.__nome if self.__nome else "cliente"
        print(f"Seja bem-vindo, {nome}! Acomode-se no nosso shopping Babosa.")


class Cardapio:
    def __init__(self, nome, itens):
        self.nome = nome
        self.itens = itens

    def mostrar(self):
        print(f"\nCardápio do {self.nome}:")
        for numero, item in enumerate(self.itens, start=1):
            print(f"{numero} - {item}")

        while True:
            try:
                escolha = int(input("Escolha uma opção: "))
                if 1 <= escolha <= len(self.itens):
                    return self.itens[escolha - 1]
                print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Digite apenas um número.")

    def pedir(self, item):
        print(f"Pedido recebido: {item}.")
        print("Seu pedido está a caminho. Aproveite!")


class BamBam(Cardapio):
    def __init__(self):
        super().__init__("BamBam", [
            "expresso", "capuccino", "café com leite", "café gelado", "americano"
        ])


class Americanas(Cardapio):
    def __init__(self):
        super().__init__("Americanas", [
            "camiseta", "calça", "boné", "tenis", "mochila"
        ])


class Riachuelo(Cardapio):
    def __init__(self):
        super().__init__("Riachuelo", [
            "vestido", "blusa", "saia", "jeans", "tênis"
        ])


class Burguer_King(Cardapio):
    def __init__(self):
        super().__init__("Burguer King", [
            "x-burger", "whopper", "batata frita", "refrigerante", "milkshake"
        ])


class Lojas:
    def __init__(self):
        self.lojas = {
            "1": BamBam(),
            "2": Americanas(),
            "3": Riachuelo(),
            "4": Burguer_King(),
        }

    def escolher_loja(self):
        print("Bem-vindo ao shopping!")
        print("1 - BamBam\n2 - Americanas\n3 - Riachuelo\n4 - Burguer King")

        while True:
            escolha = input("Escolha onde deseja ir: ").strip()
            if escolha in self.lojas:
                return self.lojas[escolha]
            print("Opção inválida. Escolha uma opção válida.")


def main():
    usuario = Login()
    usuario.cadastro()
    usuario.saudacao()

    loja = Lojas()
    loja_escolhida = loja.escolher_loja()
    item = loja_escolhida.mostrar()
    loja_escolhida.pedir(item)


if __name__ == "__main__":
    main()