black:
	black advent_of_code_2021
	black tests

black-diff:
	black advent_of_code_2021 --diff
	black tests --diff

export:
	poetry export -f requirements.txt -o requirements.txt
	poetry export -f requirements.txt -o requirements_dev.txt --dev

flake8:
	flake8 advent_of_code_2021/ tests/ --statistics

install:
	poetry install

pre-commit: black flake8 test build

test:
	pytest -vvs --cov-report term-missing --cov=advent_of_code_2021 tests/

_update:
	poetry update

update: _update export pre-commit

update-diff:
	poetry update --dry-run | grep -i updat
