OS?=undefined
ifeq ($(OS),Windows_NT)
	# Windows requires the .exe extension, otherwise the entry is ignored
	# @see https://stackoverflow.com/a/60318554/413531
    SHELL := bash.exe
else
    SHELL := bash
endif

# Bash strict mode
# -e => Instructs bash to immediately exit if any command has a non-zero exit status
# -u => A reference to any variable that has not bene previously defined will throw an error and make the program to exit
# -o pipefail => Setting prevents errors in a pipeline from being masked
.SHELLFLAGS := -eu -o pipefail -c

# Makefile config
# Display warning message when undefined variables are used
MAKEFLAGS += --warn-undefined-variables
# Remove all predefined rules
MAKEFLAGS += --no-builtin-rules

# Docker config
DOCKER_COMPOSE_DIR=./.docker
DOCKER_COMPOSE_FILE=$(DOCKER_COMPOSE_DIR)/docker-compose.yaml
DEFAULT_CONTAINER=workspace
DOCKER_COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE) --project-directory $(DOCKER_COMPOSE_DIR) --env-file $(DOCKER_COMPOSE_DIR)/.env
RUN_IN_DOCKER_CONTAINER=workspace

ifndef CONTAINER
	ARGS :=
endif

ifndef CONTAINER
	CONTAINER :=
endif

RUN_IN_DOCKER :=
ifeq ("$(wildcard /.dockerenv)","")
	RUN_IN_DOCKER := @$(DOCKER_COMPOSE) exec -T $(RUN_IN_DOCKER_CONTAINER)
endif

DEFAULT_GOAL := help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-27s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ [Setup]
.docker/.env:
	cp $(DOCKER_COMPOSE_DIR)/.env.example $(DOCKER_COMPOSE_DIR)/.env

.PHONY: pip-install
pip-install: ## Run pip install
	$(RUN_IN_DOCKER) pip3 install -r requirements.txt

##@ [Infrastructure]
.PHONY: docker-init
docker-init: .docker/.env ## Make sure the .env file exists for docker

.PHONY: docker-up
docker-up: docker-init ## Start all docker containers
	$(DOCKER_COMPOSE) up -d $(CONTAINER)

.PHONY: docker-down
docker-down: docker-init ## Stop all docker containers
	$(DOCKER_COMPOSE) down $(CONTAINER)

.PHONY: docker-build-from-scratch
docker-build-from-scratch: docker-init ## Build all docker images from scratch, without cache etc. Build a specific image by providing the service name via: make docker-build CONTAINER=<service>
	$(DOCKER_COMPOSE) rm -fs $(CONTAINER) && \
	$(DOCKER_COMPOSE) build --pull --no-cache $(CONTAINER) && \
	$(DOCKER_COMPOSE) up -d --force-recreate $(CONTAINER)

##@ [Python]
.PHONY: python
python: ## Run specific python file
	$(RUN_IN_DOCKER) python3.9 $(FILE)

.PHONY: run-tests
run-tests: ## Run all python tests
	$(RUN_IN_DOCKER) pytest test/

.PHONY: verify-setup
verify-setup: ## Run only tests for main.print_input()
	$(RUN_IN_DOCKER) pytest test/test_main.py


.PHONY: list
list:
	$(RUN_IN_DOCKER) pip list
