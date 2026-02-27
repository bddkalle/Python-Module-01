*This project has been created as part of the 42 curriculum by fschnorr.*

# CodeCultivation - Object-Oriented Garden Systems

## Description
This repository contains my implementation of Python Module 01 from the 42 curriculum.
The project goal is to move from basic Python scripts to object-oriented design through a garden-management theme.

It covers:
- program entry points and script execution (`ex0`)
- classes and object initialization (`ex1`)
- object behavior and state changes over time (`ex2`)
- factory-style object creation (`ex3`)
- encapsulation and data protection (`ex4`)
- inheritance and specialized types (`ex5`)
- interacting components, class/static methods, and analytics (`ex6`)

## Instructions
Requirements:
- Python 3.10+
- code style compatible with flake8

Run an exercise:
```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

Optional lint check:
```bash
python3 -m flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

Project reference:
- subject PDF: `_docs/en.subject.pdf`

## Resources
Classic references:
- Python docs - classes: https://docs.python.org/3/tutorial/classes.html
- Python docs - control flow: https://docs.python.org/3/tutorial/controlflow.html
- Python docs - built-in functions: https://docs.python.org/3/library/functions.html
- PEP 8 style guide: https://peps.python.org/pep-0008/
- Real Python OOP guide: https://realpython.com/python3-object-oriented-programming/

AI usage in this project:
- Used for concept clarification (`__name__ == "__main__"`, `super()`, `@classmethod`, `@staticmethod`, type hints).
- Used for debugging support (scope issues, method calls, inheritance mistakes, formatting/flake8 fixes).
- Used for code-review style checks against subject requirements and expected output format.
- Final code decisions, structure, and submitted implementation were reviewed and adjusted manually.
