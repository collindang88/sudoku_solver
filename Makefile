SRC_DIR = src/

.PHONY: ls py-fmt py-lint all

ls:
	@echo "Available targets:"
	@echo "  make install-deps    Install package depedencies"
	@echo "  make freeze-deps     Freezes package depedencies to requirements.txt"
	@echo "  make py-fmt          Format the code"
	@echo "  make py-lint         Lint the code"
	@echo "  make all             Install deps, freeze deps, format, and lint the code"

check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
        tput setaf 1; echo "Please activate your virtual environment first."; tput sgr0; \
        exit 1; \
    fi

install-deps: check-venv
	@pip install -r requirements.txt
	@tput setaf 2; echo "Depedencies installed!"; tput sgr0

freeze-deps:
	@pip freeze > requirements.txt
	@tput setaf 2; echo "Depedencies updated!"; tput sgr0

py-fmt:
	@autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place $(SRC_DIR)
	@isort $(SRC_DIR)
	@black $(SRC_DIR)
	@tput setaf 2; echo "Formatting done!"; tput sgr0

py-lint:
	@flake8 $(SRC_DIR)
	@tput setaf 2; echo "Linting done!"; tput sgr0

all: install-deps freeze-deps py-fmt py-lint
