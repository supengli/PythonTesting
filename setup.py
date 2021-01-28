from setuptools import setup, find_packages

setup(
    name="supengli-python-testing",
    version=0.01,
    packages=find_packages(where="src"),
    package_dir={"":"src"}
)