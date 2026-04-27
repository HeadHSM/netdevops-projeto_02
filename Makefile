.PHONY: ajuda registrar verificar remover atualizar sync ansible

# Comando padrão, caso digitado somente 'make'
all: ajuda

registrar:
	@echo "Abrindo Menu de Registro..."
	@uv run main.py registrar

verificar:
	@echo "Abrindo Menu de Verificação..."
	@uv run main.py verificar

remover:
	@echo "Abrindo Menu de Remoção..."
	@uv run main.py remover

atualizar:
	@echo "Abrindo Menu de Atualização..."
	@uv run main.py atualizar

ajuda:
	@uv run main.py --help

sync:
	@echo "Realizando Sincronização de Pacotes"
	@uv sync

ansible:
	@echo "Iniciando Automação Ansible..."
	@uv run ansible-playbook -i inventory.py playbook.yml -K