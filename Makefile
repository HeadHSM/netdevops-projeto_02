.PHONY: menu ansible

menu:
	@echo "Iniciando Menu Principal"
	@uv run python3 main.py

ansible:
	@echo "Iniciando Ansible"
	@uv run ansible-playbook -i inventory.py playbook.yml -K