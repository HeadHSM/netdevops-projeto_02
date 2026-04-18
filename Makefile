.PHONY: login create delete read

login:
	@echo "Ainda em Construção"
	@uv run python scripts/login.py
create:
	@echo "Abrindo menu de criação"
	@uv run python scripts/create.py

read:
	@echo "Lendo Banco de Dados..."
	@uv run python scripts/ler.py

delete:
	@echo "Ainda em Construção"
	@uv run python scripts/delete.py
