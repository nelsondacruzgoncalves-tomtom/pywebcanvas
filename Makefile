setup:
	python3 -m pip install poetry
	python3 -m poetry install

devserver:
	python3 -m poetry build
	cp -r dist pywebcanvas-project
	cd pywebcanvas-project && python3 -m poetry run python3 -m http.server 8080
