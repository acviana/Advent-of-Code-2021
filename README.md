# Advent of Code 2021

Project overview and notes.

### Setup Instructions

This project uses [Poetry](https://python-poetry.org/) for dependency management.
Once you have installed Poetry you can setup the project by running `poetry install` in the project directory.

A `requirements.txt` file is included if you prefer to set up your own environment with pip or another tool.

### Development Instructions
The Poetry development dependencies are installed by default when you run `poetry install`. If you are using pip you can install them from the `requirements_dev.txt` file.
This project uses the pre-commit package to check commits. You can install this hooks from this project by running `pre-commit install`.

A suggested workflow is documented in the `Makefile`

```console
# Created the template module
$ make setup-day-with-template day=1
cp -vn advent_of_code_2021/template_module.py advent_of_code_2021/day_1.py
advent_of_code_2021/template_module.py -> advent_of_code_2021/day_1.py
cp -vn advent_of_code_2021/template_test.py test/day_1_test.py
advent_of_code_2021/template_test.py -> test/day_1_test.py
touch inputs/day_1_input.txt
touch puzzles/day_1.md

# Run the code
$ make run day=1
python advent_of_code_2021/day_1.py
Length of data: 2000
Length of result: 1999
Solution: 1390

# Lint, format, type check, and test
$ make pre-commit
...

# Stage work
make stage-day day=1
git add advent_of_code_2021/day_1.py
git add tests/day_1_test.py
git add inputs/day_1_input.txt
git add puzzles/day_1.md
```

### Project Design
This repo is a mixture of this [Cookiecutter project template](https://github.com/acviana/python-project-template) and [last year's repo](https://github.com/acviana/advent-of-code-2020).

Each day's puzzle has 4 section:

 - The puzzle write-up: `puzzles/day_$(day).md`
 - The puzzle input: `inputs/day_$(day)_input.txt`
 - The puzzle test module: `tests/day_$(day)_test.py`
 - The actual solution module: `advent_of_code_2021/day_$(day).py`
