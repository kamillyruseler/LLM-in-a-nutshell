run: 
	streamlit run mle/main.py
setup: requirements.txt
	pip install -r requirements.txt

lint:
	black . --check
	isort . --check-only
	flake8 .

test:
	python -m pytest mle/tests/tests.py -v

all: setup lint test run

.PHONY: run setup lint test all