"""Setup script for pycashflow."""
from setuptools import setup, find_packages

__version__ = "0.0.0-1"


def load_requirements(fpath: str):
    """Loads a requirements.txt file into a list."""
    with open(fpath, "r", encoding="utf-8") as file:
        return file.read().split("\n")


setup(
    name="pycashflow",
    version=__version__,
    description="Easy manipulation of financial models.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
    extras_require={
        "dev": load_requirements("dev-requirements.txt"),
    },
)
