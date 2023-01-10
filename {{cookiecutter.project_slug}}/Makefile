init:
	git init
	git add -A
	git commit -m "Initial commit"
	git branch -M main
	@echo "push with: git push -u origin main"
install:
	{%- if cookiecutter.packaging == "poetry" %}
	poetry install
	{%- elif cookiecutter.packaging == "pipenv" %}
	pipenv install --dev
	{%- endif %}
lint:
	{{ cookiecutter.packaging }} run flake8
	{{ cookiecutter.packaging }} run black --check .
test: lint
	{{ cookiecutter.packaging }} run py.test
format:
	{{ cookiecutter.packaging }} run black .
start:
	{{ cookiecutter.packaging }} run python bot.py