# Portfólio Matheus Fabião

Bem-vindo ao meu portfólio profissional, uma plataforma web robusta desenvolvida com Django que demonstra minha expertise em desenvolvimento de software. Este projeto não é apenas uma vitrine dos meus trabalhos, mas também um exemplo prático da minha abordagem em arquitetura de software, boas práticas de desenvolvimento e domínio das tecnologias modernas.

## 🎯 Visão Geral

Este portfólio foi construído seguindo princípios de Clean Architecture e boas práticas de desenvolvimento, com foco em:

- **Modularidade** - Estrutura organizada que facilita manutenção e escalabilidade
- **Performance** - Otimizações de carregamento e renderização
- **Segurança** - Implementação das melhores práticas de segurança do Django
- **Responsividade** - Design adaptativo para diferentes dispositivos

## 🚀 Stack Tecnológica

### Backend
- **Django 5.1+** - Framework web robusto e seguro
- **PostgreSQL** - Sistema de banco de dados relacional
- **Gunicorn** - Servidor WSGI de produção
- **Nginx** - Servidor web e proxy reverso

### Frontend
- **Tailwind v4.0** - Framework CSS moderno e responsivo
- **CSS** - Estilização personalizada e responsiva
- **HTMX** - Interatividade dinâmica e moderna, sem recarregamento da página

### DevOps & Ferramentas
- **UV** - Gerenciador de pacotes Python moderno
- **Pytest** - Framework de testes
- **Ruff** - Linter e formatter Python
- **MkDocs** - Documentação elegante e organizada

## 📂 Arquitetura do Projeto

```
portfolio-matheusfabiao/
│-- src/              # Código-fonte principal
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

## 🛠️ Ambiente de Desenvolvimento

1. Clone o repositório
2. Configure um ambiente virtual Python 3.12+
3. Instale as dependências:
   ```bash
   uv pip install -e ".[dev]"
   ```
4. Configure as variáveis de ambiente (.env)
5. Execute as migrações:
   ```bash
   task migrate
   ```

## ⚡ Execução Local

Inicie o servidor de desenvolvimento:

```bash
 task run
```

Acesse `http://localhost:8000`

## 📝 Nota

Este projeto é uma demonstração do meu trabalho e abordagem profissional no desenvolvimento de software. A documentação serve como referência técnica e showcase das tecnologias e práticas utilizadas.
