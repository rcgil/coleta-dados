<h1 align="center">
      <a"> Coleta de dados </a>
</h1>

# Tabela de conteúdos

<!--ts-->

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)

- [Como executar o projeto](#-como-executar-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Rodando o Backend (servidor)](#user-content--rodando-o-backend-servidor)
- [Tecnologias](#-tecnologias)
  - [Server](#user-content-server--nodejs----typescript)
  <!--te-->

## 💻 Sobre o projeto

Este projeto busca armazenar e tratar dados a cerca de informações de atendimentos de clientes.

---

## ⚙️ Funcionalidades

- [x] Recebe um arquivo (o arquivo "Base_teste.txt é encontrado na pasta raiz do projeto) de dados e:

  - [x] Armazena em uma base de dados relacional
  - [x] Trata os dados serializando CPF/CNPJ
  - [x] Transforma Strings contendo datas, em tipo Date da base de dados
  - [x] Trata os dados deixando todos com letras minúsculas e sem caracteres especiais

---

</p>

---

## 🚀 Como executar o projeto

Este projeto roda apenas o backend:

1. Backend (pasta services)

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Doker](https://www.docker.com/products/docker-desktop).
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

#### 🎲 Rodando o Backend (servidor)

```bash

# Clone este repositório
$ git clone https://github.com/rcgil/dados.git

# Acesse a pasta do projeto no terminal/cmd
$ cd Dados


# Para fazer o build rode o comando:
$ docker-compose build

# Para subir a aplicaç!ao rode o comando
$ docker-compose up

# Para parar a aplicação rode o comando:
$ docker-compose down

```

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

**Server**

- **[FLASK](https://flask.palletsprojects.com/en/2.0.x/)**
- **[DOCKER](https://www.docker.com)**
- **[POSTGRESQL](https://www.postgresql.org)**

## 💪 Como contribuir no projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`
   > Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](./CONTRIBUTING.md)

---

## 🦸 Autor

<sub><b>Rodrigo Castro Gil</b></sub></a>
<br />
