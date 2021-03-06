import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mathsfunlib",
    version="0.0.3",
    author="Yogeswaran Thulasidoss",
    author_email="yogeeswaran@gmail.com",
    description="Maths speed test question generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yogeswarant/mathsfunlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_requires=['pytest'],
    python_requires='>=3.6',
)
