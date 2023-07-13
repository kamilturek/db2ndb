clean:
	rm -rf dist/ build/ **/*.egg-info/

build:
	pyproject-build

.PHONY: update-requirements sync-requirements clean build
