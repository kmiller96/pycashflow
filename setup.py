from setuptools import setup, find_packages

__version__ = "0.0.0-1"


def load_requirements(fpath: str):
    with open(fpath, "r") as file:
        return file.read().split("\n")


setup(
    name="pycashflow",
    version=__version__,
    description="Easy manipulation of financial models.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
)
