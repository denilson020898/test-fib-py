from setuptools import find_packages, setup

setup(
    name="test_fib_py",
    version="0.0.1",
    author="Denilson",
    author_email="denilson020898@gmail.com",
    description="Recursive fibonacci",
    long_description="Basic library to calculate fibonacci bro",
    long_description_content_type="text/markdown",
    url="https://github.com/denilson020898/test-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System:: OS Independent",
    ],
    python_requires=">=3",
    tests_require=["pytest"],
)

