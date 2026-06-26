# 🚗 Sistema Locadora de Veículos

Sistema de locadora de veículos desenvolvido em Python com o objetivo de aplicar conceitos de lógica de programação, manipulação de arquivos, controle de dados e, futuramente, tecnologias amplamente utilizadas no mercado como MySQL, Programação Orientada a Objetos (POO) e APIs REST.

## 📖 Sobre o Projeto

Este projeto simula o funcionamento de uma locadora de veículos, permitindo o gerenciamento de veículos por meio de operações CRUD (Create, Read, Update e Delete).

A primeira versão foi desenvolvida utilizando armazenamento em arquivos TXT para consolidar conceitos fundamentais de programação. Atualmente, o projeto já possui a modelagem e o schema do banco de dados em MySQL, e continuará evoluindo com a integração ao banco, refatoração para Programação Orientada a Objetos (POO) e desenvolvimento de uma API REST.

---

## ✨ Funcionalidades Atuais

- Cadastro de veículos
- Listagem de veículos cadastrados
- Alteração de informações dos veículos
- Exclusão de veículos por ID
- Pesquisa de veículos por valor
- Geração de relatório individual por ID
- Validação de dados de entrada
- Persistência de dados em arquivo TXT
- Modelagem do banco de dados em MySQL
- Schema SQL para criação automática do banco
- Interface de terminal com menu interativo

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- MySQL
- Manipulação de Arquivos TXT
- Git
- GitHub

---

## 📂 Estrutura do Projeto

```text
sistema-locadora-veiculos/
│
├── src/
│   ├── main.py
│   └── funcoes.py
│
├── data/
│   └── carros.txt
│
├── database/
│   ├── schema.sql
│   └── modelagem-banco-de-dados.png
│
├── docs/
│
├── README.md
└── .gitignore
```

---

## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/KauaMuniz/sistema-locadora-veiculos.git
```

Acesse a pasta do projeto:

```bash
cd sistema-locadora-veiculos
```

Execute a aplicação:

```bash
python src/main.py
```

---

## 📈 Roadmap

### Versão 1.0 — Concluída

- [x] CRUD de veículos
- [x] Armazenamento em arquivo TXT
- [x] Pesquisa de veículos
- [x] Relatórios
- [x] Validação de dados de entrada

### Versão 2.0 — Em desenvolvimento

- [x] Modelagem do banco de dados
- [x] Criação do schema MySQL
- [ ] Migração do armazenamento TXT para MySQL
- [ ] Separação da camada de persistência

### Versão 3.0

- [ ] Refatoração para Programação Orientada a Objetos (POO)
- [ ] Implementação das entidades do sistema
- [ ] Melhor organização dos módulos

### Versão 4.0

- [ ] Cadastro de clientes
- [ ] Sistema de locação de veículos
- [ ] Controle de disponibilidade dos veículos

### Versão 5.0

- [ ] Histórico de locações
- [ ] Relatórios avançados
- [ ] Cálculo automático do valor da locação

### Versão 6.0

- [ ] Integração com a API FIPE
- [ ] Consulta automática de marcas e modelos

### Versão 7.0

- [ ] Desenvolvimento de API REST com FastAPI
- [ ] Endpoints para veículos, clientes e locações

---

## 🎯 Objetivos de Aprendizado

Este projeto tem como objetivo aprofundar conhecimentos em:

- Python
- Estruturas de dados
- Programação Orientada a Objetos (POO)
- Modelagem de Banco de Dados
- MySQL
- Integração com APIs
- Desenvolvimento Backend
- Git e GitHub
- Boas práticas de programação

---

## 👨‍💻 Autor

**Kauã Bento Muniz**

Estudante de Engenharia de Software, desenvolvendo projetos práticos para consolidar conhecimentos em desenvolvimento Backend, bancos de dados e boas práticas de engenharia de software.
