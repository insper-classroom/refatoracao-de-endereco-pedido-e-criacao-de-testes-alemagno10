#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:
    lista = []

    def __init__(self, id='', nome=''):
        self.id = id
        self.nome = nome
        Produto.lista.append(self)

    def __str__(self):
        self.nome 
    
    def busca_nome(nome):
        resultado = []
        for produto in Produto.lista:
            if nome in produto.nome: 
                resultado.append(produto)
        return resultado

    def get_id(self):
        return self.id