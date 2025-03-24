# 🌐 Portfólio | Matheus Fabião

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Tailwind](https://img.shields.io/badge/Tailwind-4.0-blue.svg)](https://tailwindcss.com/)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)]()

Este é meu site portfólio pessoal, desenvolvido com Django e gerenciado com [UV](https://github.com/astral-sh/uv). O objetivo é apresentar meus trabalhos e informações profissionais de forma elegante e moderna, demonstrando minhas habilidades como desenvolvedor.

## 🚀 Tecnologias Utilizadas

- **Django** – Framework web para o backend
- **Tailwind v4.0** – Estrutura e estilos do frontend
- **PostgreSQL** – Banco de dados
- **UV** – Gerenciamento de pacotes Python
- **Gunicorn/Nginx** – Deploy em produção

## 📂 Estrutura do Projeto

```
portfolio-matheusfabiao/
│-- src/              # Diretório principal do código
│   │-- core/         # Configurações e URLs base do Django
│   │-- portfolio/    # Aplicação principal do portfólio
│   │   │-- migrations/  # Migrações do banco de dados
│   │   │-- admin.py    # Configuração do admin
│   │   │-- apps.py     # Configuração da aplicação
│   │   │-- models.py   # Modelos de dados
│   │   │-- tests.py    # Testes da aplicação
│   │   │-- urls.py     # URLs da aplicação
│   │   │-- views.py    # Views da aplicação
│   │-- static/       # Arquivos estáticos
│   │   │-- fa/      # Fonte de ícones
│   │   │-- fonts/   # Fontes personalizadas
│   │   │-- img/     # Imagens do site
│   │-- templates/    # Templates HTML
│   │   │-- base.html   # Template base
│   │   │-- portfolio/  # Templates do portfólio
│   │-- manage.py     # CLI do Django
│-- docs/             # Documentação MkDocs
│   │-- docs/         # Arquivos markdown
│   │-- mkdocs.yml    # Configuração do MkDocs
│-- env_files/        # Arquivos de ambiente
│   │-- .env.example  # Exemplo de configuração
│-- pyproject.toml    # Configuração e dependências
│-- .venv/           # Ambiente virtual (não versionado)
```

## 🛠️ Configuração do Ambiente

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/matheusfabiao/portfolio-matheusfabiao.git
cd portfolio-matheusfabiao
```

### 2️⃣ Configure o Ambiente Virtual
```bash
uv venv .venv
source .venv/bin/activate  # Linux/macOS
# No Windows: .venv\Scripts\activate
```

### 3️⃣ Instale as Dependências
```bash
uv pip install -e ".[dev]"
```

### 4️⃣ Configure as Variáveis de Ambiente
Crie um arquivo `.env` baseado no `.env.example` fornecido.

### 5️⃣ Execute as Migrações
```bash
task migrate
```

## ⚡ Executando o Projeto

Para iniciar o servidor de desenvolvimento:

```bash
task run
```

O site estará disponível em `http://localhost:8000`

## 📝 Nota

Este é um projeto pessoal e não está aberto para contribuições externas. A documentação serve como referência técnica e demonstração das tecnologias e práticas utilizadas no desenvolvimento.

## 🌍 Deploy

Para ambiente de produção:

1. Configure um banco de dados PostgreSQL
2. Configure as variáveis de ambiente adequadamente
3. Use Gunicorn com Nginx para servir a aplicação
4. Configure certificados SSL para HTTPS

## 📫 Contato

- 🔗 Site: [https://matheusfabiao.com](https://matheusfabiao.com)
- 📧 Email: [contato@matheusfabiao.com](mailto:contato@matheusfabiao.com)
- 💼 LinkedIn: [Matheus Fabião](https://linkedin.com/in/matheusfabiao)
- 🐙 GitHub: [@matheusfabiao](https://github.com/matheusfabiao)