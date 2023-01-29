help:
    just --list

##########################
## Formatting & Linting ##
##########################

format:
    black .

lint:
    pylint .

checks:
    @echo "Running checks..."
    black --check .


#####################
## Testing Targets ##
#####################

default_path := env_var("PWD") / "tests"

tests path=default_path:
    pytest -xv {{ path }}
