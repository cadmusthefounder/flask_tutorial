.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: commit
commit: ## run helper tool for writing commit messages.
	@npm run commit

.PHONY: tree
tree: ## ls directory structure.
	@tree -I 'node_modules|commitlint.config.js|LICENSE.txt|README.md|package.json|package-lock.json|Makefile|project_venv|__pycache__'

.PHONY: venv
venv: ## activate virtualenv.
venv: project_venv/bin/activate

project_venv/bin/activate: requirements.txt
	@test -d project_venv || python3 -m venv project_venv
	@source project_venv/bin/activate; pip install --upgrade pip && pip install -r ./requirements.txt
	@touch project_venv/bin/activate

.PHONY: run
run: venv # run flask code.
	@source project_venv/bin/activate; python3 main.py
