import time
from unidecode import unidecode


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0  # verifica o tamanho da lista

    # tratamento de lista vazia ou nao
    def inserir(self, elemento):
        # inserção quando a lista já possui elementos
        if self.first:
            aux = self.first
            while (aux.next != None):
                aux = aux.next
            aux.next = Node(elemento)
        else:
            # primeiro insert
            self.first = Node(elemento)
        self.size = self.size + 1

    def buscar(self, elemento):
        try:
            removerAcento = unidecode(elemento.lower())
            aux = self.first
            i = 0
            while (aux != None):
                auxAcento = unidecode(aux.data.lower())
                if auxAcento == removerAcento:
                    return print(f"\nO filme procurado, '{aux.data}', se encontra na posição {i}.")
                aux = aux.next
                i = i + 1
            raise ValueError(f"{elemento} não se encontra na lista atual.")
        except ValueError as erroUsuario:
            print(f"\nERRO: {erroUsuario}")

    # removendo elemento da lista
    def remover(self, elemento):
        tratando_frase = unidecode(elemento.lower().strip())
        if self.first is None:
            raise ValueError("Lista vazia.")

        if unidecode(self.first.data.lower().strip()) == tratando_frase:
            self.first = self.first.next
            self.size -= 1
            return True
        else:
            antecessor = self.first
            aux = self.first
            encontrado = False
            while aux != None:
                if unidecode(aux.data.lower().strip()) == tratando_frase:
                    antecessor.next = aux.next
                    aux.next = None
                    encontrado = True
                    self.size -= 1
                    break
                antecessor = aux
                aux = aux.next
            if encontrado:
                return True

    # retorna o tamanho da lista
    def sizelist(self):
        return self.size

    def apontar(self, qtdfilmes):
        if self.first == None:
            print("A lista de filmes está vazia.")
            return

        this_filme = self.fElem
        display = 0
        while display < qtdfilmes:
            if this_filme != None:
                print(f"• {this_filme.data}")
                display += 1
            if this_filme == self.last:
                this_filme = self.first
            else:
                this_filme = this_filme.next

    def __repr__(self):
        string = "• "
        aux = self.first
        while (aux != None):
            string = string + str(aux.data) + "\n• "
            aux = aux.next
        return string

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    lista = LinkedList()
    #firulinha
    print("*---" * 11, end="*")
    plaquinha = '\n*\t\t\tBem vindo, usuário!\t\t\t\t* ' \
                '\n*\t\tEscolha uma das opções abaixo:\t\t*\n'
    for p in [plaquinha]:
        print(p, end="")
    print("*---" * 11, end="*")

    while(True):
        print("\n"
              "\t [1] - Adicionar filme.\n"
              "\t [2] - Remover filme.\n"
              "\t [3] - Buscar um título.\n"
              "\t [4] - Listar filmes.\n"
              "\t [5] - Imprimir coleção de filmes.\n"
              "\t [6] - Tamanho da coleção.\n"
              "\t [0] - Sair")

        opcao = int(input("-> "))

        if opcao == 1:
            elemento = input("Escreva o nome do filme: ".capitalize())
            lista.inserir(elemento)
            print("\n...Inserindo filme...\n")
            time.sleep(1)
            print(f"Filme '{elemento}' inserido com sucesso!")

        elif opcao == 2:
            elemento = input("Digite o nome do filme que deseja remover: ")
            try:
                removido = lista.remover(elemento)
                if removido:
                    print(f'\nFilme removido: {elemento}')
                else:
                    print('\nEsse filme não existe na lista atual.')
            except ValueError as erroUsuario:
                if "Lista vazia." in str(erroUsuario):
                    print('\nATENÇÃO: Lista vazia!') #lista de fato vazia

        elif opcao == 3:
            elemento = input("\nDigite o nome do filme para buscar: ")
            elemento = elemento.title()
            lista.buscar(elemento)

        elif opcao == 4:
            qtdFilmes = int(input('Quantos filmes deseja imprimir?: '))
            lista.apontar(qtdFilmes)

        elif opcao == 5:
            print(lista.__repr__())

        elif opcao == 6:
            print(f"\nA lista tem {lista.size} filme(s).")

        elif opcao == 0:
            print("*---" * 10, end="*")
            plaquinha = '\n*\t   ...Finalizando aplicação...  \t*\n'
            for p in [plaquinha]:
                print(p, end="")
            time.sleep(1)
            print("*\tObrigada por utilizar o programa! \t*")
            print("*---" * 10, end="*")
            time.sleep(1.5)
            break
        else:
            print('\nOpção inválida. Escolha uma das opções abaixo:')
