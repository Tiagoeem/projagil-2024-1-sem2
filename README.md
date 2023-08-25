# Exercício de Web Services com Flask e SQLite

O objetivo deste exercício é criar um serviço web simples para gerenciar uma biblioteca. A aplicação terá a capacidade de cadastrar livros e usuários da biblioteca. A ideia é que os alunos explorem a criação de endpoints que interajam com um banco de dados SQLite, abrangendo as operações de CRUD (Create, Read, Update, Delete).

## Requisitos:

1. **Estrutura de Pastas**:
    * /db: Pasta contendo o banco de dados SQLite e scripts relacionados.
    * app.py: Arquivo principal contendo sua aplicação Flask.
    
2. **Criação da Base de Dados**:
    * A base de dados é criada executando um arquivo à parte.
    * Este arquivo só precisa ser executado uma vez durante o projeto.

3. **Tabelas**:
    * **Livros**: ID (chave primária), Título, Autor, Ano de Publicação, Gênero.
    * **Usuários**: ID (chave primária), Nome, Email, Data de Cadastro.

4. **Endpoints**:
    * **GET** `/`: Deve retornar "Hello, World!".
    * **POST** `/livro`: Cadastro de um novo livro.
    * **GET** `/livro`: Lista todos os livros. Deve suportar um query param para filtrar livros por gênero.
    * **GET** `/livro/<int:id>`: Retorna detalhes de um livro específico pelo ID.
    * **DELETE** `/livro/<int:id>`: Exclui um livro pelo ID.
    * **POST** `/usuario`: Cadastro de um novo usuário.
    * **GET** `/usuario`: Lista todos os usuários.
    * **GET** `/usuario/<int:id>`: Retorna detalhes de um usuário específico pelo ID.
    * **DELETE** `/usuario/<int:id>`: Exclui um usuário pelo ID.

5. **Requisitos Adicionais**:
    * Ao cadastrar um novo livro ou usuário via POST, os dados devem ser enviados como JSON no corpo da requisição.
    * Ao listar livros, deve ser possível filtrar por gênero usando um query param. Exemplo de requisição com query param: `GET /livro?genero=Fantasia`. Esta requisição retornaria todos os livros do gênero "Fantasia".
    * Implemente tratamento de erros adequado para situações como tentar excluir um livro ou usuário que não existe.

6. **Testando e Completando a Collection no Postman**:
    * Dentro da pasta do projeto, você encontrará uma subpasta chamada `postman` que contém uma collection inicial para o Postman.
    * Para importar a collection:
        1. Abra o Postman.
        2. Clique em "File" > "Import".
        3. Navegue até a pasta `postman` do seu projeto e selecione o arquivo JSON da collection.
        4. Clique em "Open".
    * **ATENÇÃO**: É fundamental que você adicione TODOS os métodos e endpoints na collection do Postman. Completar esta collection é uma parte essencial do exercício e vale pontos. Certifique-se de que cada endpoint esteja funcionando corretamente e que as requisições estejam configuradas de forma adequada.
    * Após completar a collection:
        1. No Postman, clique com o botão direito na collection "Biblioteca".
        2. Selecione "Export".
        3. Escolha a versão do formato (recomendamos a versão 2.1).
        4. Clique em "Export" e salve o arquivo na pasta `postman` do projeto.
    * **Observação**: Não se preocupe se o arquivo exportado tiver o mesmo nome do arquivo original. Você pode sobrescrever o arquivo existente.


Obs. O uso do arquivo `db_utils.py` é opcional nesta atividade.
