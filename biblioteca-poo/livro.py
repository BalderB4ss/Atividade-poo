from abc import ABC, abstractmethod
from item_biblioteca import ItemBiblioteca as ib

class Livro(ib):
    def __init__(self, codigo, titulo, ano, disponivel, autor, num_paginas):
        super().__init__(codigo, titulo, ano, disponivel)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        print("Livro")
        super().exibir_detalhes()
        print(f"Livro Autor: {self.__autor} | Número de paginas: {self.__num_paginas}")
              