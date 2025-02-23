SHELL := /usr/bin/bash

hello:
	echo "hello, world"

setup:
	python3 -m venv venv
	python3 -m pip install -r requirements.txt

run:
	source venv/bin/activate
	rm ./fixtures/2025-02-23-sixteen-pages-output.pdf
	python3 pdf_diy_binding_paginator.py -i ./fixtures/2024-12-05-sixteen-pages.pdf -o ./fixtures/2025-02-23-sixteen-pages-output.pdf -s 0.8 -g 0.75
	open ./fixtures/2025-02-23-sixteen-pages-output.pdf
