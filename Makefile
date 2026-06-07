.DEFAULT_GOAL := help

PORT ?= 8000
HOST ?= 127.0.0.1
PYTHON ?= python3
NETLIFY_SITE_ID ?= ae891950-b3cc-4a6f-baa4-f483277b32f5
NETLIFY_DEPLOY_DIR ?= .
SITE_URL := http://$(HOST):$(PORT)
NETLIFY_URL := https://michelamassage.netlify.app

HTML_FILES := index.html
CSS_FILES := assets/css/styles.css
JS_FILES := assets/js/main.js
DOC_FILES := $(wildcard docs/*.md)
ASSET_FILES := $(shell find assets -type f 2>/dev/null)

.PHONY: help serve open check final-check docs-check lint lint-html lint-css lint-js validate refs smoke netlify-status deploy deploy-prod deploy-open clean tree

help: ## Mostra i target disponibili
	@awk 'BEGIN {FS = ":.*##"; printf "\nTarget disponibili:\n"} /^[a-zA-Z0-9_-]+:.*##/ {printf "  %-14s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@printf "\nVariabili utili:\n"
	@printf "  PORT=%s HOST=%s\n" "$(PORT)" "$(HOST)"
	@printf "  NETLIFY_SITE_ID=%s NETLIFY_DEPLOY_DIR=%s\n" "$(NETLIFY_SITE_ID)" "$(NETLIFY_DEPLOY_DIR)"
	@printf "\nEsempi:\n"
	@printf "  make serve\n"
	@printf "  make serve PORT=8080\n"
	@printf "  make check\n"

serve: ## Avvia il sito locale con Python http.server
	@printf "Serving %s\n" "$(SITE_URL)"
	$(PYTHON) -m http.server $(PORT) --bind $(HOST)

open: ## Stampa l'URL locale da aprire nel browser
	@printf "%s\n" "$(SITE_URL)"

check: refs validate lint smoke ## Esegue tutti i controlli principali

final-check: check docs-check ## Esegue check completo prima di chiudere task/sessione

docs-check: ## Verifica documentazione e checklist agent/project
	$(PYTHON) scripts/check_docs.py

lint: lint-html lint-css lint-js ## Esegue i linter disponibili, con fallback built-in

lint-html: ## Lint HTML: htmlhint se disponibile, altrimenti controlli built-in
	@if command -v htmlhint >/dev/null 2>&1; then \
		htmlhint $(HTML_FILES); \
	elif command -v npx >/dev/null 2>&1 && [ -f package.json ]; then \
		npx --yes htmlhint $(HTML_FILES); \
	else \
		$(PYTHON) scripts/check_site.py --html-only; \
	fi

lint-css: ## Lint CSS: stylelint se disponibile, altrimenti controlli built-in
	@if command -v stylelint >/dev/null 2>&1; then \
		stylelint $(CSS_FILES); \
	elif command -v npx >/dev/null 2>&1 && [ -f package.json ]; then \
		npx --yes stylelint $(CSS_FILES); \
	else \
		$(PYTHON) scripts/check_site.py --css-only; \
	fi

lint-js: ## Controlla sintassi JavaScript con node --check
	@if command -v node >/dev/null 2>&1; then \
		node --check $(JS_FILES); \
	else \
		printf "node non trovato: skip JS syntax check\n"; \
	fi

validate: ## Valida netlify.toml, JSON-LD e struttura HTML base
	$(PYTHON) scripts/check_site.py --validate

refs: ## Verifica riferimenti locali a CSS/JS/immagini e assenza di data URI inline
	$(PYTHON) scripts/check_site.py --refs

smoke: ## Avvia server temporaneo e verifica gli endpoint principali
	$(PYTHON) scripts/smoke_test.py --host $(HOST) --port $(PORT)

netlify-status: ## Mostra informazioni del sito Netlify collegato
	@if command -v netlify >/dev/null 2>&1; then \
		netlify status; \
	elif command -v npx >/dev/null 2>&1; then \
		npx netlify status; \
	else \
		printf "Netlify CLI non trovato. Installa con: npm install -g netlify-cli\n"; exit 1; \
	fi

deploy: check ## Deploy preview su Netlify tramite CLI
	@if command -v netlify >/dev/null 2>&1; then \
		netlify deploy --dir "$(NETLIFY_DEPLOY_DIR)" --site "$(NETLIFY_SITE_ID)"; \
	elif command -v npx >/dev/null 2>&1; then \
		npx netlify deploy --dir "$(NETLIFY_DEPLOY_DIR)" --site "$(NETLIFY_SITE_ID)"; \
	else \
		printf "Netlify CLI non trovato. Installa con: npm install -g netlify-cli\n"; exit 1; \
	fi

deploy-prod: check ## Deploy produzione su Netlify tramite CLI
	@if command -v netlify >/dev/null 2>&1; then \
		netlify deploy --prod --dir "$(NETLIFY_DEPLOY_DIR)" --site "$(NETLIFY_SITE_ID)"; \
	elif command -v npx >/dev/null 2>&1; then \
		npx netlify deploy --prod --dir "$(NETLIFY_DEPLOY_DIR)" --site "$(NETLIFY_SITE_ID)"; \
	else \
		printf "Netlify CLI non trovato. Installa con: npm install -g netlify-cli\n"; exit 1; \
	fi

deploy-open: ## Stampa URL produzione Netlify
	@printf "%s\n" "$(NETLIFY_URL)"

tree: ## Mostra struttura rilevante del progetto
	@printf ".\n"
	@printf "├── index.html\n"
	@printf "├── netlify.toml\n"
	@printf "├── Makefile\n"
	@printf "├── assets/\n"
	@find assets -maxdepth 2 -type f | sort | sed 's#^#│   ├── #'
	@printf "└── docs/\n"
	@find docs -maxdepth 1 -type f | sort | sed 's#^#    ├── #'

clean: ## Rimuove cache temporanee locali
	@rm -rf .cache .netlify/cache
	@find . -name '.DS_Store' -delete
	@printf "Clean complete\n"
