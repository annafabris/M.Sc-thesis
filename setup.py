import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msc-thesis-anna.fabris", # Replace with your own username
    version="0.0.1",
    author="Anna Fabris",
    description="A utilities library for my Ms.c thesis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/annafabris/M.Sc-thesis",
    license='MIT',
    packages=setuptools.find_packages(),
)
