# 🏋️ WorkoutAPI

Este projeto é baseado em uma proposta de um curso da  Digital Innovation One de  FastAPI. 

Esta é uma API de competição de crossfit chamada WorkoutAPI, esta API é pequena e simplificada, desenvolvida para ser um 
projeto hands-on que utiliza poucas tabelas, mas com o necessário para aprender como utilizar o FastAPI.

## 🚀 Framework FastAPI

FastAPI oferece alta performance, é fácil de aprender, fácil de codar e está pronto para produção.

## ⚡ Async

Código assíncrono significa que a linguagem tem uma forma de instruir o computador/programa que, em certo ponto, ele terá que esperar por algo que será finalizado em outro lugar.


# 🛠️ Stack da API

A API foi desenvolvida utilizando FastAPI (async), junto das seguintes bibliotecas:

    Alembic
    SQLAlchemy
    Pydantic
    PostgreSQL
    Docker



## ▶️ Execução da API

`pip install -r requirements.txt`


Para subir o banco de dados, caso não tenha o docker-compose instalado, faça a instalação e logo em seguida, execute:


`make run-docker`

Para criar uma nova migration, execute:


`make create-migrations d="nome_da_migration"`

Para criar o banco de dados, execute:


`make run-migrations`

## 🌐 API

Para subir a API, execute:


`make run`

e acesse: http://127.0.0.1:8000/docs
