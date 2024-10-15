# PyRSS

PyRSS is an application for reading RSS feeds.

## Developement

### Requirements

#### Required:

- [Poetry](https://python-poetry.org/) package and dependencies manager.

#### Optional:

- [fish](https://fishshell.com/), the shell I use.
- [fish-poetry](https://github.com/ryoppippi/fish-poetry), a fish plugin for poetry.

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
python3 src/main.py
```

## Dependencies

### Developement dependencies:
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [pylint](https://pylint.pycqa.org/)
- [pytest](https://docs.pytest.org/en/6.2.x/)
