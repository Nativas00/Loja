import time

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidade:
            self.quantidade -= quantidade_vendida
            return True
        return False

class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, produto, quantidade):
        if produto.nome in self.itens:
            self.itens[produto.nome]["quantidade"] += quantidade
        else:
            self.itens[produto.nome] = {"produto": produto, "quantidade": quantidade}

    def remover_item(self, nome_produto, quantidade):
        if nome_produto in self.itens:
            if self.itens[nome_produto]["quantidade"] > quantidade:
                self.itens[nome_produto]["quantidade"] -= quantidade
            else:
                del self.itens[nome_produto]

    def calcular_total(self):
        return sum(item["produto"].preco * item["quantidade"] for item in self.itens.values())

class Loja:
    def __init__(self):
        self.estoque = [
            Produto("No place for Bravery", 44.90, 5),
            Produto("Enigma do Medo", 49.90, 2),
            Produto("Who needs a Hero?", 14.90, 15),
            Produto("Hazel Sky", 39.90, 10),
        ]
        self.carrinho = Carrinho()

    def mostrar_estoque(self):
        print("\nEstoque disponivel:")
        for idx, produto in enumerate(self.estoque, 1):
            print(f"{idx}. {produto.nome} - R${produto.preco:.2f} - {produto.quantidade} unidades")
        time.sleep(2)

    def adicionar_ao_carrinho(self):
        self.mostrar_estoque()
        try:
            escolha = int(input("\nDigite o numero do jogo que quer adicionar: ")) - 1
            if 0 <= escolha < len(self.estoque):
                quantidade = int(input("Digite a quantidade: "))
                if quantidade > 0:
                    produto = self.estoque[escolha]
                    if produto.quantidade >= quantidade:
                        self.carrinho.adicionar_item(produto, quantidade)
                        print(f"{quantidade} {produto.nome}(s) adicionado(s) ao carrinho!")
                        time.sleep(1)
                    else:
                        print("Quantidade indisponivel em estoque.")
                        time.sleep(1)
                else:
                    print("Quantidade invalida.")
                    time.sleep(1)
            else:
                print("Produto não encontrado.")
                time.sleep(1)
        except ValueError:
            print("Opcao invalida.")

    def remover_do_carrinho(self):
        if not self.carrinho.itens:
            print("Carrinho vazio.")
            return

        print("\nItens no carrinho:")
        for idx, (nome, item) in enumerate(self.carrinho.itens.items(), 1):
            print(f"{idx}. {nome} - {item["quantidade"]} unidades")

        try:
            escolha = int(input("\nDigite o numero do item para remover: ")) - 1
            if 0 <= escolha < len(self.carrinho.itens):
                nome = list(self.carrinho.itens.keys())[escolha]
                quantidade = int(input("Digite a quantidade para remover: "))
                if quantidade > 0:
                    self.carrinho.remover_item(nome, quantidade)
                    print(f"{quantidade} {nome}(s) removido(s) do carrinho!")
                    time.sleep(1)
                else:
                    print("Quantidade invalida.")
                    time.sleep(1)
            else:
                print("Opcao invalida.")
                time.sleep(1)
        except ValueError:
            print("Opcao invalida.")
            time.sleep(1)

    def ver_carrinho(self):
        if not self.carrinho.itens:
            print("Carrinho vazio.")
            return

        print("\nItens no carrinho:")
        total = 0
        for nome, item in self.carrinho.itens.items():
            subtotal = item["produto"].preco * item["quantidade"]
            print(f"{nome} - {item["quantidade"]} unidades - R${subtotal:.2f}")
            total += subtotal

        print(f"\nTotal: R${total:.2f}")
        time.sleep(1)

    def finalizar_compra(self):
        if not self.carrinho.itens:
            print("Carrinho vazio.")
            return

        total = self.carrinho.calcular_total()
        print(f"\nTotal da compra: R${total:.2f}")
        time.sleep(1)

        print("\nFormas de pagamento:")
        print("1. Pix (10% de desconto)")
        print("2. Cartão de debito (sem desconto)")
        print("3. Cartão de credito (acrescimo de 5% para parcelamento)")

        try:
            opcao = int(input("\nEscolha a forma de pagamento: "))
            if opcao == 1:
                total *= 0.9
                print(f"Total com desconto: R${total:.2f}")
                time.sleep(1)
            elif opcao == 2:
                print(f"Total a pagar: R${total:.2f}")
                time.sleep(1)
            elif opcao == 3:
                parcelas = int(input("Numero de parcelas (1-12): "))
                time.sleep(1)
                if 1 <= parcelas <= 12:
                    if parcelas > 1:
                        total *= 1.05
                    print(f"Total a pagar: R${total:.2f} em {parcelas}x de R${total/parcelas:.2f}")
                else:
                    print("Numero de parcelas invalidas, retornando ao menu principal.")
                    return
            else:
                print("Opcao invalida.")
                return

            confirmacao = input("\nConfirmar compra? (Y/N): ").upper()
            if confirmacao == "Y":
                for item in self.carrinho.itens.values():
                    item['produto'].atualizar_estoque(item['quantidade'])
                self.carrinho = Carrinho()
                print("\nCompra finalizada com sucesso!")
                time.sleep(1)
            elif confirmacao == "N":
                print("\nRetornando ao menu principal.")
                time.sleep(1)
            else:
                print("\nOpcao invalida.")
                time.sleep(1)
        except ValueError:
            print("Opcao invalida.")
            time.sleep(1)

    def menu(self):
        while True:
            print("\n=== MENU DA LOJA DE JOGOS BRASILEIROS ===")
            print("1. Ver o catalogo")
            print("2. Adicionar um jogo ao carrinho")
            print("3. Remover um jogo do carrinho")
            print("4. Ver carrinho")
            print("5. Finalizar compra")
            print("6. Sair")

            try:
                opcao = int(input("\nEscolha uma opcao: "))
                if opcao == 1:
                    self.mostrar_estoque()
                elif opcao == 2:
                    self.adicionar_ao_carrinho()
                elif opcao == 3:
                    self.remover_do_carrinho()
                elif opcao == 4:
                    self.ver_carrinho()
                elif opcao == 5:
                    self.finalizar_compra()
                elif opcao == 6:
                    print("\nObrigado por investir em projetos brasileiros!")
                    time.sleep(0.5)
                    print("Ate breve.")
                    break
                else:
                    print("Opcao invalida.")
                    time.sleep(1)
            except ValueError:
                print("Entrada invalida.")
                time.sleep(1)


if __name__ == "__main__":
    loja = Loja()
    loja.menu()
