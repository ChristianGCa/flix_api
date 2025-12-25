# Flix API

Este é um projeto desenvolvido como parte do curso Django Master da PyCodeBR. Ele consiste em uma API para gerenciar informações relacionadas a filmes, gêneros, atores e avaliações. O projeto foi construído utilizando o framework Django.

## Funcionalidades

- **Autenticação**: Endpoints para autenticação de usuários utilizando JWT.
- **Gerenciamento de Gêneros**: CRUD para gêneros de filmes.
- **Gerenciamento de Atores**: CRUD para atores.
- **Gerenciamento de Filmes**: CRUD para filmes.
- **Avaliações**: CRUD para avaliações de filmes.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Django**: Framework web para desenvolvimento rápido e seguro.
- **Django REST Framework**: Extensão para criação de APIs RESTful.
- **SQLite**: Banco de dados utilizado no desenvolvimento.

## Instalação e Configuração

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd flix-api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo `.env`:

   ```env
   SECRET_KEY=uma-chave-secreta-segura
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Endpoints Principais

Os endpoints da API estão organizados sob o prefixo `/api/v1/`. Aqui estão alguns exemplos:

- **Autenticação**:
  - `POST /api/v1/authentication/token/`: Obter token JWT.
  - `POST /api/v1/authentication/token/refresh/`: Atualizar token JWT.

- **Gêneros**:
  - `GET /api/v1/genres/`: Listar gêneros.
  - `POST /api/v1/genres/`: Criar um novo gênero.

- **Atores**:
  - `GET /api/v1/actors/`: Listar atores.
  - `POST /api/v1/actors/`: Criar um novo ator.

- **Filmes**:
  - `GET /api/v1/movies/`: Listar filmes.
  - `POST /api/v1/movies/`: Criar um novo filme.

- **Avaliações**:
  - `GET /api/v1/reviews/`: Listar avaliações.
  - `POST /api/v1/reviews/`: Criar uma nova avaliação.
