from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Renan_Scarabelli",
    author_email="renanscarabelli@gmail.com",
    description="Pacote criado para entrega de projeto na DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenanScarabelli/processamento_imagens_dio"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)