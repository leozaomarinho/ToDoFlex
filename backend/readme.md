# ✅ ToDoFlex – API de Lista de Tarefas

O **ToDoFlex** é uma API desenvolvida em Python com FastAPI para gerenciar tarefas (ToDoList), pensada para integração com aplicações **web** e **mobile**. O projeto está estruturado para facilitar o crescimento modular, testes e escalabilidade.

---

## 🚀 Funcionalidades atuais

- 📋 Obtenção de tarefas
- 🔄 Atualização automática em tempo real durante o desenvolvimento (hot reload)

> Em constante evolução: novos endpoints, autenticação e banco de dados serão adicionados nas próximas versões.


### Pré-requisitos
- Python 3.11+
- Git (opcional)
- Navegador para acessar a documentação Swagger

📦 Bibliotecas utilizadas
Este projeto utiliza bibliotecas modernas da stack Python para desenvolvimento de APIs:

🔹 FastAPI
Framework web moderno e de alta performance para APIs REST.

Geração automática de documentação.

Validação robusta com Pydantic.

Suporte a código assíncrono (async def).

🔹 Uvicorn
Servidor ASGI leve e rápido.

Permite hot reload com --reload.

Compatível com padrões modernos da web.

🔹 venv
Ferramenta padrão do Python para criação de ambientes virtuais.

Isola as dependências do projeto.

Facilita o controle de versões de bibliotecas.


✅ (feito) Criar database.py com engine e Base

✅ (feito) Criar o modelo Task (models/task_model.py)

🔲 Criar schemas (schemas/task_schema.py) — Pydantic

🔲 Criar a lógica de serviços (services/task_service.py) — CRUD

🔲 Criar rotas (routers/task_router.py) — POST, GET, PUT, DELETE

🔲 Atualizar main.py — incluir rotas e inicializar banco


