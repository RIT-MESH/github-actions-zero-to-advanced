.PHONY: validate yaml json markdown workflows python node help

help:
	@echo "Targets: validate, yaml, json, markdown, workflows, python, node"

validate: yaml json markdown workflows python node

yaml-json:
	python scripts/validate_yaml_json.py

yaml: yaml-json
json: yaml-json

markdown:
	node scripts/validate-markdown.js

workflows:
	python scripts/validate-workflows.py

python:
	cd examples/python-app && python -m pytest -q

node:
	cd examples/node-app && npm test
