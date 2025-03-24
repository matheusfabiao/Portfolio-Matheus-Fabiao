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
- **Bootstrap 5.3** - Framework CSS moderno e responsivo
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
│   │-- core/         # Configurações e URLs base
│   │-- static/       # Assets estáticos
│   │-- templates/    # Templates HTML
│   │-- manage.py     # CLI do Django
│-- env_files/        # Configurações de ambiente
│-- pyproject.toml    # Dependências e tasks
│-- .venv/           # Ambiente virtual
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
