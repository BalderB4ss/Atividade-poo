from abc import ABC, abstractmethod
from item_biblioteca import ItemBiblioteca as ib

class Revistas(ib):
    def __init__(self, codigo, titulo, ano, disponivel, edicao, mes):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__edicao = edicao
        self.__mes = mes
    
    def exibir_detalhes(self):
        print(f"Revista -> Código: {self.__codigo} | Título: {self.__titulo} | Ano: {self.__ano}  \nEdicão: {self.__edicao} | Mês: {self.__mes} | Disponível: {self.__disponivel}")