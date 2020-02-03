include .env

.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: commit
commit: ## run helper tool for writing commit messages.
	@npm run commit

.PHONY: tree
tree: ## ls directory structure.
	@tree -I 'node_modules|commitlint.config.js|LICENSE.txt|README.md|package.json|package-lock.json|Makefile|sample.env|flask_tutorial_venv'

.PHONY: venv
venv: ## activate virtualenv.
venv: flask_tutorial_venv/bin/activate

flask_tutorial_venv/bin/activate: requirements.txt
	@test -d flask_tutorial_venv || python3 -m venv flask_tutorial_venv
	@source flask_tutorial_venv/bin/activate; pip install --upgrade pip && pip install -r ./requirements.txt
	@touch flask_tutorial_venv/bin/activate

.PHONY: run
run: venv ## run flask code.
	@source flask_tutorial_venv/bin/activate; python3 src/server/app.py