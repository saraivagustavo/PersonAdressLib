import pytest
from pessoa_lib.models import Pessoa

def test_criarPessoa():
    """
    Testa se uma instância de Pessoa pode ser criada.
    """
    pessoa = Pessoa(
        nome="Saraiva Teste",
        idade=20,
        email="saraiva@email.com"
    )
    
    assert pessoa.nome == "Saraiva Teste"
    assert pessoa.email == "saraiva@email.com"
