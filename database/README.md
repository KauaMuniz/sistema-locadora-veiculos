# 🗄️ Banco de Dados

Esta pasta reúne todos os os arquivos relacionados ao banco de dados do projeto **Sistema Locadora de Veículos**.

O objetivo é organizar a estrutura do banco de dados, os dados para testes, consultas SQL e a documentação da modelagem, facilitando a manutenção e a evolução do sistema.

---

## 📂 Estrutura

```text
database/
│
├── schema.sql
├── seeds.sql
├── queries.sql
├── modelagem_banco_de_dados.png
└── README.md
```

---

## 📄 Descrição dos Arquivos

### `schema.sql`

Arquivo responsável pela criação da estrutura completa do banco de dados.

Contém:

- Criação do banco de dados;
- Criação das tabelas;
- Definição das chaves primárias (PRIMARY KEY);
- Definição das chaves estrangeiras (FOREIGN KEY);
- Tipos de dados;
- Restrições da modelagem.

Este é o primeiro arquivo que deve ser executado para inicializar o banco de dados.

---

### `seeds.sql`

Contém registros fictícios utilizados para testes da aplicação.

Exemplos de dados inseridos:

- Veículos;
- Clientes;
- Funcionários;
- Locações.

Seu objetivo é facilitar o desenvolvimento e os testes sem a necessidade de cadastrar informações manualmente.

---

### `queries.sql`

Arquivo destinado ao armazenamento de consultas SQL desenvolvidas durante o aprendizado e para validação da modelagem do banco de dados.

Exemplos de consultas que podem ser armazenadas:

- SELECT
- WHERE
- ORDER BY
- UPDATE
- DELETE
- INNER JOIN
- GROUP BY
- COUNT
- SUM
- AVG

Este arquivo também pode ser utilizado como referência para estudos e testes durante a evolução do projeto.

---

### `modelagem_banco_de_dados.png`

Diagrama da modelagem do banco de dados.

Representa graficamente:

- As entidades do sistema;
- Os atributos de cada tabela;
- As chaves primárias (Primary Keys);
- As chaves estrangeiras (Foreign Keys);
- Os relacionamentos entre as tabelas.

O diagrama serve como documentação da estrutura do banco de dados e auxilia na compreensão da arquitetura da aplicação.

---

## 🚀 Ordem de Execução

Para criar completamente o banco de dados do projeto, execute os arquivos na seguinte ordem:

1. `schema.sql`
2. `seeds.sql`
3. `queries.sql` *(opcional, para testes e estudos)*

---

## 🛠️ Sistema Gerenciador de Banco de Dados

- MySQL

---

## 🎯 Objetivo

Esta organização busca manter uma separação clara entre:

- Estrutura do banco de dados;
- Dados para testes;
- Consultas SQL;
- Documentação da modelagem.

Essa abordagem facilita a manutenção, os testes e a evolução do projeto, além de seguir uma organização comum em projetos de desenvolvimento de software.
