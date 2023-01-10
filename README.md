# **cookiecutter python aiogram bot template**

# Install

## Requirements

- cookiecutter
- pipenv/poetry (choosable)
- make (optional for use make commands)
- other dependencies are installed from Pipfile/poetry.lock using `make install`

## Installing

GitHub:

```python
cookiecutter gh:golifox/cookiecutter-python-aiogram-bot.git 
```

Local template:

```
cookiecutter path/to/template 
```

*For install without any input add flag `--no-input`.*

**Important**
When using no-input flag you should write your Telegram token in `cookiecutter.json` before install OR in `.env` file after template install.

# Makefile commands

Install packages:

```
make install
```

Init GIT repository:

```
make init
```

Flake8 linter:

```
make lint
```

Start tests:

```
make test
```

"Black" code formatter:

```
make format
```

Run bot:

```
make start
```
