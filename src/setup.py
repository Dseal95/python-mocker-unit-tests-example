from setuptools import find_packages, setup

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="simple-package",
    description="A simple package.",
    version="1.0.0",
    author="Dan Seal",
    install_requires=requirements,
    packages=find_packages(),
)
