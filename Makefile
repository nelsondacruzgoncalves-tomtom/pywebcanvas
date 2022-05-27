setup:
	python3 -m pip install poetry
	python3 -m poetry install

devserver:
	python3 -m poetry build
	cp -r dist pywebcanvas-project
	cd pywebcanvas-project && python3 -m poetry run python3 -m http.server 8080

build_docs: setup
	rm -rdf public/ pyodide.py js.py
	# Placeholder for pyscript dependencies
	touch pyodide.py
	echo "class JsProxy:" > pyodide.py
	echo "    pass" >> pyodide.py
	touch js.py
	# Generate docs
	poetry run pdoc pywebcanvas -o public/ --docformat numpy
	rm -rdf pyodide.py js.py
