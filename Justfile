help:
    just --list

default_path := env_var("PWD") / "tests"

tests path=default_path:
    pytest -xv {{ path }}
