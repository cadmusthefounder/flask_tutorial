include .env

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: commit
commit: ## run helper tool for writing commit messages.
	@npm run commit

.PHONY: tree
tree: ## ls directory structure.
	@tree -I 'node_modules|commitlint.config.js|LICENSE.txt|README.md|package.json|package-lock.json|Makefile|sample.env|flask_tutorial_venv'

.PHONY: venv
venv: flask_tutorial_venv/bin/activate ## activate virtualenv.

flask_tutorial_venv/bin/activate: requirements.txt
	@test -d flask_tutorial_venv || python3 -m venv flask_tutorial_venv
	@source flask_tutorial_venv/bin/activate; pip install --upgrade pip && pip install -r ./requirements.txt
	@touch flask_tutorial_venv/bin/activate

.PHONY: run
run: venv # run flask code.
	@source flask_tutorial_venv/bin/activate; python3 src/server/app.py