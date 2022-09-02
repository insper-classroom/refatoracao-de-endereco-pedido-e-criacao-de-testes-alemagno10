#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    lista_pessoas = []

    def __init__(self,nome,email,cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas.append(self)

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco]=end

    def remover_endereco(self, apelido_endereco):
        pass

    def get_endereco(self, apelido_endereco):
        if apelido_endereco in self.__enderecos:
            return self.__enderecos[apelido_endereco].rua
    
    def busca_nome(nome):
        resultado = []
        for pessoa in PessoaFisica.lista_pessoas:
            if nome.lower() in pessoa.nome.lower():
                resultado.append(pessoa)
        return resultado


    def listar_enderecos(self):
        return self.__enderecos
    
    # escolher o estilo de retorno
    def __str__(self):
        return self.nome
    
    
    