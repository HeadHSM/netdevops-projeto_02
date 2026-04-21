> [!TIP]
> **Este repositório é um Mirror.** O desenvolvimento principal e a "Soberania do Código" ocorrem no [Codeberg](https://codeberg.org/HeadHSM/netdevops-projeto_01).

# 🚀 NetDevOps Projeto 02 [WIP]

Sistema de gerenciamento de inventário para Ansible, focado em automatizar a administração de ativos de rede e servidores via banco de dados SQLite.

## 🛠️ Funcionalidades

O projeto substitui o inventário estático do Ansible por uma solução dinâmica, centralizada e fácil de gerenciar:

Tenho ciência de que o arquivo `inventory.py` não está completamente automatico, tendo em vista, de que ainda tem de adicionar o [grupo] dos dispositivos e servidores manualmente, pretendo estudar e resolver isso no projeto seguinte.

1.  **Gestão Completa (CRUD)**: Interface CLI para registrar, listar, atualizar e remover ativos.
2.  **Inventário Dinâmico**: O script `inventory.py` converte os dados do SQLite em JSON para o Ansible em tempo real.
3.  **Ambiente Moderno**: Gerenciamento de dependências ultra-rápido com **UV** e interface visual com **Rich & Typer**.

## 📂 Estrutura do Projeto

```text
.
├── atualizar.py      # Lógica de alteração de dados existentes
├── database.py       # Modelagem SQLAlchemy e conexão SQLite
├── inventory.py      # Script de inventário dinâmico para Ansible
├── main.py           # Menu principal e orquestração (Typer/Rich)
├── Makefile          # Atalhos para comandos (make menu, make ansible)
├── registro.py       # Lógica de inserção de novos ativos
├── remover.py        # Lógica de exclusão de ativos
├── verificacao.py    # Listagem e consulta de dados
├── playbook.yml      # Automação de tarefas (Provisionamento)
├── ansible.cfg       # Configuração do ambiente Ansible
└── pyproject.toml    # Dependências e metadados (UV)
```

## 🚀 Como Utilizar

### Pré-requisitos

```text
Python 3.12+

UV instalado
```

### Comandos Rápidos

Instalar dependências:

```bash
uv sync
```

Abrir o Menu de Gestão:

```bash
make menu
```

Rodar a Automação:

```bash
make ansible
```

---
