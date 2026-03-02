from abc import ABC, abstractmethod

class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Código: {self.__codigo} | Título: {self.__titulo} | Ano: {self.__ano} | Disponível: {self.__disponivel}")

    def set_emprestar(self):
        if self.__disponivel == True:
            print(f"O item {self.__titulo} foi emprestado com sucesso!")
            self.__disponivel = False
        print(f"O item {self.__titulo} não está disponível❌")

    def set_devolver(self):
        if self.__disponivel == False:
            print(f"O item {self.__titulo} foi devolvido com sucesso!")
            self.__disponivel = True
        print(f"O item {self.__titulo} ainda está pendente")