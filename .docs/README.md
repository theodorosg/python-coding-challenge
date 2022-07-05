# Makefile targets

Convenience make targets that have been made to help with coding challenge.

## `make docker-build-from-scratch`

Builds all the docker images from scratch, without cache.

## `make docker-up`

Starts all the docker containers

## `make docker-down`

Stops all the docker containers

## `make pip-install`

Runs pip install (input is taken from `requirements.txt`)

## `make python FILE=<ARG>`

Run specific python file from outside the container
e.g `make python3.9-run FILE=main.py`

## `make run-tests`

Runs all the python tests

## `make verify-setup`

Verifies that the setup is working properly by running tests
for `main.print_input()`
