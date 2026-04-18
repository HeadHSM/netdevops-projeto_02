.PHONY: login create delete read

login:
	@echo "Ainda em Construção"
	@python3 scripts/login.py
create:
	@echo "Abrindo menu de criação"
	@python3 scripts/create.py

read:
	@echo "Lendo Banco de Dados..."
	@uv run python scripts/ler.py

delete:
	@echo "Ainda em Construção"
	@python3 scripts/delete.py
