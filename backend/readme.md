# ✅ ToDoFlex – API de Lista de Tarefas

O **ToDoFlex** é uma API desenvolvida em Python com FastAPI para gerenciar tarefas (ToDoList), pensada para integração com aplicações **web** e **mobile**. O projeto está estruturado para facilitar o crescimento modular, testes e escalabilidade.

---

## 🚀 Funcionalidades atuais

- 📋 Obtenção de tarefas
- 🔄 Atualização automática em tempo real durante o desenvolvimento (hot reload)

> Em constante evolução: novos endpoints, autenticação e banco de dados serão adicionados nas próximas versões.

---

## 🏗️ Estrutura do Projeto

ToDoFlex/
├── backend/
│ ├── app/
│ │ ├── main.py ← Ponto de entrada da aplicação
│ │ ├── routers/
│ │ │ └── task_routes.py ← Arquivo com as rotas da API
│ │ └── init.py
│ ├── start.bat ← Script para inicializar o servidor (Windows)
│ ├── requirements.txt ← Dependências do projeto
│ └── venv/ ← Ambiente virtual do Python

yaml
Copiar
Editar

---

## 🛠️ Como executar localmente

### Pré-requisitos
- Python 3.11+
- Git (opcional)
- Navegador para acessar a documentação Swagger

### 1. Clone o projeto (se aplicável)
```bash
git clone https://github.com/seu-usuario/ToDoFlex.git
cd ToDoFlex/backend
2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Inicie o servidor com o script (Windows)
bash
Copiar
Editar
start.bat
Ou manualmente:

bash
Copiar
Editar
uvicorn app.main:app --reload
5. Acesse a documentação interativa
Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

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





