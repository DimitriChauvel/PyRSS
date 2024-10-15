*<sub>Python 3.12.3</sub>*

# PyRSS
PyRSS is an application for reading RSS feeds.

## Developement

### Requirements

#### Required:

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [Poetry](https://python-poetry.org/)

#### Optional for [Fish shell](https://fishshell.com/):

- [fish-poetry](https://github.com/ryoppippi/fish-poetry)

#### Visual Studio Code extensions:

*<sub>Developed by Microsoft</sub>*
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)
- [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)


### Clone repository

#### HTTP :

```sh
git clone https://github.com/DimitriChauvel/PyRSS.git
```

#### SSH :

```sh
git clone git@github.com:DimitriChauvel/PyRSS.git
```

### Install dependencies

```sh
cd PyRSS
poetry install
```

### Run project

At the root of the project, run the following command:

```sh
poetry run start
```

## Dependencies

### Developement dependencies:
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [pylint](https://pylint.pycqa.org/)
- [pytest](https://docs.pytest.org/en/6.2.x/)

### Scripts
 ```sh
poetry run lint-fix   # run black on all files
poetry run lint       # run pylint on all files
poetry run tests      # run tests with pytest
```
