install:
	poetry install

lint:
	poetry run flake8 brain_games

info:
	python3 --version
	poetry --version
	git --version
	poetry config --list
	poetry show

publish:
	poetry version $(V)
	poetry publish --build -r Hexlet
