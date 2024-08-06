from setuptools import find_packages, setup
from pathlib import Path

# Read the content of your README.md file
long_description = (Path(__file__).parent / 'README.md').read_text()

setup(
    name="HousingPricePrediction",
    version="0.0.1",
    author="Asang Kumar Singh",
    author_email="asangkumar6666@gmail.com",
    description="A package for predicting housing prices",
    long_description=long_description,
    long_description_content_type='text/markdown',  # Using Markdown content type for .md files
    install_requires=["pytest", "pandas", "numpy", "ensure", "scikit-learn", "tox"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
