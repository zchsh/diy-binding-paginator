SHELL := /usr/bin/bash

hello:
	echo "hello, world"

setup:
	python3 -m venv venv
	python3 -m pip install -r requirements.txt

run16:
	source venv/bin/activate
	rm -f ./fixtures/2025-02-23-sixteen-pages-output.pdf
	python3 pdf_diy_binding_paginator.py -i ./fixtures/2024-12-05-sixteen-pages.pdf -o ./fixtures/2025-02-23-sixteen-pages-output.pdf -s 0.8 -g 0.75
	open ./fixtures/2025-02-23-sixteen-pages-output.pdf

og:
	source venv/bin/activate
	python3 pdf_diy_binding_paginator.py --inputFile ~/Downloads/figma-export.pdf --outputFile ~/Downloads/figma-export-for-diy-binding.pdf --scale 0.8 --gutter 0.75
	open ~/Downloads/figma-export-for-diy-binding.pdf

splitOg:
	source venv/bin/activate
	python3 pdf_split_even_odd.py --inputFile ~/Downloads/figma-export-for-diy-binding.pdf
