.PHONY: ajuda criar ler remover atualizar sync ansible

# Comando padrão, caso digitado somente 'make'
all: ajuda

criar:
	@echo "Abrindo Menu de Registro..."
	@uv run main.py registrar

ler:
	@echo "Abrindo Menu de Verificação..."
	@uv run main.py verificar

remover:
	@echo "Abrindo Menu de Remoção..."
	@uv run main.py excluir

atualizar:
	@echo "Abrindo Menu de Atualização..."
	@uv run main.py alterar

ajuda:
	@uv run main.py --help

sync:
	@echo "Realizando Sincronização de Pacotes"
	@uv sync

ansible:
	@echo "Iniciando Automação Ansible..."
	@uv run ansible-playbook -i inventory.py playbook.yml -K