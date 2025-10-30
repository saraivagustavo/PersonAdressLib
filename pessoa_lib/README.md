# 📖 Pessoa Lib

[![Status do
Workflow](https://img.shields.io/github/actions/workflow/status/saraivagustavo/PersonAdressLib/deploy.yml?branch=main&style=for-the-badge)](https://github.com/saraivagustavo/PersonAdressLib/actions)
[![PyPI](https://img.shields.io/pypi/v/saraivagustavo?style=for-the-badge)](https://pypi.org/project/saraivagustavo/)
[![Versão do
Python](https://img.shields.io/pypi/pyversions/saraivagustavo?style=for-the-badge)](https://pypi.org/project/saraivagustavo/)
[![Licença](https://img.shields.io/pypi/l/saraivagustavo?style=for-the-badge)](https://pypi.org/project/saraivagustavo/)

Esta é uma biblioteca Python para gerenciar **Pessoas** e seus
respectivos **Endereços**. Originalmente desenvolvida como parte de um
projeto acadêmico, ela separa a lógica de negócios e o acesso a dados da
camada de API (View/Controller).

A biblioteca utiliza `SQLModel` (baseado em Pydantic e SQLAlchemy) para
definição de modelos, DTOs e interação com o banco de dados.

------------------------------------------------------------------------

## ✨ Principais Features

-   **Gerenciamento de Pessoas**: CRUD para entidades `Pessoa` (Nome,
    Idade, Email).
-   **Gerenciamento de Endereços**: CRUD para entidades `Endereco`
    (Logradouro, Número, etc.).
-   **Relacionamento**: Modela o relacionamento um-para-muitos (Uma
    `Pessoa` pode ter múltiplos `Enderecos`).
-   **Arquitetura Desacoplada**: Utiliza um padrão genérico de `Service`
    e `Repository` para máxima reutilização de código.
-   **Validação de Dados**: Baseada em `SQLModel` e `Pydantic` para
    garantir a integridade dos dados.

------------------------------------------------------------------------

## 🚀 Instalação

Você pode instalar a biblioteca diretamente do PyPI:

``` bash
pip install saraivaPessoaLib
```

------------------------------------------------------------------------

## 💡 Exemplo de Uso (Quick Start)

Veja como é simples configurar um banco de dados em memória e usar os
serviços para criar e listar entidades:

``` python
from sqlmodel import create_engine, Session, SQLModel
from pessoa_lib.models import Pessoa
from pessoa_lib.dto import PessoaCreate
from pessoa_lib.repository import Repository
from pessoa_lib.service import Service

# 1. Configurar o Engine (ex: SQLite em memória)
engine = create_engine("sqlite:///:memory:")

# 2. Criar as tabelas no banco de dados
SQLModel.metadata.create_all(engine)

# 3. Instanciar Repository e Service genéricos para o modelo 'Pessoa'
pessoa_repo = Repository(Pessoa)
pessoa_service = Service(pessoa_repo)

# 4. Criar uma nova pessoa
print("Criando pessoa...")
with Session(engine) as session:
    pessoa_dto = PessoaCreate(
        nome="Carlos Souza",
        idade=45,
        email="carlos.souza@exemplo.com"
    )
    pessoa = pessoa_service.create(session=session, data=pessoa_dto)
    print(f"-> Pessoa Criada: {pessoa.nome} (ID: {pessoa.id})")

# 5. Listar todas as pessoas
print("\nListando pessoas...")
with Session(engine) as session:
    pessoas = pessoa_service.list(session=session, offset=0, limit=10)
    for p in pessoas:
        print(f"-> Pessoa Encontrada: {p.nome}")
```

**Saída Esperada:**

    Criando pessoa...
    -> Pessoa Criada: Carlos Souza (ID: 1)

    Listando pessoas...
    -> Pessoa Encontrada: Carlos Souza

------------------------------------------------------------------------

## 🏛️ Arquitetura da Biblioteca

A `pessoa_lib` é organizada com uma clara separação de
responsabilidades:

    pessoa_lib/
    ├── models.py        # Modelos de dados (Pessoa, Endereco)
    ├── dto.py           # Data Transfer Objects (Create, Read, Update)
    ├── repository.py    # Classe Repository genérica (CRUD)
    ├── service.py       # Classe Service genérica (lógica de negócios)
    └── database.py      # Configuração e inicialização do banco

------------------------------------------------------------------------

## 🧑‍💻 Contribuição e Desenvolvimento

Se você deseja contribuir com o projeto, siga estes passos para
configurar o ambiente de desenvolvimento:

### 1️⃣ Clone o repositório:

``` bash
git clone https://github.com/saraivagustavo/PersonAdressLib.git
cd PersonAdressLib/pessoa_lib
```

### 2️⃣ Crie e ative um ambiente virtual:

``` bash
python -m venv venv
source venv/bin/activate  # (ou .\venv\Scripts\activate no Windows)
```

### 3️⃣ Instale as dependências (incluindo as de desenvolvimento):

``` bash
pip install -e .[dev]
```

> O `-e .` instala o pacote em modo editável.

### 4️⃣ Rode os testes:

``` bash
pytest
```

------------------------------------------------------------------------

## 📝 Licença

Este projeto é distribuído sob a licença **MIT**.\
Consulte o arquivo `LICENSE` para mais detalhes.
