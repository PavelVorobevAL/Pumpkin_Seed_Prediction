test:
	python -m pytest

coverage:
	python -m pytest --cov=app --cov-report=term-missing

test-all:
	python -m pytest --cov=app --cov-report=term-missing