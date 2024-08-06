from setuptools import find_packages, setup
from pathlib import Path

# Read the content of your README file
long_description = (Path(__file__).parent / 'README.txt').read_text()

setup(
    name="HousingPricePrediction",
    version="0.0.1",
    author="Asang Kumar Singh",
    author_email="asangkumar6666@gmail.com",
    description="A package for predicting housing prices",
    long_description=long_description,
    long_description_content_type='text/plain',  # Using plain text since README.txt is a .txt file
    install_requires=["pytest", "pandas", "numpy", "ensure", "scikit-learn", "tox"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
