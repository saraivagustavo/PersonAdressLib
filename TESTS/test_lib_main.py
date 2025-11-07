from PALib.models.models import *
from PALib.models.dto import *

import pytest

def createPerson():
    pessoa = PessoaCreate(
        nome="Gustavo Saraiva",
        idade=20,
        email="gustavosaraiva@email.com"
    )

    assert pessoa.nome == "Gustavo Saraiva"
    assert pessoa.idade == 20
    assert pessoa.email == "gustavosaraiva@email.com"

def createAddress():
    endereco = EnderecoCreate(
        logradouro="Rua do Teste",
        numero=123,
        estado="ES",
        cidade="Vila Velha",
        bairro="TestesPython",
        id_pessoa=1
    )

    assert endereco.logradouro == "Rua do Teste"
    assert endereco.numero == 123
    assert endereco.estado == "ES"
    assert endereco.cidade == "Vila Velha"
    assert endereco.bairro == "TestesPython"
    assert endereco.id_pessoa == 1

def testeEnderecoUpdate():
    endereco_update = EnderecoUpdate(
        logradouro="Rua Atualizada",
        numero=456,
        estado="RJ",
        cidade="Rio de Janeiro",
        bairro="AtualizacoesPython",
        id_pessoa=2
    )

    assert endereco_update.logradouro == "Rua Atualizada"
    assert endereco_update.numero == 456
    assert endereco_update.estado == "RJ"
    assert endereco_update.cidade == "Rio de Janeiro"
    assert endereco_update.bairro == "AtualizacoesPython"
    assert endereco_update.id_pessoa == 2

def testePessoaUpdate():
    pessoa_update = PessoaUpdate(
        nome="Gustavo Atualizado",
        idade=21,
        email="teste@email.com"
    )

    assert pessoa_update.nome == "Gustavo Atualizado"
    assert pessoa_update.idade == 21
    assert pessoa_update.email == "teste@email.com" 
    