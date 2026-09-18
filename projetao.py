# sistema de loja

class Login:
    def __init__(self, nome="", email=""):
        self.__nome = nome
        self.__email = email

    def cadastro(self):
        self.__nome = input("Digite seu nome: ").strip()
        self.__email = input("Digite seu email: ").strip()
        if self.__nome != "" and "@" in self.__email:
            print("Cadastro concluido.")
            return self.__nome and self.__email
        else:
            print("Dados inválidos, tente novamente. \n ")
            return self.cadastro()
    

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
        return item


class Starbucks(Cardapio):
    def __init__(self):
        super().__init__("Starbucks", [
            "expresso", "capuccino", "café com leite", "café gelado", "latte com morango"
        ])


class Americanas(Cardapio):
    def __init__(self):
        super().__init__("Americanas", [
            "Fini", "Batom Garoto", "tenis", "mochila"
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
            "1": Starbucks(),
            "2": Americanas(),
            "3": Riachuelo(),
            "4": Burguer_King(),
        }

    def escolher_loja(self):
        print("Bem-vindo ao shopping!")
        print("1 - Starbucks\n2 - Americanas\n3 - Riachuelo\n4 - Burguer King")

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
    iniciar_entrega(item)


class cliente:
    def __init__(self, nome='', endereco='', telefone=''):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


class SistemaEntrega:
    def __init__(self, item=""):
        self.item = item
        self.dados_cliente = None

    def cadastrar_dados_entrega(self):
        print("      SISTEMA DE ENTREGA      ")

        while True:
            nome = input("Informe o nome do destinatário: ").strip()
            endereco = input("Informe o endereço completo de entrega: ").strip()
            telefone_texto = input("Informe o telefone para contato: ").strip()

            if nome and endereco and telefone_texto and telefone_texto.isdigit():
                telefone = int(telefone_texto)
                self.dados_cliente = cliente(nome, endereco, telefone)
                print("\n Dados de entrega cadastrados com sucesso!")
                return

            print("Todos os campos devem ser preenchidos com dados válidos. Tente novamente.\n")

    def confirmar_envio(self):
        if not self.dados_cliente:
            print("Nenhum cliente cadastrado para entrega.")
            return

        print("\n RESUMO DO ENVIO ")
        print(f"Destinatário : {self.dados_cliente.nome}")
        print(f"Pedido       : {self.item}")
        print(f"Endereço     : {self.dados_cliente.endereco}")
        print(f"Telefone     : {self.dados_cliente.telefone}")
        print("Status       : Pedido saiu para entrega com o entregador!")
        
def iniciar_entrega(item):
    entrega = SistemaEntrega(item)
    entrega.cadastrar_dados_entrega()
    entrega.confirmar_envio()


if __name__ == "__main__":
    main()