import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplecayennelpp",
    version="1.0.0",
    author="Philip Basford",
    author_email="P.J.Basford@soton.ac.uk",
    description="A class for cayenneLPP packet creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FEEprojects/cayennelpp-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)