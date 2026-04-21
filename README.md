> [!TIP]
> **Este repositório é um Mirror.** O desenvolvimento principal e a "Soberania do Código" ocorrem no [Codeberg](https://codeberg.org/HeadHSM/netdevops-projeto_01).

# NetDevOps Projeto 02

Este projeto automatiza a gestão de inventários para Ansible a partir de bancos de dados SQLite.

## 🛠️ Funcionamento

O sistema centraliza informações de **Servidores** e **Dispositivos** em bancos de dados distintos. O diferencial aqui é a geração de um ambiente de trabalho seguro:

1.  **Credenciais**: Ao rodar o comando de acesso, o sistema gera um arquivo `.env` com credenciais criptografadas.
2.  **Inventário Dinâmico**: O `inventory.py` lê os bancos `servidores.db` e `dispositivos.db` e gera o JSON que o Ansible precisa, sem necessidade de arquivos `.ini` manuais.
3.  **Automação**: O `playbook.yml` utiliza esses dados para configurar o ambiente (ex: Nginx).

## 🚀 Comandos Principais

Utilize o `Makefile` para interagir com o projeto:

- `make menu`: Abre a interface principal de gestão (`main.py`).
- `make ansible`: Executa o playbook do Ansible utilizando o inventário dinâmico.

## 📂 Estrutura do Projeto

A organização dos arquivos segue o padrão de automação NetDevOps moderno:

```text
.
├── ansible.cfg          # Configurações globais do Ansible
├── database.py          # Modelagem SQLAlchemy e conexão com SQLite
├── dispositivos.db      # Banco de Dados de ativos de rede
├── inventory.py         # Script Python de inventário dinâmico
├── main.py              # Menu principal e orquestração do sistema
├── Makefile             # Atalhos para comandos rápidos (make login, make ansible)
├── playbook.yml         # Automação de tarefas (ex: instalação Nginx)
├── pyproject.toml       # Dependências e configurações do projeto (UV)
├── README.md            # Documentação do projeto
├── registro.py          # Lógica de cadastro de novos usuários/equipamentos
├── servidores.db        # Banco de Dados específico de servidores
└── verificacao.py       # Lógica de login e criptografia de credenciais
```

---
